# CredentialManager.RefreshTokensApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_refresh_token_by_id**](RefreshTokensApi.md#delete_refresh_token_by_id) | **DELETE** /refresh_tokens/{refresh_token_id} | Delete a Refresh Token by ID
[**get_refresh_token_by_id**](RefreshTokensApi.md#get_refresh_token_by_id) | **GET** /refresh_tokens/{refresh_token_id} | Get Refresh Token details by ID
[**get_refresh_tokens**](RefreshTokensApi.md#get_refresh_tokens) | **GET** /refresh_tokens/ | List of Refresh Tokens
[**options_get_refresh_token_by_redditor**](RefreshTokensApi.md#options_get_refresh_token_by_redditor) | **OPTIONS** /refresh_tokens/by_redditor | Check which methods are allowed
[**options_refresh_token_by_id**](RefreshTokensApi.md#options_refresh_token_by_id) | **OPTIONS** /refresh_tokens/{refresh_token_id} | Check which methods are allowed
[**options_refresh_tokens**](RefreshTokensApi.md#options_refresh_tokens) | **OPTIONS** /refresh_tokens/ | Check which methods are allowed
[**patch_refresh_token_by_id**](RefreshTokensApi.md#patch_refresh_token_by_id) | **PATCH** /refresh_tokens/{refresh_token_id} | Patch refresh_token details by ID
[**post_get_refresh_token_by_redditor**](RefreshTokensApi.md#post_get_refresh_token_by_redditor) | **POST** /refresh_tokens/by_redditor | Get Refresh Token by reddit app and redditor


# **delete_refresh_token_by_id**
> delete_refresh_token_by_id(refresh_token_id)

Delete a Refresh Token by ID

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
api_instance = CredentialManager.RefreshTokensApi(CredentialManager.ApiClient(config))
refresh_token_id = 56 # int | 

try:
    # Delete a Refresh Token by ID
    api_instance.delete_refresh_token_by_id(refresh_token_id)
except ApiException as e:
    print("Exception when calling RefreshTokensApi->delete_refresh_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refresh_token_by_id**
> RefreshToken get_refresh_token_by_id(refresh_token_id)

Get Refresh Token details by ID

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
api_instance = CredentialManager.RefreshTokensApi(CredentialManager.ApiClient(config))
refresh_token_id = 56 # int | 

try:
    # Get Refresh Token details by ID
    api_response = api_instance.get_refresh_token_by_id(refresh_token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefreshTokensApi->get_refresh_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_id** | **int**|  | 

### Return type

[**RefreshToken**](RefreshToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refresh_tokens**
> list[BaseRefreshToken] get_refresh_tokens(limit=limit, redditor=redditor, offset=offset, owner_id=owner_id)

List of Refresh Tokens

**PERMISSIONS: At least Active user is required.**   Returns a list of Refresh Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner_id`` to see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.

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
api_instance = CredentialManager.RefreshTokensApi(CredentialManager.ApiClient(config))
limit = 20 # int | limit a number of items (allowed range is 1-100), default is 20. (optional) (default to 20)
redditor = 'redditor_example' # str |  (optional)
offset = 0 # int | a number of items to skip, default is 0. (optional) (default to 0)
owner_id = 56 # int |  (optional)

try:
    # List of Refresh Tokens
    api_response = api_instance.get_refresh_tokens(limit=limit, redditor=redditor, offset=offset, owner_id=owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefreshTokensApi->get_refresh_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit a number of items (allowed range is 1-100), default is 20. | [optional] [default to 20]
 **redditor** | **str**|  | [optional] 
 **offset** | **int**| a number of items to skip, default is 0. | [optional] [default to 0]
 **owner_id** | **int**|  | [optional] 

### Return type

[**list[BaseRefreshToken]**](BaseRefreshToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_get_refresh_token_by_redditor**
> options_get_refresh_token_by_redditor()

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
api_instance = CredentialManager.RefreshTokensApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_get_refresh_token_by_redditor()
except ApiException as e:
    print("Exception when calling RefreshTokensApi->options_get_refresh_token_by_redditor: %s\n" % e)
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

# **options_refresh_token_by_id**
> options_refresh_token_by_id(refresh_token_id)

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
api_instance = CredentialManager.RefreshTokensApi(CredentialManager.ApiClient(config))
refresh_token_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_refresh_token_by_id(refresh_token_id)
except ApiException as e:
    print("Exception when calling RefreshTokensApi->options_refresh_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_refresh_tokens**
> options_refresh_tokens()

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
api_instance = CredentialManager.RefreshTokensApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_refresh_tokens()
except ApiException as e:
    print("Exception when calling RefreshTokensApi->options_refresh_tokens: %s\n" % e)
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

# **patch_refresh_token_by_id**
> RefreshToken patch_refresh_token_by_id(refresh_token_id, body)

Patch refresh_token details by ID

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
api_instance = CredentialManager.RefreshTokensApi(CredentialManager.ApiClient(config))
refresh_token_id = 56 # int | 
body = [CredentialManager.Body4()] # list[Body4] | 

try:
    # Patch refresh_token details by ID
    api_response = api_instance.patch_refresh_token_by_id(refresh_token_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefreshTokensApi->patch_refresh_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_id** | **int**|  | 
 **body** | [**list[Body4]**](Body4.md)|  | 

### Return type

[**RefreshToken**](RefreshToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_refresh_token_by_redditor**
> RefreshToken post_get_refresh_token_by_redditor(redditor, reddit_app_id)

Get Refresh Token by reddit app and redditor

**PERMISSIONS: At least Active user is required.**   Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.

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
api_instance = CredentialManager.RefreshTokensApi(CredentialManager.ApiClient(config))
redditor = 'redditor_example' # str | Redditor the Refresh Token is for
reddit_app_id = 56 # int | Reddit app the Refresh Token is for

try:
    # Get Refresh Token by reddit app and redditor
    api_response = api_instance.post_get_refresh_token_by_redditor(redditor, reddit_app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefreshTokensApi->post_get_refresh_token_by_redditor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redditor** | **str**| Redditor the Refresh Token is for | 
 **reddit_app_id** | **int**| Reddit app the Refresh Token is for | 

### Return type

[**RefreshToken**](RefreshToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

