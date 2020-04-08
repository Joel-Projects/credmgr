# python 2 and python 3 compatibility library
from CredentialManager.api_client import ApiClient


class APIBase(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete(self, item_id, **kwargs):
        '''Delete an item by ID

        **PERMISSIONS: Owner/Admin may execute this action.**

        :param int item_id: (required)
        :return: None
        '''
        return self.delete_with_http_info(item_id, **kwargs)

    def delete_with_http_info(self, item_id, **kwargs):
        '''Delete a API Token by ID

        **PERMISSIONS: Owner/Admin may execute this action.**

        :param int item_id: (required)
        :return: None
                 If the method is called asynchronously, returns the request thread.
        '''

        all_params = ['item_id']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs']:
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method delete")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if 'item_id' not in params or params['item_id'] is None:
            raise ValueError("Missing the required parameter `item_id` when calling `delete`")

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['item_id'] = params['item_id']

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

        return self.api_client.call_api('/{api_tokens}/{item_id}', 'DELETE', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_by_id(self, item_id, **kwargs):
        '''Get API Token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**

        :param int item_id: (required)
        :return: ApiToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_by_id_with_http_info(item_id, **kwargs)
        else:
            (data) = self.get_by_id_with_http_info(item_id, **kwargs)
            return data

    def get_by_id_with_http_info(self, item_id, **kwargs):
        '''Get API Token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(item_id, async_req=True)
        >>> result = thread.get()


        :param int item_id: (required)
        :return: ApiToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['item_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if 'item_id' not in params or params['item_id'] is None:
            raise ValueError("Missing the required parameter `item_id` when calling `get_by_id`")

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['item_id'] = params['item_id']

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

        return self.api_client.call_api('/api_tokens/{item_id}', 'GET', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='ApiToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_api_tokens(self, **kwargs):
        '''List of API Tokens

        **PERMISSIONS: At least Active user is required.**   Returns a list of API Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see API Tokens for other users. Regular users will see their own API Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_tokens(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseApiToken]
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_tokens_with_http_info(**kwargs)
        else:
            (data) = self.get_api_tokens_with_http_info(**kwargs)
            return data

    def get_api_tokens_with_http_info(self, **kwargs):
        '''List of API Tokens

        **PERMISSIONS: At least Active user is required.**   Returns a list of API Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see API Tokens for other users. Regular users will see their own API Tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_tokens_with_http_info(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseApiToken]
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
                                " to method get_api_tokens" % key)
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError("Invalid value for parameter `limit` when calling `get_api_tokens`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `get_api_tokens`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `get_api_tokens`, must be a value greater than or equal to `0`")
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
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/api_tokens/', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='list[BaseApiToken]', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_api_token_by_id(self, item_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_api_token_by_id(item_id, async_req=True)
        >>> result = thread.get()


        :param int item_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_api_token_by_id_with_http_info(item_id, **kwargs)
        else:
            (data) = self.options_api_token_by_id_with_http_info(item_id, **kwargs)
            return data

    def options_api_token_by_id_with_http_info(self, item_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_api_token_by_id_with_http_info(item_id, async_req=True)
        >>> result = thread.get()


        :param int item_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['item_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_api_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if 'item_id' not in params or params['item_id'] is None:
            raise ValueError("Missing the required parameter `item_id` when calling `options_api_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['item_id'] = params['item_id']

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

        return self.api_client.call_api('/api_tokens/{item_id}', 'OPTIONS', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_api_tokens(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_api_tokens(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_api_tokens_with_http_info(**kwargs)
        else:
            (data) = self.options_api_tokens_with_http_info(**kwargs)
            return data

    def options_api_tokens_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_api_tokens_with_http_info(async_req=True)
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
                                " to method options_api_tokens" % key)
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

        return self.api_client.call_api('/api_tokens/', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def patch_api_token_by_id(self, item_id, body, **kwargs):
        '''Patch api_token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_api_token_by_id(item_id, body, async_req=True)
        >>> result = thread.get()


        :param int item_id: (required)
        :param list[Body] body: (required)
        :return: ApiToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_api_token_by_id_with_http_info(item_id, body, **kwargs)
        else:
            (data) = self.patch_api_token_by_id_with_http_info(item_id, body, **kwargs)
            return data

    def patch_api_token_by_id_with_http_info(self, item_id, body, **kwargs):
        '''Patch api_token details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_api_token_by_id_with_http_info(item_id, body, async_req=True)
        >>> result = thread.get()


        :param int item_id: (required)
        :param list[Body] body: (required)
        :return: ApiToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['item_id', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method patch_api_token_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if 'item_id' not in params or params['item_id'] is None:
            raise ValueError("Missing the required parameter `item_id` when calling `patch_api_token_by_id`")
        # verify the required parameter 'body' is set
        if 'body' not in params or params['body'] is None:
            raise ValueError("Missing the required parameter `body` when calling `patch_api_token_by_id`")

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['item_id'] = params['item_id']

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

        return self.api_client.call_api('/api_tokens/{item_id}', 'PATCH', path_params, query_params, header_params, body=body_params,
                                        params=form_params, response_type='ApiToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_api_tokens(self, name, **kwargs):
        '''Create a new API Token

        **PERMISSIONS: At least Active user is required.**   API token can be used instead of username/password. Include the API token in the ``X-API-KEY`` header
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_api_tokens(name, async_req=True)
        >>> result = thread.get()


        :param str name: Name of the API token (required)
        :param int owner_id: Owner of the token. Requires Admin to create for other users.
        :param int length: Length of the token. Must be between 16 and 128, `16<=length<=128`. Defaults to `32`
        :return: ApiToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_api_tokens_with_http_info(name, **kwargs)
        else:
            (data) = self.post_api_tokens_with_http_info(name, **kwargs)
            return data

    def post_api_tokens_with_http_info(self, name, **kwargs):
        '''Create a new API Token

        **PERMISSIONS: At least Active user is required.**   API token can be used instead of username/password. Include the API token in the ``X-API-KEY`` header
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_api_tokens_with_http_info(name, async_req=True)
        >>> result = thread.get()


        :param str name: Name of the API token (required)
        :param int owner_id: Owner of the token. Requires Admin to create for other users.
        :param int length: Length of the token. Must be between 16 and 128, `16<=length<=128`. Defaults to `32`
        :return: ApiToken
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['name', 'owner_id', 'length']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_api_tokens" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if 'name' not in params or params['name'] is None:
            raise ValueError("Missing the required parameter `name` when calling `post_api_tokens`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'owner_id' in params:
            form_params.append(('owner_id', params['owner_id']))
        if 'length' in params:
            form_params.append(('length', params['length']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/x-www-form-urlencoded', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/api_tokens/', 'POST', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='ApiToken', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))