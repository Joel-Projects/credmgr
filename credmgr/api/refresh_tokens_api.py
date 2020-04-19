# python 2 and python 3 compatibility library
from credmgr.api_client import ApiClient


class RefreshTokensApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_refresh_token_by_id(self, refresh_token_id, **kwargs):
        '''Delete a Refresh Token by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_refresh_token_by_id(refresh_token_id, async_req=True)
        >>> result = thread.get()


        :param int refresh_token_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_refresh_token_by_id_with_http_info(refresh_token_id, **kwargs)
        else:
            (data) = self.delete_refresh_token_by_id_with_http_info(refresh_token_id, **kwargs)
            return data

    def delete_refresh_token_by_id_with_http_info(self, refresh_token_id, **kwargs):
        '''Delete a Refresh Token by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_refresh_token_by_id_with_http_info(refresh_token_id, async_req=True)
        >>> result = thread.get()


        :param int refresh_token_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['refresh_token_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method delete_refresh_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'refresh_token_id' is set
        if ('refresh_token_id' not in params or params['refresh_token_id'] is None):
            raise ValueError("Missing the required parameter `refresh_token_id` when calling `delete_refresh_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'refresh_token_id' in params:
            path_params['refresh_token_id'] = params['refresh_token_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/refresh_tokens/{refresh_token_id}', 'DELETE', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_refresh_token_by_id(self, refresh_token_id, **kwargs):
        '''Get Refresh Token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_token_by_id(refresh_token_id, async_req=True)
        >>> result = thread.get()


        :param int refresh_token_id: (required)
        :return: RefreshToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_refresh_token_by_id_with_http_info(refresh_token_id, **kwargs)
        else:
            (data) = self.get_refresh_token_by_id_with_http_info(refresh_token_id, **kwargs)
            return data

    def get_refresh_token_by_id_with_http_info(self, refresh_token_id, **kwargs):
        '''Get Refresh Token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_token_by_id_with_http_info(refresh_token_id, async_req=True)
        >>> result = thread.get()


        :param int refresh_token_id: (required)
        :return: RefreshToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['refresh_token_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_refresh_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'refresh_token_id' is set
        if ('refresh_token_id' not in params or params['refresh_token_id'] is None):
            raise ValueError("Missing the required parameter `refresh_token_id` when calling `get_refresh_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'refresh_token_id' in params:
            path_params['refresh_token_id'] = params['refresh_token_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/refresh_tokens/{refresh_token_id}', 'GET', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='RefreshToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_refresh_tokens(self, **kwargs):
        '''List of Refresh Tokens

        **PERMISSIONS: At least Active user is required.**   Returns a list of Refresh Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner_id`` to see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_tokens(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param str redditor:
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseRefreshToken]
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_refresh_tokens_with_http_info(**kwargs)
        else:
            (data) = self.get_refresh_tokens_with_http_info(**kwargs)
            return data

    def get_refresh_tokens_with_http_info(self, **kwargs):
        '''List of Refresh Tokens

        **PERMISSIONS: At least Active user is required.**   Returns a list of Refresh Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner_id`` to see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_tokens_with_http_info(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param str redditor:
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseRefreshToken]
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['limit', 'redditor', 'offset', 'owner_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_refresh_tokens" % key)
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError("Invalid value for parameter `limit` when calling `get_refresh_tokens`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `get_refresh_tokens`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `get_refresh_tokens`, must be a value greater than or equal to `0`")
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'redditor' in params:
            query_params.append(('redditor', params['redditor']))
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
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/refresh_tokens/', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='list[BaseRefreshToken]', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_get_refresh_token_by_redditor(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_get_refresh_token_by_redditor(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_get_refresh_token_by_redditor_with_http_info(**kwargs)
        else:
            (data) = self.options_get_refresh_token_by_redditor_with_http_info(**kwargs)
            return data

    def options_get_refresh_token_by_redditor_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_get_refresh_token_by_redditor_with_http_info(async_req=True)
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
                                " to method options_get_refresh_token_by_redditor" % key)
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
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/refresh_tokens/by_redditor', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_refresh_token_by_id(self, refresh_token_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_refresh_token_by_id(refresh_token_id, async_req=True)
        >>> result = thread.get()


        :param int refresh_token_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_refresh_token_by_id_with_http_info(refresh_token_id, **kwargs)
        else:
            (data) = self.options_refresh_token_by_id_with_http_info(refresh_token_id, **kwargs)
            return data

    def options_refresh_token_by_id_with_http_info(self, refresh_token_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_refresh_token_by_id_with_http_info(refresh_token_id, async_req=True)
        >>> result = thread.get()


        :param int refresh_token_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['refresh_token_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_refresh_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'refresh_token_id' is set
        if ('refresh_token_id' not in params or params['refresh_token_id'] is None):
            raise ValueError("Missing the required parameter `refresh_token_id` when calling `options_refresh_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'refresh_token_id' in params:
            path_params['refresh_token_id'] = params['refresh_token_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/refresh_tokens/{refresh_token_id}', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_refresh_tokens(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_refresh_tokens(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_refresh_tokens_with_http_info(**kwargs)
        else:
            (data) = self.options_refresh_tokens_with_http_info(**kwargs)
            return data

    def options_refresh_tokens_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_refresh_tokens_with_http_info(async_req=True)
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
                                " to method options_refresh_tokens" % key)
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
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/refresh_tokens/', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def patch_refresh_token_by_id(self, refresh_token_id, body, **kwargs):
        '''Patch refresh_token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_refresh_token_by_id(refresh_token_id, body, async_req=True)
        >>> result = thread.get()


        :param int refresh_token_id: (required)
        :param list[Body4] body: (required)
        :return: RefreshToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_refresh_token_by_id_with_http_info(refresh_token_id, body, **kwargs)
        else:
            (data) = self.patch_refresh_token_by_id_with_http_info(refresh_token_id, body, **kwargs)
            return data

    def patch_refresh_token_by_id_with_http_info(self, refresh_token_id, body, **kwargs):
        '''Patch refresh_token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_refresh_token_by_id_with_http_info(refresh_token_id, body, async_req=True)
        >>> result = thread.get()


        :param int refresh_token_id: (required)
        :param list[Body4] body: (required)
        :return: RefreshToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['refresh_token_id', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method patch_refresh_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'refresh_token_id' is set
        if ('refresh_token_id' not in params or params['refresh_token_id'] is None):
            raise ValueError("Missing the required parameter `refresh_token_id` when calling `patch_refresh_token_by_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_refresh_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'refresh_token_id' in params:
            path_params['refresh_token_id'] = params['refresh_token_id']

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
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/refresh_tokens/{refresh_token_id}', 'PATCH', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='RefreshToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_get_refresh_token_by_redditor(self, redditor, reddit_app_id, **kwargs):
        '''Get Refresh Token by reddit app and redditor

        **PERMISSIONS: At least Active user is required.**   Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_get_refresh_token_by_redditor(redditor, reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param str redditor: Redditor the Refresh Token is for (required)
        :param int reddit_app_id: Reddit app the Refresh Token is for (required)
        :return: RefreshToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_get_refresh_token_by_redditor_with_http_info(redditor, reddit_app_id, **kwargs)
        else:
            (data) = self.post_get_refresh_token_by_redditor_with_http_info(redditor, reddit_app_id, **kwargs)
            return data

    def post_get_refresh_token_by_redditor_with_http_info(self, redditor, reddit_app_id, **kwargs):
        '''Get Refresh Token by reddit app and redditor

        **PERMISSIONS: At least Active user is required.**   Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_get_refresh_token_by_redditor_with_http_info(redditor, reddit_app_id, async_req=True)
        >>> result = thread.get()


        :param str redditor: Redditor the Refresh Token is for (required)
        :param int reddit_app_id: Reddit app the Refresh Token is for (required)
        :return: RefreshToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['redditor', 'reddit_app_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_get_refresh_token_by_redditor" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'redditor' is set
        if ('redditor' not in params or params['redditor'] is None):
            raise ValueError("Missing the required parameter `redditor` when calling `post_get_refresh_token_by_redditor`")
        # verify the required parameter 'reddit_app_id' is set
        if ('reddit_app_id' not in params or params['reddit_app_id'] is None):
            raise ValueError("Missing the required parameter `reddit_app_id` when calling `post_get_refresh_token_by_redditor`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'redditor' in params:
            form_params.append(('redditor', params['redditor']))
        if 'reddit_app_id' in params:
            form_params.append(('reddit_app_id', params['reddit_app_id']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/x-www-form-urlencoded', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/refresh_tokens/by_redditor', 'POST', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='RefreshToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))