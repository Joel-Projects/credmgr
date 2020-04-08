import copy
import logging
import multiprocessing
import sys
from http import client

import urllib3


class Config(object):

    _default = None

    def __init__(self, host="https://credmgr.jesassn.org/api/v1", api_key=None, username=None, password=None):

        # Default Base url
        self.host = host
        # Authentication Settings
        # API Key
        self.api_key = api_key
        # Username for HTTP basic authentication
        self.username = username
        # Password for HTTP basic authentication
        self.password = password

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("CredentialManager")
        self.logger["requests_logger"] = logging.getLogger("requests")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

    @classmethod
    def set_default(cls, default):
        cls._default = default

    @property
    def logger_file(self):
        '''The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file __path.
        :type: str
        '''
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        '''The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file __path.
        :type: str
        '''
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        '''Debug status

        :param value: The debug status, True or False.
        :type: bool
        '''
        return self.__debug

    @debug.setter
    def debug(self, value):
        '''Debug status

        :param value: The debug status, True or False.
        :type: bool
        '''
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            client.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            client.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        '''The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        '''
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        '''The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        '''
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_basic_auth_token(self):
        '''Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        '''
        return urllib3.util.make_headers(basic_auth=f'{self.username}:{self.password}').get('authorization')

    def auth_settings(self):
        '''Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        '''
        return {
            'apiKey': {
                'type': 'api_key', 'in': 'header', 'key': 'X-API-KEY', 'value': self.api_key
                },
            'basic': {
                'type': 'basic', 'in': 'header', 'key': 'Authorization', 'value': self.get_basic_auth_token()
                },

            }

    def to_debug_report(self):
        '''Gets the essential information for debugging.

        :return: The report for debugging.
        '''
        return f"Python SDK Debug Report:\nOS: {sys.platform}\nPython Version: {sys.version}\nVersion of the API: 1.0\nSDK Package Version: 1.0.0"