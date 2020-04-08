import datetime
import json
import re
from json import JSONDecodeError

from . import __version__

import CredentialManager.models
from CredentialManager import requestor
from CredentialManager.config import Config
from .exceptions import ApiException


class ApiClient(object):
    '''Generic API client for Swagger client library builds.

    Swagger generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the Swagger
    templates.

    :param config: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    '''

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {'int': int, 'long': int, 'float': float, 'str': str, 'bool': bool, 'date': datetime.date, 'datetime': datetime.datetime, 'object': object, 'dict': dict, 'list': list}

    def __init__(self, credmgr, config, header_name=None, header_value=None):
        if config is None:
            config = Config()
        self.config = config
        self._credmgr = credmgr
        self.requestor = requestor.Requestor(self.config)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        # Set default User-Agent.
        self.user_agent = f'CredentialManager/{__version__}'

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
            raise ApiException(status=0, reason=f"Failed to parse `{string}` as datetime object")

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
            raise ApiException(status=0, reason="Failed to parse `{0}` as date object".format(string))

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

    @staticmethod
    def select_header_content_type(content_types):
        '''Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        '''
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    @staticmethod
    def select_header_accept(accepts):
        '''Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        '''
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    @staticmethod
    def parameters_to_tuples(params, collection_formats):
        '''Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        '''
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append((k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    @property
    def user_agent(self):
        '''User agent for this API client'''
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(self, resource_path, method, query_params=None, header_params=None, body=None, params=None, response_type=None, collection_formats=None, _request_timeout=None):

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)

        # post parameters
        if params:
            params = self.sanitize_for_serialization(params)

        # auth setting
        self.update_params_for_auth(header_params)
        if method == 'POST':
            header_params['Content-Type'] = 'application/x-www-form-urlencoded'

        # request url
        url = self.config.host + resource_path

        # perform request and return response
        response_data = self.request(method, url, query_params=query_params, headers=header_params, params=params, _request_timeout=_request_timeout)

        self.last_response = response_data

        if response_type:
            return_data = self.deserialize(response_data, response_type)
        else:
            return_data = None

        return return_data, response_data.status_code, response_data.headers

    def sanitize_for_serialization(self, obj):
        '''Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        '''
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `_swagger_types`, `_attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj._attribute_map[attr]: getattr(obj, attr) for attr, _ in obj._swagger_types.items() if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val) for key, val in obj_dict.items()}

    def deserialize(self, response, response_type):
        '''Deserializes response into an object.

        :param response: Response object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        '''
        try:
            return self.__deserialize(response.json(), response_type)
        except JSONDecodeError:
            if response.status_code == 404:
                raise ApiException(response.status_code, 'Not Found')


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

            if objectType.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', objectType).group(2)
                return {k: self.__deserialize(v, sub_kls) for k, v in data.items()}

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
        else:
            return self.__deserialize_model(data, objectType)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None, params=None, response_type=None, collection_formats=None, _preload_content=True, _request_timeout=None):
        '''Makes the HTTP request (synchronous) and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
            for `multipart/form-data`.
: execute request asynchronously
        :param collection_formats: dict of collection formats for __path, query,
            header, and post parameters.
        :param _request_timeout: timeout setting for this request. If one number provided, it will be total request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
        :return:
        '''
        return self.__call_api(resource_path, method, query_params, header_params, body, params, response_type, collection_formats, _request_timeout)

    def request(self, method, url, query_params=None, headers=None, params=None, _request_timeout=None):
        '''Makes the HTTP request using RESTClient.'''
        return self.requestor.request(url=url, method=method, params=query_params, headers=headers, data=params, timeout=_request_timeout)

    def update_params_for_auth(self, headers):
        '''Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        '''

        for auth in ['apiKey', 'basic']:
            auth_setting = self.config.auth_settings().get(auth)
            if auth_setting:
                if not auth_setting['value']:
                    continue
                elif auth_setting['in'] == 'header':
                    headers[auth_setting['key']] = auth_setting['value']
                else:
                    raise ValueError('Authentication token must be inz `header`')

    def __hasattr(self, object, name):
        return name in object.__class__.__dict__

    def __deserialize_model(self, data, objectType):
        '''Deserializes list or dict to model.

        :param data: dict, list.
        :param objectType: class literal.
        :return: model object.
        '''

        if not objectType._swagger_types and not self.__hasattr(objectType, 'get_real_child_model'):
            return data

        kwargs = {}
        if objectType._swagger_types is not None:
            for attr, attr_type in objectType._swagger_types.items():
                if data is not None and objectType._attribute_map[attr] in data and isinstance(data, (list, dict)):
                    value = data[objectType._attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)
        try:
            instance = objectType(self._credmgr, **kwargs)
        except TypeError:
            for key, value in kwargs.items():
                setattr(objectType, key, value)
            instance = objectType
        if isinstance(instance, dict) and objectType._swagger_types is not None and isinstance(data, dict):
            for key, value in data.items():
                if key not in objectType._swagger_types:
                    instance[key] = value
        if self.__hasattr(instance, 'get_real_child_model'):
            objectType_name = instance.get_real_child_model(data)
            if objectType_name:
                instance = self.__deserialize(data, objectType_name)
        return instance