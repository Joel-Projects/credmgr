import re

# python 2 and python 3 compatibility library
from CredentialManager.api_client import ApiClient


class BotsApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_bot_by_id(self, bot_id, **kwargs):
        '''Delete a Bot by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bot_by_id(bot_id, async_req=True)
        >>> result = thread.get()


        :param int bot_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bot_by_id_with_http_info(bot_id, **kwargs)
        else:
            (data) = self.delete_bot_by_id_with_http_info(bot_id, **kwargs)
            return data

    def delete_bot_by_id_with_http_info(self, bot_id, **kwargs):
        '''Delete a Bot by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bot_by_id_with_http_info(bot_id, async_req=True)
        >>> result = thread.get()


        :param int bot_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['bot_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method delete_bot_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bot_id' is set
        if 'bot_id' not in params or params['bot_id'] is None:
            raise ValueError("Missing the required parameter `bot_id` when calling `delete_bot_by_id`")

        collection_formats = {}

        path_params = {}
        if 'bot_id' in params:
            path_params['bot_id'] = params['bot_id']

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

        return self.api_client.call_api('/bots/{bot_id}', 'DELETE', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_bot_by_id(self, bot_id, **kwargs):
        '''Get Bot details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bot_by_id(bot_id, async_req=True)
        >>> result = thread.get()


        :param int bot_id: (required)
        :return: Bot
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bot_by_id_with_http_info(bot_id, **kwargs)
        else:
            (data) = self.get_bot_by_id_with_http_info(bot_id, **kwargs)
            return data

    def get_bot_by_id_with_http_info(self, bot_id, **kwargs):
        '''Get Bot details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bot_by_id_with_http_info(bot_id, async_req=True)
        >>> result = thread.get()


        :param int bot_id: (required)
        :return: Bot
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['bot_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method get_bot_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bot_id' is set
        if 'bot_id' not in params or params['bot_id'] is None:
            raise ValueError("Missing the required parameter `bot_id` when calling `get_bot_by_id`")

        collection_formats = {}

        path_params = {}
        if 'bot_id' in params:
            path_params['bot_id'] = params['bot_id']

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

        return self.api_client.call_api('/bots/{bot_id}', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='Bot', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def get_bots(self, **kwargs):
        '''List of Bots

        **PERMISSIONS: At least Active user is required.**   Returns a list of Bots starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Bots for other users. Regular users will see their own Bots.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bots(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseBot]
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bots_with_http_info(**kwargs)
        else:
            (data) = self.get_bots_with_http_info(**kwargs)
            return data

    def get_bots_with_http_info(self, **kwargs):
        '''List of Bots

        **PERMISSIONS: At least Active user is required.**   Returns a list of Bots starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Bots for other users. Regular users will see their own Bots.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bots_with_http_info(async_req=True)
        >>> result = thread.get()


        :param int limit: limit a number of items (allowed range is 1-100), default is 20.
        :param int offset: a number of items to skip, default is 0.
        :param int owner_id:
        :return: list[BaseBot]
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
                                " to method get_bots" % key)
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError("Invalid value for parameter `limit` when calling `get_bots`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError(
                "Invalid value for parameter `limit` when calling `get_bots`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError(
                "Invalid value for parameter `offset` when calling `get_bots`, must be a value greater than or equal to `0`")
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

        return self.api_client.call_api('/bots/', 'GET', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='list[BaseBot]', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_bot_by_id(self, bot_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_bot_by_id(bot_id, async_req=True)
        >>> result = thread.get()


        :param int bot_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_bot_by_id_with_http_info(bot_id, **kwargs)
        else:
            (data) = self.options_bot_by_id_with_http_info(bot_id, **kwargs)
            return data

    def options_bot_by_id_with_http_info(self, bot_id, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_bot_by_id_with_http_info(bot_id, async_req=True)
        >>> result = thread.get()


        :param int bot_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['bot_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method options_bot_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bot_id' is set
        if 'bot_id' not in params or params['bot_id'] is None:
            raise ValueError("Missing the required parameter `bot_id` when calling `options_bot_by_id`")

        collection_formats = {}

        path_params = {}
        if 'bot_id' in params:
            path_params['bot_id'] = params['bot_id']

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

        return self.api_client.call_api('/bots/{bot_id}', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_bots(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_bots(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_bots_with_http_info(**kwargs)
        else:
            (data) = self.options_bots_with_http_info(**kwargs)
            return data

    def options_bots_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_bots_with_http_info(async_req=True)
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
                                " to method options_bots" % key)
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

        return self.api_client.call_api('/bots/', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def options_get_bot_by_name(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_get_bot_by_name(async_req=True)
        >>> result = thread.get()


        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_get_bot_by_name_with_http_info(**kwargs)
        else:
            (data) = self.options_get_bot_by_name_with_http_info(**kwargs)
            return data

    def options_get_bot_by_name_with_http_info(self, **kwargs):
        '''Check which methods are allowed

        **PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_get_bot_by_name_with_http_info(async_req=True)
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
                                " to method options_get_bot_by_name" % key)
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

        return self.api_client.call_api('/bots/by_name', 'OPTIONS', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type=None, collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def patch_bot_by_id(self, bot_id, body, **kwargs):
        '''Patch bot details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_bot_by_id(bot_id, body, async_req=True)
        >>> result = thread.get()


        :param int bot_id: (required)
        :param list[Body1] body: (required)
        :return: Bot
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_bot_by_id_with_http_info(bot_id, body, **kwargs)
        else:
            (data) = self.patch_bot_by_id_with_http_info(bot_id, body, **kwargs)
            return data

    def patch_bot_by_id_with_http_info(self, bot_id, body, **kwargs):
        '''Patch bot details by ID

        **PERMISSIONS: Owner/Admin may execute this action.**
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_bot_by_id_with_http_info(bot_id, body, async_req=True)
        >>> result = thread.get()


        :param int bot_id: (required)
        :param list[Body1] body: (required)
        :return: Bot
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['bot_id', 'body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method patch_bot_by_id" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bot_id' is set
        if 'bot_id' not in params or params['bot_id'] is None:
            raise ValueError("Missing the required parameter `bot_id` when calling `patch_bot_by_id`")
        # verify the required parameter 'body' is set
        if 'body' not in params or params['body'] is None:
            raise ValueError("Missing the required parameter `body` when calling `patch_bot_by_id`")

        collection_formats = {}

        path_params = {}
        if 'bot_id' in params:
            path_params['bot_id'] = params['bot_id']

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

        return self.api_client.call_api('/bots/{bot_id}', 'PATCH', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='Bot', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_bots(self, app_name, **kwargs):
        '''Create a new Bot

        **PERMISSIONS: At least Active user is required.**   Bots are used for grouping apps into a single request

        :param str app_name: Name of the Bot (required)
        :param int reddit_id: Reddit App the bot will use
        :param int sentry_id: Sentry Token the bot will use
        :param int database_id: Database Credentials the bot will use
        :param int owner_id: Owner of the bot. Requires Admin to create for other users.
        :return: Bot
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_bots_with_http_info(app_name, **kwargs)
        else:
            (data) = self.post_bots_with_http_info(app_name, **kwargs)
            return data

    def post_bots_with_http_info(self, app_name, **kwargs):
        '''Create a new Bot

        **PERMISSIONS: At least Active user is required.**   Bots are used for grouping apps into a single request
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_bots_with_http_info(name, async_req=True)
        >>> result = thread.get()


        :param str app_name: Name of the Bot (required)
        :param int reddit_id: Reddit App the bot will use
        :param int sentry_id: Sentry Token the bot will use
        :param int database_id: Database Credentials the bot will use
        :param int owner_id: Owner of the bot. Requires Admin to create for other users.
        :return: Bot
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['name', 'reddit_id', 'sentry_id', 'database_id', 'owner_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_bots" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if 'name' not in params or params['name'] is None:
            raise ValueError("Missing the required parameter `name` when calling `post_bots`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'reddit_id' in params:
            form_params.append(('reddit_id', params['reddit_id']))
        if 'sentry_id' in params:
            form_params.append(('sentry_id', params['sentry_id']))
        if 'database_id' in params:
            form_params.append(('database_id', params['database_id']))
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

        return self.api_client.call_api('/bots/', 'POST', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='Bot', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))

    def post_get_bot_by_name(self, app_name, **kwargs):
        '''Get Refresh Token by reddit app and redditor

        **PERMISSIONS: At least Active user is required.**   Only Admins can specify ``owner_id`` to get other users' Bot details. If ``owner_id`` is not specified, only your Bots will be queried.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_get_bot_by_name(name, async_req=True)
        >>> result = thread.get()


        :param str app_name: Name of the Bot (required)
        :param int owner_id: Owner of the bot. Requires Admin to get for other users.
        :return: Bot
                 If the method is called asynchronously,
                 returns the request thread.
        '''
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_get_bot_by_name_with_http_info(app_name, **kwargs)
        else:
            (data) = self.post_get_bot_by_name_with_http_info(app_name, **kwargs)
            return data

    def post_get_bot_by_name_with_http_info(self, app_name, **kwargs):
        '''Get Refresh Token by reddit app and redditor

        **PERMISSIONS: At least Active user is required.**   Only Admins can specify ``owner_id`` to get other users' Bot details. If ``owner_id`` is not specified, only your Bots will be queried.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_get_bot_by_name_with_http_info(name, async_req=True)
        >>> result = thread.get()


        :param str app_name: Name of the Bot (required)
        :param int owner_id: Owner of the bot. Requires Admin to get for other users.
        :return: Bot
                 If the method is called asynchronously,
                 returns the request thread.
        '''

        all_params = ['name', 'owner_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method post_get_bot_by_name" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if 'name' not in params or params['name'] is None:
            raise ValueError("Missing the required parameter `name` when calling `post_get_bot_by_name`")

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

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basic']

        return self.api_client.call_api('/bots/by_name', 'POST', path_params, query_params, header_params, body=body_params, params=form_params,
                                        response_type='Bot', collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True), _request_timeout=params.get('_request_timeout'))