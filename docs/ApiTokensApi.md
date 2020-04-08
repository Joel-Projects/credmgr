# CredentialManager.ApiTokensApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](ApiTokensApi.md#delete) | **DELETE** /api_tokens/{item_id} | Delete a API Token by ID
[**get_api_token_by_id**](ApiTokensApi.md#get_api_token_by_id) | **GET** /api_tokens/{item_id} | Get API Token details by ID
[**get_api_tokens**](ApiTokensApi.md#get_api_tokens) | **GET** /api_tokens/ | List of API Tokens
[**options_api_token_by_id**](ApiTokensApi.md#options_api_token_by_id) | **OPTIONS** /api_tokens/{item_id} | Check which methods are allowed
[**options_api_tokens**](ApiTokensApi.md#options_api_tokens) | **OPTIONS** /api_tokens/ | Check which methods are allowed
[**patch_api_token_by_id**](ApiTokensApi.md#patch_api_token_by_id) | **PATCH** /api_tokens/{item_id} | Patch api_token details by ID
[**post_api_tokens**](ApiTokensApi.md#post_api_tokens) | **POST** /api_tokens/ | Create a new API Token


# **delete**
> delete(item_id)

Delete a API Token by ID

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
api_instance = CredentialManager.ApiTokensApi(CredentialManager.ApiClient(config))
item_id = 56 # int | 

try:
    # Delete a API Token by ID
    api_instance.delete(item_id)
except ApiException as e:
    print("Exception when calling ApiTokensApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token_by_id**
> ApiToken get_api_token_by_id(item_id)

Get API Token details by ID

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
api_instance = CredentialManager.ApiTokensApi(CredentialManager.ApiClient(config))
item_id = 56 # int | 

try:
    # Get API Token details by ID
    api_response = api_instance.get_api_token_by_id(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->get_api_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**ApiToken**](ApiToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_tokens**
> list[BaseApiToken] get_api_tokens(limit=limit, offset=offset, owner_id=owner_id)

List of API Tokens

**PERMISSIONS: At least Active user is required.**   Returns a list of API Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see API Tokens for other users. Regular users will see their own API Tokens.

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
api_instance = CredentialManager.ApiTokensApi(CredentialManager.ApiClient(config))
limit = 20 # int | limit a number of items (allowed range is 1-100), default is 20. (optional) (default to 20)
offset = 0 # int | a number of items to skip, default is 0. (optional) (default to 0)
owner_id = 56 # int |  (optional)

try:
    # List of API Tokens
    api_response = api_instance.get_api_tokens(limit=limit, offset=offset, owner_id=owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->get_api_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit a number of items (allowed range is 1-100), default is 20. | [optional] [default to 20]
 **offset** | **int**| a number of items to skip, default is 0. | [optional] [default to 0]
 **owner_id** | **int**|  | [optional] 

### Return type

[**list[BaseApiToken]**](BaseApiToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_api_token_by_id**
> options_api_token_by_id(item_id)

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
api_instance = CredentialManager.ApiTokensApi(CredentialManager.ApiClient(config))
item_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_api_token_by_id(item_id)
except ApiException as e:
    print("Exception when calling ApiTokensApi->options_api_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_api_tokens**
> options_api_tokens()

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
api_instance = CredentialManager.ApiTokensApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_api_tokens()
except ApiException as e:
    print("Exception when calling ApiTokensApi->options_api_tokens: %s\n" % e)
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

# **patch_api_token_by_id**
> ApiToken patch_api_token_by_id(item_id, body)

Patch api_token details by ID

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
api_instance = CredentialManager.ApiTokensApi(CredentialManager.ApiClient(config))
item_id = 56 # int | 
body = [CredentialManager.Body()] # list[Body] | 

try:
    # Patch api_token details by ID
    api_response = api_instance.patch_api_token_by_id(item_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->patch_api_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **body** | [**list[Body]**](Body.md)|  | 

### Return type

[**ApiToken**](ApiToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_tokens**
> ApiToken post_api_tokens(name, owner_id=owner_id, length=length)

Create a new API Token

**PERMISSIONS: At least Active user is required.**   API token can be used instead of username/password. Include the API token in the ``X-API-KEY`` header

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
api_instance = CredentialManager.ApiTokensApi(CredentialManager.ApiClient(config))
name = 'name_example' # str | Name of the API token
owner_id = 56 # int | Owner of the token. Requires Admin to create for other users. (optional)
length = 56 # int | Length of the token. Must be between 16 and 128, `16<=length<=128`. Defaults to `32` (optional)

try:
    # Create a new API Token
    api_response = api_instance.post_api_tokens(name, owner_id=owner_id, length=length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->post_api_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the API token | 
 **owner_id** | **int**| Owner of the token. Requires Admin to create for other users. | [optional] 
 **length** | **int**| Length of the token. Must be between 16 and 128, &#x60;16&lt;&#x3D;length&lt;&#x3D;128&#x60;. Defaults to &#x60;32&#x60; | [optional] 

### Return type

[**ApiToken**](ApiToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

