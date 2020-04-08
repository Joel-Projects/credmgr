import re

# python 2 and python 3 compatibility library
from CredentialManager.api_client import ApiClient


class UsersApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_user_by_id(self, user_id, **kwargs):
        '''Delete a user by ID

        **PERMISSIONS: Admin role is required.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_by_id(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_by_id_with_http_info(user_id, **kwargs)
        else:
            (data) = self.delete_user_by_id_with_http_info(user_id, **kwargs)
            return data

    def delete_user_by_id_with_http_info(self, user_id, **kwargs):
        '''Delete a user by ID

        **PERMISSIONS: Admin role is required.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_by_id_with_http_info(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method delete_user_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_user_by_id`")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

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

        return self.api_client.call_api('/users/{user_id}', 'DELETE', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_apps_by_user_id(self, user_id, **kwargs):
        '''Get items that is owned by user

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_apps_by_user_id(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: UserItems
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_apps_by_user_id_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_apps_by_user_id_with_http_info(user_id, **kwargs)
            return data

    def get_apps_by_user_id_with_http_info(self, user_id, **kwargs):
        '''Get items that is owned by user

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_apps_by_user_id_with_http_info(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: UserItems
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_apps_by_user_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_apps_by_user_id`")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

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

        return self.api_client.call_api('/users/{user_id}/apps', 'GET', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='UserItems', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_user_by_id(self, user_id, **kwargs):
        '''Get user details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_by_id(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_by_id_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_user_by_id_with_http_info(user_id, **kwargs)
            return data

    def get_user_by_id_with_http_info(self, user_id, **kwargs):
        '''Get user details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_by_id_with_http_info(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_user_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_by_id`")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

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

        return self.api_client.call_api('/users/{user_id}', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='User', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_user_me(self, **kwargs):
        '''Get current user details

        **PERMISSIONS: At least Active user is required.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_me(async_req=True)
        >>> result = thread.get()


        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_me_with_http_info(**kwargs)
        else:
            (data) = self.get_user_me_with_http_info(**kwargs)
            return data

    def get_user_me_with_http_info(self, **kwargs):
        '''Get current user details

        **PERMISSIONS: At least Active user is required.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_me_with_http_info(async_req=True)
        >>> result = thread.get()


        :return: User
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
                                " to method get_user_me" % key)
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

        return self.api_client.call_api('/users/me', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='User', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_users(self, **kwargs):
        '''List of users

        **PERMISSIONS: Admin role is required.**   Returns a list of users starting from ``offset`` limited by ``limit`` parameter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :return: list[BaseUser]
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_with_http_info(**kwargs)
        else:
            (data) = self.get_users_with_http_info(**kwargs)
            return data

    def get_users_with_http_info(self, **kwargs):
        '''List of users

        **PERMISSIONS: Admin role is required.**   Returns a list of users starting from ``offset`` limited by ``limit`` parameter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_with_http_info(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :return: list[BaseUser]
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_users" % key)
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_users`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_users`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError(
                "Invalid value for parameter `offset` when calling `get_users`, must be a value greater than or equal to `0`")
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))

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

        return self.api_client.call_api('/users/', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='list[BaseUser]', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_apps_by_user_id(self, user_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_apps_by_user_id(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_apps_by_user_id_with_http_info(user_id, **kwargs)
        else:
            (data) = self.options_apps_by_user_id_with_http_info(user_id, **kwargs)
            return data

    def options_apps_by_user_id_with_http_info(self, user_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_apps_by_user_id_with_http_info(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_apps_by_user_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `options_apps_by_user_id`")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

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

        return self.api_client.call_api('/users/{user_id}/apps', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_user_by_id(self, user_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_user_by_id(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_user_by_id_with_http_info(user_id, **kwargs)
        else:
            (data) = self.options_user_by_id_with_http_info(user_id, **kwargs)
            return data

    def options_user_by_id_with_http_info(self, user_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_user_by_id_with_http_info(user_id, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_user_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `options_user_by_id`")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

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

        return self.api_client.call_api('/users/{user_id}', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_user_me(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_user_me(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_user_me_with_http_info(**kwargs)
        else:
            (data) = self.options_user_me_with_http_info(**kwargs)
            return data

    def options_user_me_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_user_me_with_http_info(async_req=True)
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
                                " to method options_user_me" % key)
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

        return self.api_client.call_api('/users/me', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_users(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_users(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_users_with_http_info(**kwargs)
        else:
            (data) = self.options_users_with_http_info(**kwargs)
            return data

    def options_users_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_users_with_http_info(async_req=True)
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
                                " to method options_users" % key)
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

        return self.api_client.call_api('/users/', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def patch_user_by_id(self, user_id, body, **kwargs):
        '''Patch user details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_user_by_id(user_id, body, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :param list[Body7] body: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_user_by_id_with_http_info(user_id, body, **kwargs)
        else:
            (data) = self.patch_user_by_id_with_http_info(user_id, body, **kwargs)
            return data

    def patch_user_by_id_with_http_info(self, user_id, body, **kwargs):
        '''Patch user details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_user_by_id_with_http_info(user_id, body, async_req=True)
        >>> result = thread.get()


        :param int user_id: (required)
        :param list[Body7] body: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_id', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method patch_user_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_user_by_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_user_by_id`")

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

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

        return self.api_client.call_api('/users/{user_id}', 'PATCH', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='User', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_users(self, username, password, **kwargs):
        '''Create a new user

        **PERMISSIONS: Admin role is required.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_users(username, password, async_req=True)
        >>> result = thread.get()


        :param str username: Username for new user (Example: ```spaz```) (required)
        :param str password: Password for new user (Example: ```supersecurepassword```) (required)
        :param str default_settings: Default values to use for new apps (Example: ```{\"database_flavor\": \"postgres\", \"database_host\": \"localhost\"}```)
        :param bool is_admin: Is the user an admin? Allows the user to see all objects and create users (Default: ``false``)
        :param bool is_active: Is the user active? Allows the user to sign in (Default: ``true``)
        :param bool is_regular_user: (Internal use only)
        :param bool is_internal: (Internal use only)
        :param str reddit_username:
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_users_with_http_info(username, password, **kwargs)
        else:
            (data) = self.post_users_with_http_info(username, password, **kwargs)
            return data

    def post_users_with_http_info(self, username, password, **kwargs):
        '''Create a new user

        **PERMISSIONS: Admin role is required.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_users_with_http_info(username, password, async_req=True)
        >>> result = thread.get()


        :param str username: Username for new user (Example: ```spaz```) (required)
        :param str password: Password for new user (Example: ```supersecurepassword```) (required)
        :param str default_settings: Default values to use for new apps (Example: ```{\"database_flavor\": \"postgres\", \"database_host\": \"localhost\"}```)
        :param bool is_admin: Is the user an admin? Allows the user to see all objects and create users (Default: ``false``)
        :param bool is_active: Is the user active? Allows the user to sign in (Default: ``true``)
        :param bool is_regular_user: (Internal use only)
        :param bool is_internal: (Internal use only)
        :param str reddit_username:
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['username', 'password', 'default_settings', 'is_admin', 'is_active', 'is_regular_user', 'is_internal',
                      'reddit_username']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_users" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `post_users`")
        # verify the required parameter 'password' is set
        if ('password' not in params or params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `post_users`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'username' in params:
            form_params.append(('username', params['username']))
        if 'password' in params:
            form_params.append(('password', params['password']))
        if 'default_settings' in params:
            form_params.append(('default_settings', params['default_settings']))
        if 'is_admin' in params:
            form_params.append(('is_admin', params['is_admin']))
        if 'is_active' in params:
            form_params.append(('is_active', params['is_active']))
        if 'is_regular_user' in params:
            form_params.append(('is_regular_user', params['is_regular_user']))
        if 'is_internal' in params:
            form_params.append(('is_internal', params['is_internal']))
        if 'reddit_username' in params:
            form_params.append(('reddit_username', params['reddit_username']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/users/', 'POST', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='User', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))