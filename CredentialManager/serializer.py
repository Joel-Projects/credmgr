import datetime
import re

import CredentialManager.models
from .exceptions import SerializerException


class Serializer(object):
    '''The serializer builds :class:`.BaseModel` objects.'''

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'str': str,
        'bool': bool,
        'datetime': datetime.datetime,
        'object': object,
        'dict': dict,
        'list': list
        }

    def __init__(self, credmgr):
        '''Initialize an Objector instance.

        :param credmgr: An instance of :class:`~.CredentialManager`.

        '''
        self._credmgr = credmgr

    @staticmethod
    def deserialize_datatime(string):
        '''Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        '''
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise SerializerException(f"Failed to parse `{string}` as datetime object")

    @staticmethod
    def deserialize_date(string):
        '''Deserializes string to date.

        :param string: str.
        :return: date.
        '''
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise SerializerException(f"Failed to parse `{string}` as date object")

    @staticmethod
    def deserialize_object(value):
        '''Return a original value.

        :return: object.
        '''
        return value

    @staticmethod
    def deserialize_primitive(data, objectType):
        '''Deserializes string to primitive type.

        :param data: str.
        :param objectType: class literal.

        :return: int, long, float, str, bool.
        '''
        try:
            return objectType(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def deserialize(self, response):
        '''Deserializes response into an object.

        :param response: Response object to be deserialized.

        :return: deserialized object.
        '''
        data = response.json()
        if isinstance(data, list) and all([i['resource_type'] == data[0]['resource_type'] for i in data]):
            if data:
                resourceType = f'list[{data[0]["resource_type"]}]'
            else:
                return data
        else:
            resourceType = data.get('resource_type', 'dict')
        return self.__deserialize(data, resourceType)

    def __deserialize(self, data, objectType):
        '''Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param objectType: class literal, or string of class name.

        :return: object.
        '''
        if data is None:
            return None

        if type(objectType) == str:
            if objectType.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', objectType).group(1)
                return [self.__deserialize(sub_data, sub_kls) for sub_data in data]

            if objectType.startswith('dict'):
                return {k: self.__deserialize(v, type(v)) for k, v in data.items()}

            # convert str to class
            if objectType in self.NATIVE_TYPES_MAPPING:
                objectType = self.NATIVE_TYPES_MAPPING[objectType]
            else:
                objectType = getattr(CredentialManager.models, objectType)

        if objectType in self.PRIMITIVE_TYPES:
            return self.deserialize_primitive(data, objectType)
        elif objectType == object:
            return self.deserialize_object(data)
        elif objectType == datetime.date:
            return self.deserialize_date(data)
        elif objectType == datetime.datetime:
            return self.deserialize_datatime(data)
        elif objectType == dict:
            return self.__deserialize(data, 'dict')
        else:
            return self.__deserialize_model(data, objectType)

    def __hasattr(self, object, name):
        return name in object.__class__.__dict__

    def __deserialize_model(self, data, objectType):
        '''Deserializes list or dict to model.

        :param data: dict, list.
        :param objectType: class literal.
        :return: model object.
        '''

        if not objectType._attrTypes:
            return data

        kwargs = {}
        if objectType._attrTypes is not None:
            for attr, attrType in objectType._attrTypes.items():
                if data is not None and attr in data and isinstance(data, (list, dict)):
                    value = data[attr]
                    kwargs[attr] = self.__deserialize(value, attrType)
        try:
            instance = objectType(self._credmgr, **kwargs)
        except TypeError:
            for key, value in kwargs.items():
                setattr(objectType, key, value)
            instance = objectType
        if isinstance(instance, dict) and objectType._attrTypes is not None and isinstance(data, dict):
            for key, value in data.items():
                if key not in objectType._attrTypes:
                    instance[key] = value
        return instance