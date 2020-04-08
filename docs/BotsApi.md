# CredentialManager.BotsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bot_by_id**](BotsApi.md#delete_bot_by_id) | **DELETE** /bots/{bot_id} | Delete a Bot by ID
[**get_bot_by_id**](BotsApi.md#get_bot_by_id) | **GET** /bots/{bot_id} | Get Bot details by ID
[**get_bots**](BotsApi.md#get_bots) | **GET** /bots/ | List of Bots
[**options_bot_by_id**](BotsApi.md#options_bot_by_id) | **OPTIONS** /bots/{bot_id} | Check which methods are allowed
[**options_bots**](BotsApi.md#options_bots) | **OPTIONS** /bots/ | Check which methods are allowed
[**options_get_bot_by_name**](BotsApi.md#options_get_bot_by_name) | **OPTIONS** /bots/by_name | Check which methods are allowed
[**patch_bot_by_id**](BotsApi.md#patch_bot_by_id) | **PATCH** /bots/{bot_id} | Patch bot details by ID
[**post_bots**](BotsApi.md#post_bots) | **POST** /bots/ | Create a new Bot
[**post_get_bot_by_name**](BotsApi.md#post_get_bot_by_name) | **POST** /bots/by_name | Get Refresh Token by reddit app and redditor


# **delete_bot_by_id**
> delete_bot_by_id(bot_id)

Delete a Bot by ID

**PERMISSIONS: Owner/Admin may execute this action.**

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))
bot_id = 56 # int | 

try:
    # Delete a Bot by ID
    api_instance.delete_bot_by_id(bot_id)
except ApiException as e:
    print("Exception when calling BotsApi->delete_bot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_by_id**
> Bot get_bot_by_id(bot_id)

Get Bot details by ID

**PERMISSIONS: Owner/Admin may execute this action.**

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))
bot_id = 56 # int | 

try:
    # Get Bot details by ID
    api_response = api_instance.get_bot_by_id(bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->get_bot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 

### Return type

[**Bot**](Bot.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bots**
> list[BaseBot] get_bots(limit=limit, offset=offset, owner_id=owner_id)

List of Bots

**PERMISSIONS: At least Active user is required.**   Returns a list of Bots starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Bots for other users. Regular users will see their own Bots.

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))
limit = 20 # int | limit a number of items (allowed range is 1-100), default is 20. (optional) (default to 20)
offset = 0 # int | a number of items to skip, default is 0. (optional) (default to 0)
owner_id = 56 # int |  (optional)

try:
    # List of Bots
    api_response = api_instance.get_bots(limit=limit, offset=offset, owner_id=owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->get_bots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit a number of items (allowed range is 1-100), default is 20. | [optional] [default to 20]
 **offset** | **int**| a number of items to skip, default is 0. | [optional] [default to 0]
 **owner_id** | **int**|  | [optional] 

### Return type

[**list[BaseBot]**](BaseBot.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_bot_by_id**
> options_bot_by_id(bot_id)

Check which methods are allowed

**PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))
bot_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_bot_by_id(bot_id)
except ApiException as e:
    print("Exception when calling BotsApi->options_bot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_bots**
> options_bots()

Check which methods are allowed

**PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_bots()
except ApiException as e:
    print("Exception when calling BotsApi->options_bots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_get_bot_by_name**
> options_get_bot_by_name()

Check which methods are allowed

**PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_get_bot_by_name()
except ApiException as e:
    print("Exception when calling BotsApi->options_get_bot_by_name: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_bot_by_id**
> Bot patch_bot_by_id(bot_id, body)

Patch bot details by ID

**PERMISSIONS: Owner/Admin may execute this action.**

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))
bot_id = 56 # int | 
body = [CredentialManager.Body1()] # list[Body1] | 

try:
    # Patch bot details by ID
    api_response = api_instance.patch_bot_by_id(bot_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->patch_bot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **body** | [**list[Body1]**](Body1.md)|  | 

### Return type

[**Bot**](Bot.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bots**
> Bot post_bots(app_name, reddit_id=reddit_id, sentry_id=sentry_id, database_id=database_id, owner_id=owner_id)

Create a new Bot

**PERMISSIONS: At least Active user is required.**   Bots are used for grouping apps into a single request

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))
app_name = 'app_name_example' # str | Name of the Bot
reddit_id = 56 # int | Reddit App the bot will use (optional)
sentry_id = 56 # int | Sentry Token the bot will use (optional)
database_id = 56 # int | Database Credentials the bot will use (optional)
owner_id = 56 # int | Owner of the bot. Requires Admin to create for other users. (optional)

try:
    # Create a new Bot
    api_response = api_instance.post_bots(app_name, reddit_id=reddit_id, sentry_id=sentry_id, database_id=database_id, owner_id=owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->post_bots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Name of the Bot | 
 **reddit_id** | **int**| Reddit App the bot will use | [optional] 
 **sentry_id** | **int**| Sentry Token the bot will use | [optional] 
 **database_id** | **int**| Database Credentials the bot will use | [optional] 
 **owner_id** | **int**| Owner of the bot. Requires Admin to create for other users. | [optional] 

### Return type

[**Bot**](Bot.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_bot_by_name**
> Bot post_get_bot_by_name(app_name, owner_id=owner_id)

Get Refresh Token by reddit app and redditor

**PERMISSIONS: At least Active user is required.**   Only Admins can specify ``owner_id`` to get other users' Bot details. If ``owner_id`` is not specified, only your Bots will be queried.

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-KEY'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.BotsApi(CredentialManager.ApiClient(config))
app_name = 'app_name_example' # str | Name of the Bot
owner_id = 56 # int | Owner of the bot. Requires Admin to get for other users. (optional)

try:
    # Get Refresh Token by reddit app and redditor
    api_response = api_instance.post_get_bot_by_name(app_name, owner_id=owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->post_get_bot_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Name of the Bot | 
 **owner_id** | **int**| Owner of the bot. Requires Admin to get for other users. | [optional] 

### Return type

[**Bot**](Bot.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

