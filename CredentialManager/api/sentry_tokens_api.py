import re

# python 2 and python 3 compatibility library
from CredentialManager.api_client import ApiClient


class SentryTokensApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_sentry_token_by_id(self, sentry_token_id, **kwargs):
        '''Delete a Sentry Token by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sentry_token_by_id(sentry_token_id, async_req=True)
        >>> result = thread.get()


        :param int sentry_token_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sentry_token_by_id_with_http_info(sentry_token_id, **kwargs)
        else:
            (data) = self.delete_sentry_token_by_id_with_http_info(sentry_token_id, **kwargs)
            return data

    def delete_sentry_token_by_id_with_http_info(self, sentry_token_id, **kwargs):
        '''Delete a Sentry Token by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sentry_token_by_id_with_http_info(sentry_token_id, async_req=True)
        >>> result = thread.get()


        :param int sentry_token_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['sentry_token_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method delete_sentry_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sentry_token_id' is set
        if ('sentry_token_id' not in params or params['sentry_token_id'] is None):
            raise ValueError("Missing the required parameter `sentry_token_id` when calling `delete_sentry_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'sentry_token_id' in params:
            path_params['sentry_token_id'] = params['sentry_token_id']

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

        return self.api_client.call_api('/sentry_tokens/{sentry_token_id}', 'DELETE', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_sentry_token_by_id(self, sentry_token_id, **kwargs):
        '''Get Sentry Token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sentry_token_by_id(sentry_token_id, async_req=True)
        >>> result = thread.get()


        :param int sentry_token_id: (required)
        :return: SentryToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sentry_token_by_id_with_http_info(sentry_token_id, **kwargs)
        else:
            (data) = self.get_sentry_token_by_id_with_http_info(sentry_token_id, **kwargs)
            return data

    def get_sentry_token_by_id_with_http_info(self, sentry_token_id, **kwargs):
        '''Get Sentry Token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sentry_token_by_id_with_http_info(sentry_token_id, async_req=True)
        >>> result = thread.get()


        :param int sentry_token_id: (required)
        :return: SentryToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['sentry_token_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_sentry_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sentry_token_id' is set
        if ('sentry_token_id' not in params or params['sentry_token_id'] is None):
            raise ValueError("Missing the required parameter `sentry_token_id` when calling `get_sentry_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'sentry_token_id' in params:
            path_params['sentry_token_id'] = params['sentry_token_id']

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

        return self.api_client.call_api('/sentry_tokens/{sentry_token_id}', 'GET', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='SentryToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_sentry_tokens(self, **kwargs):
        '''List of Sentry Tokens

        **PERMISSIONS: At least Active user is required.**   Returns a list of Sentry Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Sentry Tokens for other users. Regular users will see their own Sentry Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sentry_tokens(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseSentryToken]
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sentry_tokens_with_http_info(**kwargs)
        else:
            (data) = self.get_sentry_tokens_with_http_info(**kwargs)
            return data

    def get_sentry_tokens_with_http_info(self, **kwargs):
        '''List of Sentry Tokens

        **PERMISSIONS: At least Active user is required.**   Returns a list of Sentry Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Sentry Tokens for other users. Regular users will see their own Sentry Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sentry_tokens_with_http_info(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseSentryToken]
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
                                " to method get_sentry_tokens" % key)
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_sentry_tokens`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_sentry_tokens`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError(
                "Invalid value for parameter `offset` when calling `get_sentry_tokens`, must be a value greater than or equal to `0`")
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

        return self.api_client.call_api('/sentry_tokens/', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='list[BaseSentryToken]', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_sentry_token_by_id(self, sentry_token_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_sentry_token_by_id(sentry_token_id, async_req=True)
        >>> result = thread.get()


        :param int sentry_token_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_sentry_token_by_id_with_http_info(sentry_token_id, **kwargs)
        else:
            (data) = self.options_sentry_token_by_id_with_http_info(sentry_token_id, **kwargs)
            return data

    def options_sentry_token_by_id_with_http_info(self, sentry_token_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_sentry_token_by_id_with_http_info(sentry_token_id, async_req=True)
        >>> result = thread.get()


        :param int sentry_token_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['sentry_token_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_sentry_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sentry_token_id' is set
        if ('sentry_token_id' not in params or params['sentry_token_id'] is None):
            raise ValueError("Missing the required parameter `sentry_token_id` when calling `options_sentry_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'sentry_token_id' in params:
            path_params['sentry_token_id'] = params['sentry_token_id']

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

        return self.api_client.call_api('/sentry_tokens/{sentry_token_id}', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_sentry_tokens(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_sentry_tokens(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_sentry_tokens_with_http_info(**kwargs)
        else:
            (data) = self.options_sentry_tokens_with_http_info(**kwargs)
            return data

    def options_sentry_tokens_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_sentry_tokens_with_http_info(async_req=True)
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
                                " to method options_sentry_tokens" % key)
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

        return self.api_client.call_api('/sentry_tokens/', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def patch_sentry_token_by_id(self, sentry_token_id, body, **kwargs):
        '''Patch sentry_token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_sentry_token_by_id(sentry_token_id, body, async_req=True)
        >>> result = thread.get()


        :param int sentry_token_id: (required)
        :param list[Body5] body: (required)
        :return: SentryToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_sentry_token_by_id_with_http_info(sentry_token_id, body, **kwargs)
        else:
            (data) = self.patch_sentry_token_by_id_with_http_info(sentry_token_id, body, **kwargs)
            return data

    def patch_sentry_token_by_id_with_http_info(self, sentry_token_id, body, **kwargs):
        '''Patch sentry_token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_sentry_token_by_id_with_http_info(sentry_token_id, body, async_req=True)
        >>> result = thread.get()


        :param int sentry_token_id: (required)
        :param list[Body5] body: (required)
        :return: SentryToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['sentry_token_id', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method patch_sentry_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sentry_token_id' is set
        if ('sentry_token_id' not in params or params['sentry_token_id'] is None):
            raise ValueError("Missing the required parameter `sentry_token_id` when calling `patch_sentry_token_by_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_sentry_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'sentry_token_id' in params:
            path_params['sentry_token_id'] = params['sentry_token_id']

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

        return self.api_client.call_api('/sentry_tokens/{sentry_token_id}', 'PATCH', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='SentryToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_sentry_tokens(self, app_name, dsn, **kwargs):
        '''Create a new Sentry Token

        **PERMISSIONS: At least Active user is required.**   Sentry Tokens are used for logging and error reporting in applications
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_sentry_tokens(app_name, dsn, async_req=True)
        >>> result = thread.get()


        :param str app_name: Name of the Sentry Token (required)
        :param str dsn: DSN of the Sentry Token (required)
        :param bool enabled:
        :param int owner_id: Owner of the token. Requires Admin to create for other users.
        :return: SentryToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_sentry_tokens_with_http_info(app_name, dsn, **kwargs)
        else:
            (data) = self.post_sentry_tokens_with_http_info(app_name, dsn, **kwargs)
            return data

    def post_sentry_tokens_with_http_info(self, app_name, dsn, **kwargs):
        '''Create a new Sentry Token

        **PERMISSIONS: At least Active user is required.**   Sentry Tokens are used for logging and error reporting in applications
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_sentry_tokens_with_http_info(app_name, dsn, async_req=True)
        >>> result = thread.get()


        :param str app_name: Name of the Sentry Token (required)
        :param str dsn: DSN of the Sentry Token (required)
        :param bool enabled:
        :param int owner_id: Owner of the token. Requires Admin to create for other users.
        :return: SentryToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['app_name', 'dsn', 'enabled', 'owner_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_sentry_tokens" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `post_sentry_tokens`")
        # verify the required parameter 'dsn' is set
        if ('dsn' not in params or params['dsn'] is None):
            raise ValueError("Missing the required parameter `dsn` when calling `post_sentry_tokens`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'app_name' in params:
            form_params.append(('app_name', params['app_name']))
        if 'dsn' in params:
            form_params.append(('dsn', params['dsn']))
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

        return self.api_client.call_api('/sentry_tokens/', 'POST', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='SentryToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))