import re

# python 2 and python 3 compatibility library
from CredentialManager.api_client import ApiClient


class UserVerificationsApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_user_verification_by_id(self, user_verification_id, **kwargs):
        '''Delete a User Verification by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_verification_by_id(user_verification_id, async_req=True)
        >>> result = thread.get()


        :param int user_verification_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_verification_by_id_with_http_info(user_verification_id, **kwargs)
        else:
            (data) = self.delete_user_verification_by_id_with_http_info(user_verification_id, **kwargs)
            return data

    def delete_user_verification_by_id_with_http_info(self, user_verification_id, **kwargs):
        '''Delete a User Verification by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_verification_by_id_with_http_info(user_verification_id, async_req=True)
        >>> result = thread.get()


        :param int user_verification_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_verification_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method delete_user_verification_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_verification_id' is set
        if ('user_verification_id' not in params or params['user_verification_id'] is None):
            raise ValueError("Missing the required parameter `user_verification_id` when calling `delete_user_verification_by_id`")

        collection_formats = {}

        path_params = {}
        if 'user_verification_id' in params:
            path_params['user_verification_id'] = params['user_verification_id']

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

        return self.api_client.call_api('/user_verifications/{user_verification_id}', 'DELETE', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_user_verification_by_id(self, user_verification_id, **kwargs):
        '''Get User Verification details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_verification_by_id(user_verification_id, async_req=True)
        >>> result = thread.get()


        :param int user_verification_id: (required)
        :return: UserVerification
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_verification_by_id_with_http_info(user_verification_id, **kwargs)
        else:
            (data) = self.get_user_verification_by_id_with_http_info(user_verification_id, **kwargs)
            return data

    def get_user_verification_by_id_with_http_info(self, user_verification_id, **kwargs):
        '''Get User Verification details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_verification_by_id_with_http_info(user_verification_id, async_req=True)
        >>> result = thread.get()


        :param int user_verification_id: (required)
        :return: UserVerification
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_verification_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_user_verification_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_verification_id' is set
        if ('user_verification_id' not in params or params['user_verification_id'] is None):
            raise ValueError("Missing the required parameter `user_verification_id` when calling `get_user_verification_by_id`")

        collection_formats = {}

        path_params = {}
        if 'user_verification_id' in params:
            path_params['user_verification_id'] = params['user_verification_id']

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

        return self.api_client.call_api('/user_verifications/{user_verification_id}', 'GET', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type='UserVerification', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_user_verifications(self, **kwargs):
        '''List of User Verifications

        **PERMISSIONS: At least Active user is required.**   Returns a list of User Verifications starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see User Verifications for other users. Regular users will see their own User Verifications.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_verifications(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseUserVerification]
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_verifications_with_http_info(**kwargs)
        else:
            (data) = self.get_user_verifications_with_http_info(**kwargs)
            return data

    def get_user_verifications_with_http_info(self, **kwargs):
        '''List of User Verifications

        **PERMISSIONS: At least Active user is required.**   Returns a list of User Verifications starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see User Verifications for other users. Regular users will see their own User Verifications.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_verifications_with_http_info(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseUserVerification]
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
                                " to method get_user_verifications" % key)
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_user_verifications`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_user_verifications`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError(
                "Invalid value for parameter `offset` when calling `get_user_verifications`, must be a value greater than or equal to `0`")
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

        return self.api_client.call_api('/user_verifications/', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='list[BaseUserVerification]', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_get_user_verification_by_user_id(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_get_user_verification_by_user_id(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_get_user_verification_by_user_id_with_http_info(**kwargs)
        else:
            (data) = self.options_get_user_verification_by_user_id_with_http_info(**kwargs)
            return data

    def options_get_user_verification_by_user_id_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_get_user_verification_by_user_id_with_http_info(async_req=True)
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
                                " to method options_get_user_verification_by_user_id" % key)
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

        return self.api_client.call_api('/user_verifications/get_redditor', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_user_verification_by_id(self, user_verification_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_user_verification_by_id(user_verification_id, async_req=True)
        >>> result = thread.get()


        :param int user_verification_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_user_verification_by_id_with_http_info(user_verification_id, **kwargs)
        else:
            (data) = self.options_user_verification_by_id_with_http_info(user_verification_id, **kwargs)
            return data

    def options_user_verification_by_id_with_http_info(self, user_verification_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_user_verification_by_id_with_http_info(user_verification_id, async_req=True)
        >>> result = thread.get()


        :param int user_verification_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_verification_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_user_verification_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_verification_id' is set
        if ('user_verification_id' not in params or params['user_verification_id'] is None):
            raise ValueError("Missing the required parameter `user_verification_id` when calling `options_user_verification_by_id`")

        collection_formats = {}

        path_params = {}
        if 'user_verification_id' in params:
            path_params['user_verification_id'] = params['user_verification_id']

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

        return self.api_client.call_api('/user_verifications/{user_verification_id}', 'OPTIONS', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_user_verifications(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_user_verifications(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_user_verifications_with_http_info(**kwargs)
        else:
            (data) = self.options_user_verifications_with_http_info(**kwargs)
            return data

    def options_user_verifications_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_user_verifications_with_http_info(async_req=True)
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
                                " to method options_user_verifications" % key)
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

        return self.api_client.call_api('/user_verifications/', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def patch_user_verification_by_id(self, user_verification_id, body, **kwargs):
        '''Patch user_verification details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_user_verification_by_id(user_verification_id, body, async_req=True)
        >>> result = thread.get()


        :param int user_verification_id: (required)
        :param list[Body6] body: (required)
        :return: UserVerification
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_user_verification_by_id_with_http_info(user_verification_id, body, **kwargs)
        else:
            (data) = self.patch_user_verification_by_id_with_http_info(user_verification_id, body, **kwargs)
            return data

    def patch_user_verification_by_id_with_http_info(self, user_verification_id, body, **kwargs):
        '''Patch user_verification details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_user_verification_by_id_with_http_info(user_verification_id, body, async_req=True)
        >>> result = thread.get()


        :param int user_verification_id: (required)
        :param list[Body6] body: (required)
        :return: UserVerification
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_verification_id', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method patch_user_verification_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_verification_id' is set
        if ('user_verification_id' not in params or params['user_verification_id'] is None):
            raise ValueError("Missing the required parameter `user_verification_id` when calling `patch_user_verification_by_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_user_verification_by_id`")

        collection_formats = {}

        path_params = {}
        if 'user_verification_id' in params:
            path_params['user_verification_id'] = params['user_verification_id']

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

        return self.api_client.call_api('/user_verifications/{user_verification_id}', 'PATCH', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type='UserVerification', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_get_user_verification_by_user_id(self, user_id, **kwargs):
        '''Get User Verification by User ID

        **PERMISSIONS: At least Active user is required.**   Optionally filter by Reddit App ID  Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_get_user_verification_by_user_id(user_id, async_req=True)
        >>> result = thread.get()


        :param str user_id: User ID to associate Redditor with (required)
        :param int reddit_app_id: Optionally specify a Reddit app the User Verification belongs to
        :return: UserVerification
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_get_user_verification_by_user_id_with_http_info(user_id, **kwargs)
        else:
            (data) = self.post_get_user_verification_by_user_id_with_http_info(user_id, **kwargs)
            return data

    def post_get_user_verification_by_user_id_with_http_info(self, user_id, **kwargs):
        '''Get User Verification by User ID

        **PERMISSIONS: At least Active user is required.**   Optionally filter by Reddit App ID  Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_get_user_verification_by_user_id_with_http_info(user_id, async_req=True)
        >>> result = thread.get()


        :param str user_id: User ID to associate Redditor with (required)
        :param int reddit_app_id: Optionally specify a Reddit app the User Verification belongs to
        :return: UserVerification
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_id', 'reddit_app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_get_user_verification_by_user_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_get_user_verification_by_user_id`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'user_id' in params:
            form_params.append(('user_id', params['user_id']))
        if 'reddit_app_id' in params:
            form_params.append(('reddit_app_id', params['reddit_app_id']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/user_verifications/get_redditor', 'POST', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='UserVerification', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_user_verifications(self, user_id, reddit_app_id, **kwargs):
        '''Create a new User Verification

        **PERMISSIONS: At least Active user is required.**   User Verifications for verifying a redditor with a User ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_user_verifications(user_id, reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param str user_id: User ID to associate Redditor with (required)
        :param int reddit_app_id: Reddit app the User Verification is for (required)
        :param str redditor: Redditor the User Verification is for
        :param str extra_data: Extra JSON data to include with verification
        :param int owner_id: Owner of the verification. Requires Admin to create for other users.
        :return: UserVerification
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_user_verifications_with_http_info(user_id, reddit_app_id, **kwargs)
        else:
            (data) = self.post_user_verifications_with_http_info(user_id, reddit_app_id, **kwargs)
            return data

    def post_user_verifications_with_http_info(self, user_id, reddit_app_id, **kwargs):
        '''Create a new User Verification

        **PERMISSIONS: At least Active user is required.**   User Verifications for verifying a redditor with a User ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_user_verifications_with_http_info(user_id, reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param str user_id: User ID to associate Redditor with (required)
        :param int reddit_app_id: Reddit app the User Verification is for (required)
        :param str redditor: Redditor the User Verification is for
        :param str extra_data: Extra JSON data to include with verification
        :param int owner_id: Owner of the verification. Requires Admin to create for other users.
        :return: UserVerification
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['user_id', 'reddit_app_id', 'redditor', 'extra_data', 'owner_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_user_verifications" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_user_verifications`")
        # verify the required parameter 'reddit_app_id' is set
        if ('reddit_app_id' not in params or params['reddit_app_id'] is None):
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `post_user_verifications`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'user_id' in params:
            form_params.append(('user_id', params['user_id']))
        if 'redditor' in params:
            form_params.append(('redditor', params['redditor']))
        if 'reddit_app_id' in params:
            form_params.append(('reddit_app_id', params['reddit_app_id']))
        if 'extra_data' in params:
            form_params.append(('extra_data', params['extra_data']))
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

        return self.api_client.call_api('/user_verifications/', 'POST', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='UserVerification', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))