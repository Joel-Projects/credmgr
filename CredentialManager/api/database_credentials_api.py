import re

# python 2 and python 3 compatibility library
from CredentialManager.api_client import ApiClient


class DatabaseCredentialsApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_database_credential_by_id(self, database_credential_id, **kwargs):
        '''Delete a Database Credential by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_database_credential_by_id(database_credential_id, async_req=True)
        >>> result = thread.get()


        :param int database_credential_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_database_credential_by_id_with_http_info(database_credential_id, **kwargs)
        else:
            (data) = self.delete_database_credential_by_id_with_http_info(database_credential_id, **kwargs)
            return data

    def delete_database_credential_by_id_with_http_info(self, database_credential_id, **kwargs):
        '''Delete a Database Credential by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_database_credential_by_id_with_http_info(database_credential_id, async_req=True)
        >>> result = thread.get()


        :param int database_credential_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['database_credential_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method delete_database_credential_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_credential_id' is set
        if ('database_credential_id' not in params or params['database_credential_id'] is None):
            raise ValueError("Missing the required parameter `database_credential_id` when calling `delete_database_credential_by_id`")

        collection_formats = {}

        path_params = {}
        if 'database_credential_id' in params:
            path_params['database_credential_id'] = params['database_credential_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/database_credentials/{database_credential_id}', 'DELETE', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_database_credential_by_id(self, database_credential_id, **kwargs):
        '''Get Database Credential details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_database_credential_by_id(database_credential_id, async_req=True)
        >>> result = thread.get()


        :param int database_credential_id: (required)
        :return: DatabaseCredential
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_database_credential_by_id_with_http_info(database_credential_id, **kwargs)
        else:
            (data) = self.get_database_credential_by_id_with_http_info(database_credential_id, **kwargs)
            return data

    def get_database_credential_by_id_with_http_info(self, database_credential_id, **kwargs):
        '''Get Database Credential details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_database_credential_by_id_with_http_info(database_credential_id, async_req=True)
        >>> result = thread.get()


        :param int database_credential_id: (required)
        :return: DatabaseCredential
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['database_credential_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_database_credential_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_credential_id' is set
        if ('database_credential_id' not in params or params['database_credential_id'] is None):
            raise ValueError("Missing the required parameter `database_credential_id` when calling `get_database_credential_by_id`")

        collection_formats = {}

        path_params = {}
        if 'database_credential_id' in params:
            path_params['database_credential_id'] = params['database_credential_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/database_credentials/{database_credential_id}', 'GET', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type='DatabaseCredential',
                                        collection_formats=collection_formats, _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def get_database_credentials(self, **kwargs):
        '''List of Database Credentials

        **PERMISSIONS: At least Active user is required.**   Returns a list of Database Credentials starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Database Credentials for other users. Regular users will see their own Database Credentials.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_database_credentials(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseDatabaseCredential]
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_database_credentials_with_http_info(**kwargs)
        else:
            (data) = self.get_database_credentials_with_http_info(**kwargs)
            return data

    def get_database_credentials_with_http_info(self, **kwargs):
        '''List of Database Credentials

        **PERMISSIONS: At least Active user is required.**   Returns a list of Database Credentials starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Database Credentials for other users. Regular users will see their own Database Credentials.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_database_credentials_with_http_info(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseDatabaseCredential]
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['limit', 'offset', 'owner_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_database_credentials" % key)
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_database_credentials`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_database_credentials`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError(
                "Invalid value for parameter `offset` when calling `get_database_credentials`, must be a value greater than or equal to `0`")
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'owner_id' in params:
            query_params.append(('owner_id', params['owner_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/database_credentials/', 'GET', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='list[BaseDatabaseCredential]', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_database_credential_by_id(self, database_credential_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_database_credential_by_id(database_credential_id, async_req=True)
        >>> result = thread.get()


        :param int database_credential_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_database_credential_by_id_with_http_info(database_credential_id, **kwargs)
        else:
            (data) = self.options_database_credential_by_id_with_http_info(database_credential_id, **kwargs)
            return data

    def options_database_credential_by_id_with_http_info(self, database_credential_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_database_credential_by_id_with_http_info(database_credential_id, async_req=True)
        >>> result = thread.get()


        :param int database_credential_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['database_credential_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_database_credential_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_credential_id' is set
        if ('database_credential_id' not in params or params['database_credential_id'] is None):
            raise ValueError("Missing the required parameter `database_credential_id` when calling `options_database_credential_by_id`")

        collection_formats = {}

        path_params = {}
        if 'database_credential_id' in params:
            path_params['database_credential_id'] = params['database_credential_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/database_credentials/{database_credential_id}', 'OPTIONS', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_database_credentials(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_database_credentials(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_database_credentials_with_http_info(**kwargs)
        else:
            (data) = self.options_database_credentials_with_http_info(**kwargs)
            return data

    def options_database_credentials_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_database_credentials_with_http_info(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_database_credentials" % key)
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/database_credentials/', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def patch_database_credential_by_id(self, database_credential_id, body, **kwargs):
        '''Patch database_credential details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_database_credential_by_id(database_credential_id, body, async_req=True)
        >>> result = thread.get()


        :param int database_credential_id: (required)
        :param list[Body2] body: (required)
        :return: DatabaseCredential
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_database_credential_by_id_with_http_info(database_credential_id, body, **kwargs)
        else:
            (data) = self.patch_database_credential_by_id_with_http_info(database_credential_id, body, **kwargs)
            return data

    def patch_database_credential_by_id_with_http_info(self, database_credential_id, body, **kwargs):
        '''Patch database_credential details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_database_credential_by_id_with_http_info(database_credential_id, body, async_req=True)
        >>> result = thread.get()


        :param int database_credential_id: (required)
        :param list[Body2] body: (required)
        :return: DatabaseCredential
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['database_credential_id', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method patch_database_credential_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_credential_id' is set
        if ('database_credential_id' not in params or params['database_credential_id'] is None):
            raise ValueError("Missing the required parameter `database_credential_id` when calling `patch_database_credential_by_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_database_credential_by_id`")

        collection_formats = {}

        path_params = {}
        if 'database_credential_id' in params:
            path_params['database_credential_id'] = params['database_credential_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/database_credentials/{database_credential_id}', 'PATCH', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type='DatabaseCredential',
                                        collection_formats=collection_formats, _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def post_database_credentials(self, app_name, database_username, database_host, database_flavor, **kwargs):
        '''Create a new Database Credential

        **PERMISSIONS: At least Active user is required.**   Database Credentials are used for logging and error reporting in applications
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_database_credentials(name, database_username, database_host, database_flavor, async_req=True)
        >>> result = thread.get()


        :param str app_name: Name of the Database Credential (required)
        :param str database_username: Username to use to connect to the database (required)
        :param str database_host: Database server address, defaults to `localhost` (required)
        :param str database_flavor: Type of database, defaults to `postgres` (required)
        :param str database: Working database to use, defaults to `postgres`
        :param int owner_id: Owner of the app. Requires Admin to create for other users.
        :return: DatabaseCredential
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_database_credentials_with_http_info(app_name, database_username, database_host, database_flavor, **kwargs)
        else:
            (data) = self.post_database_credentials_with_http_info(app_name, database_username, database_host, database_flavor,
                                                                   **kwargs)
            return data

    def post_database_credentials_with_http_info(self, app_name, database_username, database_host, database_flavor, **kwargs):
        '''Create a new Database Credential

        **PERMISSIONS: At least Active user is required.**   Database Credentials are used for logging and error reporting in applications
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_database_credentials_with_http_info(name, database_username, database_host, database_flavor, async_req=True)
        >>> result = thread.get()


        :param str app_name: Name of the Database Credential (required)
        :param str database_username: Username to use to connect to the database (required)
        :param str database_host: Database server address, defaults to `localhost` (required)
        :param str database_flavor: Type of database, defaults to `postgres` (required)
        :param str database: Working database to use, defaults to `postgres`
        :param int owner_id: Owner of the app. Requires Admin to create for other users.
        :return: DatabaseCredential
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['name', 'database_username', 'database_host', 'database_flavor', 'database', 'owner_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_database_credentials" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `post_database_credentials`")
        # verify the required parameter 'database_username' is set
        if ('database_username' not in params or params['database_username'] is None):
            raise ValueError("Missing the required parameter `database_username` when calling `post_database_credentials`")
        # verify the required parameter 'database_host' is set
        if ('database_host' not in params or params['database_host'] is None):
            raise ValueError("Missing the required parameter `database_host` when calling `post_database_credentials`")
        # verify the required parameter 'database_flavor' is set
        if ('database_flavor' not in params or params['database_flavor'] is None):
            raise ValueError("Missing the required parameter `database_flavor` when calling `post_database_credentials`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'database_username' in params:
            form_params.append(('database_username', params['database_username']))
        if 'database_host' in params:
            form_params.append(('database_host', params['database_host']))
        if 'database' in params:
            form_params.append(('database', params['database']))
        if 'database_flavor' in params:
            form_params.append(('database_flavor', params['database_flavor']))
        if 'owner_id' in params:
            form_params.append(('owner_id', params['owner_id']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/database_credentials/', 'POST', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='DatabaseCredential', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))