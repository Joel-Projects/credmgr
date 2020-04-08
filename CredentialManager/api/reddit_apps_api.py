import re

# python 2 and python 3 compatibility library
from CredentialManager.api_client import ApiClient


class RedditAppsApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_reddit_app_by_id(self, reddit_app_id, **kwargs):
        '''Delete a Reddit App by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_reddit_app_by_id(reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_reddit_app_by_id_with_http_info(reddit_app_id, **kwargs)
        else:
            (data) = self.delete_reddit_app_by_id_with_http_info(reddit_app_id, **kwargs)
            return data

    def delete_reddit_app_by_id_with_http_info(self, reddit_app_id, **kwargs):
        '''Delete a Reddit App by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_reddit_app_by_id_with_http_info(reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['reddit_app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method delete_reddit_app_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reddit_app_id' is set
        if 'reddit_app_id' not in params or params['reddit_app_id'] is None:
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `delete_reddit_app_by_id`")

        collection_formats = {}

        path_params = {}
        if 'reddit_app_id' in params:
            path_params['reddit_app_id'] = params['reddit_app_id']

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

        return self.api_client.call_api('/reddit_apps/{reddit_app_id}', 'DELETE', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_reddit_app_by_id(self, reddit_app_id, **kwargs):
        '''Get Reddit App details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reddit_app_by_id(reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :return: RedditApp
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_reddit_app_by_id_with_http_info(reddit_app_id, **kwargs)
        else:
            (data) = self.get_reddit_app_by_id_with_http_info(reddit_app_id, **kwargs)
            return data

    def get_reddit_app_by_id_with_http_info(self, reddit_app_id, **kwargs):
        '''Get Reddit App details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reddit_app_by_id_with_http_info(reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :return: RedditApp
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['reddit_app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_reddit_app_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reddit_app_id' is set
        if 'reddit_app_id' not in params or params['reddit_app_id'] is None:
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `get_reddit_app_by_id`")

        collection_formats = {}

        path_params = {}
        if 'reddit_app_id' in params:
            path_params['reddit_app_id'] = params['reddit_app_id']

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

        return self.api_client.call_api('/reddit_apps/{reddit_app_id}', 'GET', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='RedditApp', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_reddit_apps(self, **kwargs):
        '''List of Reddit Apps

        **PERMISSIONS: At least Active user is required.**   Returns a list of Reddit Apps starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Reddit Apps for other users. Regular users will see their own Reddit Apps.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reddit_apps(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseRedditApp]
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_reddit_apps_with_http_info(**kwargs)
        else:
            (data) = self.get_reddit_apps_with_http_info(**kwargs)
            return data

    def get_reddit_apps_with_http_info(self, **kwargs):
        '''List of Reddit Apps

        **PERMISSIONS: At least Active user is required.**   Returns a list of Reddit Apps starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Reddit Apps for other users. Regular users will see their own Reddit Apps.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reddit_apps_with_http_info(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseRedditApp]
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
                                " to method get_reddit_apps" % key)
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_reddit_apps`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_reddit_apps`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError(
                "Invalid value for parameter `offset` when calling `get_reddit_apps`, must be a value greater than or equal to `0`")
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

        return self.api_client.call_api('/reddit_apps/', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='list[BaseRedditApp]', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_generate_auth_url(self, reddit_app_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_generate_auth_url(reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_generate_auth_url_with_http_info(reddit_app_id, **kwargs)
        else:
            (data) = self.options_generate_auth_url_with_http_info(reddit_app_id, **kwargs)
            return data

    def options_generate_auth_url_with_http_info(self, reddit_app_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_generate_auth_url_with_http_info(reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['reddit_app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_generate_auth_url" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reddit_app_id' is set
        if 'reddit_app_id' not in params or params['reddit_app_id'] is None:
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `options_generate_auth_url`")

        collection_formats = {}

        path_params = {}
        if 'reddit_app_id' in params:
            path_params['reddit_app_id'] = params['reddit_app_id']

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

        return self.api_client.call_api('/reddit_apps/{reddit_app_id}/generate_auth', 'OPTIONS', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_reddit_app_by_id(self, reddit_app_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_reddit_app_by_id(reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_reddit_app_by_id_with_http_info(reddit_app_id, **kwargs)
        else:
            (data) = self.options_reddit_app_by_id_with_http_info(reddit_app_id, **kwargs)
            return data

    def options_reddit_app_by_id_with_http_info(self, reddit_app_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_reddit_app_by_id_with_http_info(reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['reddit_app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_reddit_app_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reddit_app_id' is set
        if 'reddit_app_id' not in params or params['reddit_app_id'] is None:
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `options_reddit_app_by_id`")

        collection_formats = {}

        path_params = {}
        if 'reddit_app_id' in params:
            path_params['reddit_app_id'] = params['reddit_app_id']

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

        return self.api_client.call_api('/reddit_apps/{reddit_app_id}', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_reddit_apps(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_reddit_apps(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_reddit_apps_with_http_info(**kwargs)
        else:
            (data) = self.options_reddit_apps_with_http_info(**kwargs)
            return data

    def options_reddit_apps_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_reddit_apps_with_http_info(async_req=True)
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
                                " to method options_reddit_apps" % key)
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

        return self.api_client.call_api('/reddit_apps/', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def patch_reddit_app_by_id(self, reddit_app_id, body, **kwargs):
        '''Patch reddit_app details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_reddit_app_by_id(reddit_app_id, body, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :param list[Body3] body: (required)
        :return: RedditApp
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_reddit_app_by_id_with_http_info(reddit_app_id, body, **kwargs)
        else:
            (data) = self.patch_reddit_app_by_id_with_http_info(reddit_app_id, body, **kwargs)
            return data

    def patch_reddit_app_by_id_with_http_info(self, reddit_app_id, body, **kwargs):
        '''Patch reddit_app details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_reddit_app_by_id_with_http_info(reddit_app_id, body, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :param list[Body3] body: (required)
        :return: RedditApp
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['reddit_app_id', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method patch_reddit_app_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reddit_app_id' is set
        if 'reddit_app_id' not in params or params['reddit_app_id'] is None:
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `patch_reddit_app_by_id`")
        # verify the required parameter 'body' is set
        if 'body' not in params or params['body'] is None:
            raise ValueError("Missing the required parameter `body` when calling `patch_reddit_app_by_id`")

        collection_formats = {}

        path_params = {}
        if 'reddit_app_id' in params:
            path_params['reddit_app_id'] = params['reddit_app_id']

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

        return self.api_client.call_api('/reddit_apps/{reddit_app_id}', 'PATCH', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='RedditApp', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_generate_auth_url(self, reddit_app_id, scopes, **kwargs):
        '''Generate a reddit auth url

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_generate_auth_url(reddit_app_id, scopes, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :param list[str] scopes: List of scopes needed for app (required)
        :param str duration: Duration authorization is good for. Options are: `permanent` and `temporary`. Defaults to `permanent`.
        :param str user_verification_user_id: Specify a User Verification User ID to assoiate with auth url by User ID
        :param int user_verification_id: Specify a User Verification ID to assoiate with auth url by User Verification ID
        :return: AuthUrl
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_generate_auth_url_with_http_info(reddit_app_id, scopes, **kwargs)
        else:
            (data) = self.post_generate_auth_url_with_http_info(reddit_app_id, scopes, **kwargs)
            return data

    def post_generate_auth_url_with_http_info(self, reddit_app_id, scopes, **kwargs):
        '''Generate a reddit auth url

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_generate_auth_url_with_http_info(reddit_app_id, scopes, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :param list[str] scopes: List of scopes needed for app (required)
        :param str duration: Duration authorization is good for. Options are: `permanent` and `temporary`. Defaults to `permanent`.
        :param str user_verification_user_id: Specify a User Verification User ID to assoiate with auth url by User ID
        :param int user_verification_id: Specify a User Verification ID to assoiate with auth url by User Verification ID
        :return: AuthUrl
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['reddit_app_id', 'scopes', 'duration', 'user_verification_user_id', 'user_verification_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_generate_auth_url" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reddit_app_id' is set
        if 'reddit_app_id' not in params or params['reddit_app_id'] is None:
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `post_generate_auth_url`")
        # verify the required parameter 'scopes' is set
        if 'scopes' not in params or params['scopes'] is None:
            raise ValueError("Missing the required parameter `scopes` when calling `post_generate_auth_url`")

        collection_formats = {}

        path_params = {}
        if 'reddit_app_id' in params:
            path_params['reddit_app_id'] = params['reddit_app_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'duration' in params:
            form_params.append(('duration', params['duration']))
        if 'scopes' in params:
            form_params.append(('scopes', params['scopes']))
            collection_formats['scopes'] = 'multi'
        if 'user_verification_user_id' in params:
            form_params.append(('user_verification_user_id', params['user_verification_user_id']))
        if 'user_verification_id' in params:
            form_params.append(('user_verification_id', params['user_verification_id']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/reddit_apps/{reddit_app_id}/generate_auth', 'POST', path_params, query_params, header_params,
                                        body=body_params, params=form_params, response_type='AuthUrl', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_reddit_app_by_id(self, reddit_app_id, redditor, **kwargs):
        '''Get Refresh Token by reddit app and redditor

        **PERMISSIONS: Owner/Admin may execute this action.**   Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_reddit_app_by_id(reddit_app_id, redditor, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :param str redditor: Redditor the Refresh Token is for (required)
        :return: RefreshToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_reddit_app_by_id_with_http_info(reddit_app_id, redditor, **kwargs)
        else:
            (data) = self.post_reddit_app_by_id_with_http_info(reddit_app_id, redditor, **kwargs)
            return data

    def post_reddit_app_by_id_with_http_info(self, reddit_app_id, redditor, **kwargs):
        '''Get Refresh Token by reddit app and redditor

        **PERMISSIONS: Owner/Admin may execute this action.**   Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_reddit_app_by_id_with_http_info(reddit_app_id, redditor, async_req=True)
        >>> result = thread.get()


        :param int reddit_app_id: (required)
        :param str redditor: Redditor the Refresh Token is for (required)
        :return: RefreshToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['reddit_app_id', 'redditor']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_reddit_app_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reddit_app_id' is set
        if 'reddit_app_id' not in params or params['reddit_app_id'] is None:
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `post_reddit_app_by_id`")
        # verify the required parameter 'redditor' is set
        if 'redditor' not in params or params['redditor'] is None:
            raise ValueError("Missing the required parameter `redditor` when calling `post_reddit_app_by_id`")

        collection_formats = {}

        path_params = {}
        if 'reddit_app_id' in params:
            path_params['reddit_app_id'] = params['reddit_app_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'redditor' in params:
            form_params.append(('redditor', params['redditor']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/reddit_apps/{reddit_app_id}', 'POST', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='RefreshToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_reddit_apps(self, app_name, client_id, user_agent, app_type, redirect_uri, **kwargs):
        '''Create a new Reddit App

        **PERMISSIONS: At least Active user is required.**   Reddit Apps are used for interacting with reddit
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_reddit_apps(app_name, client_id, user_agent, app_type, redirect_uri, async_req=True)
        >>> result = thread.get()


        :param str app_name: (required)
        :param str client_id: Client ID of the Reddit App (required)
        :param str user_agent: User agent used for requests to Reddit's API (required)
        :param str app_type: Type of the app. One of `web`, `installed`, or `script` (required)
        :param str redirect_uri: Redirect URI for Oauth2 flow. Defaults to user set redirect uri (required)
        :param str client_secret: Client secret of the Reddit App
        :param str short_name: Short name of the Reddit App
        :param str app_description: Description of the Reddit App
        :param str state:
        :param bool enabled: Allows the app to be used
        :param int owner_id: Owner of the app. Requires Admin to create for other users.
        :return: RedditApp
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_reddit_apps_with_http_info(app_name, client_id, user_agent, app_type, redirect_uri, **kwargs)
        else:
            (data) = self.post_reddit_apps_with_http_info(app_name, client_id, user_agent, app_type, redirect_uri, **kwargs)
            return data

    def post_reddit_apps_with_http_info(self, app_name, client_id, user_agent, app_type, redirect_uri, **kwargs):
        '''Create a new Reddit App

        **PERMISSIONS: At least Active user is required.**   Reddit Apps are used for interacting with reddit
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_reddit_apps_with_http_info(app_name, client_id, user_agent, app_type, redirect_uri, async_req=True)
        >>> result = thread.get()


        :param str app_name: (required)
        :param str client_id: Client ID of the Reddit App (required)
        :param str user_agent: User agent used for requests to Reddit's API (required)
        :param str app_type: Type of the app. One of `web`, `installed`, or `script` (required)
        :param str redirect_uri: Redirect URI for Oauth2 flow. Defaults to user set redirect uri (required)
        :param str client_secret: Client secret of the Reddit App
        :param str short_name: Short name of the Reddit App
        :param str app_description: Description of the Reddit App
        :param str state:
        :param bool enabled: Allows the app to be used
        :param int owner_id: Owner of the app. Requires Admin to create for other users.
        :return: RedditApp
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['app_name', 'client_id', 'user_agent', 'app_type', 'redirect_uri', 'client_secret', 'short_name', 'app_description', 'state',
                      'enabled', 'owner_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_reddit_apps" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_name' is set
        if 'app_name' not in params or params['app_name'] is None:
            raise ValueError("Missing the required parameter `app_name` when calling `post_reddit_apps`")
        # verify the required parameter 'client_id' is set
        if 'client_id' not in params or params['client_id'] is None:
            raise ValueError("Missing the required parameter `client_id` when calling `post_reddit_apps`")
        # verify the required parameter 'user_agent' is set
        if 'user_agent' not in params or params['user_agent'] is None:
            raise ValueError("Missing the required parameter `user_agent` when calling `post_reddit_apps`")
        # verify the required parameter 'app_type' is set
        if 'app_type' not in params or params['app_type'] is None:
            raise ValueError("Missing the required parameter `app_type` when calling `post_reddit_apps`")
        # verify the required parameter 'redirect_uri' is set
        if 'redirect_uri' not in params or params['redirect_uri'] is None:
            raise ValueError("Missing the required parameter `redirect_uri` when calling `post_reddit_apps`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'app_name' in params:
            form_params.append(('app_name', params['app_name']))
        if 'client_id' in params:
            form_params.append(('client_id', params['client_id']))
        if 'client_secret' in params:
            form_params.append(('client_secret', params['client_secret']))
        if 'short_name' in params:
            form_params.append(('short_name', params['short_name']))
        if 'app_description' in params:
            form_params.append(('app_description', params['app_description']))
        if 'user_agent' in params:
            form_params.append(('user_agent', params['user_agent']))
        if 'app_type' in params:
            form_params.append(('app_type', params['app_type']))
        if 'redirect_uri' in params:
            form_params.append(('redirect_uri', params['redirect_uri']))
        if 'state' in params:
            form_params.append(('state', params['state']))
        if 'enabled' in params:
            form_params.append(('enabled', params['enabled']))
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

        return self.api_client.call_api('/reddit_apps/', 'POST', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='RedditApp', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))