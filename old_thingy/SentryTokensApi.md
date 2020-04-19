# CredentialManager.SentryTokensApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sentry_token_by_id**](SentryTokensApi.md#delete_sentry_token_by_id) | **DELETE** /sentry_tokens/{sentry_token_id} | Delete a Sentry Token by ID
[**get_sentry_token_by_id**](SentryTokensApi.md#get_sentry_token_by_id) | **GET** /sentry_tokens/{sentry_token_id} | Get Sentry Token details by ID
[**get_sentry_tokens**](SentryTokensApi.md#get_sentry_tokens) | **GET** /sentry_tokens/ | List of Sentry Tokens
[**options_sentry_token_by_id**](SentryTokensApi.md#options_sentry_token_by_id) | **OPTIONS** /sentry_tokens/{sentry_token_id} | Check which methods are allowed
[**options_sentry_tokens**](SentryTokensApi.md#options_sentry_tokens) | **OPTIONS** /sentry_tokens/ | Check which methods are allowed
[**patch_sentry_token_by_id**](SentryTokensApi.md#patch_sentry_token_by_id) | **PATCH** /sentry_tokens/{sentry_token_id} | Patch sentry_token details by ID
[**post_sentry_tokens**](SentryTokensApi.md#post_sentry_tokens) | **POST** /sentry_tokens/ | Create a new Sentry Token


# **delete_sentry_token_by_id**
> delete_sentry_token_by_id(sentry_token_id)

Delete a Sentry Token by ID

**PERMISSIONS: Owner/Admin may execute this action.**

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import APIException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-TOKEN'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.SentryTokensApi(CredentialManager.ApiClient(config))
sentry_token_id = 56 # int | 

try:
    # Delete a Sentry Token by ID
    api_instance.delete_sentry_token_by_id(sentry_token_id)
except APIException as e:
    print("Exception when calling SentryTokensApi->delete_sentry_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sentry_token_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sentry_token_by_id**
> SentryToken get_sentry_token_by_id(sentry_token_id)

Get Sentry Token details by ID

**PERMISSIONS: Owner/Admin may execute this action.**

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import APIException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-TOKEN'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.SentryTokensApi(CredentialManager.ApiClient(config))
sentry_token_id = 56 # int | 

try:
    # Get Sentry Token details by ID
    api_response = api_instance.get_sentry_token_by_id(sentry_token_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling SentryTokensApi->get_sentry_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sentry_token_id** | **int**|  | 

### Return type

[**SentryToken**](SentryToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sentry_tokens**
> list[BaseSentryToken] get_sentry_tokens(limit=limit, offset=offset, owner_id=owner_id)

List of Sentry Tokens

**PERMISSIONS: At least Active user is required.**   Returns a list of Sentry Tokens starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Sentry Tokens for other users. Regular users will see their own Sentry Tokens.

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import APIException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-TOKEN'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.SentryTokensApi(CredentialManager.ApiClient(config))
limit = 20 # int | limit a number of items (allowed range is 1-100), default is 20. (optional) (default to 20)
offset = 0 # int | a number of items to skip, default is 0. (optional) (default to 0)
owner_id = 56 # int |  (optional)

try:
    # List of Sentry Tokens
    api_response = api_instance.get_sentry_tokens(limit=limit, offset=offset, owner_id=owner_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling SentryTokensApi->get_sentry_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit a number of items (allowed range is 1-100), default is 20. | [optional] [default to 20]
 **offset** | **int**| a number of items to skip, default is 0. | [optional] [default to 0]
 **owner_id** | **int**|  | [optional] 

### Return type

[**list[BaseSentryToken]**](BaseSentryToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_sentry_token_by_id**
> options_sentry_token_by_id(sentry_token_id)

Check which methods are allowed

**PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import APIException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-TOKEN'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.SentryTokensApi(CredentialManager.ApiClient(config))
sentry_token_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_sentry_token_by_id(sentry_token_id)
except APIException as e:
    print("Exception when calling SentryTokensApi->options_sentry_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sentry_token_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_sentry_tokens**
> options_sentry_tokens()

Check which methods are allowed

**PERMISSIONS: At least Active user is required.**   Use this method if you need to know what operations are allowed to be performed on this endpoint, e.g. to decide wether to display a button in your UI.  The list of allowed methods is provided in `Allow` response header.

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import APIException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-TOKEN'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.SentryTokensApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_sentry_tokens()
except APIException as e:
    print("Exception when calling SentryTokensApi->options_sentry_tokens: %s\n" % e)
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

# **patch_sentry_token_by_id**
> SentryToken patch_sentry_token_by_id(sentry_token_id, body)

Patch sentry_token details by ID

**PERMISSIONS: Owner/Admin may execute this action.**

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import APIException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-TOKEN'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.SentryTokensApi(CredentialManager.ApiClient(config))
sentry_token_id = 56 # int | 
body = [CredentialManager.Body5()] # list[Body5] | 

try:
    # Patch sentry_token details by ID
    api_response = api_instance.patch_sentry_token_by_id(sentry_token_id, body)
    pprint(api_response)
except APIException as e:
    print("Exception when calling SentryTokensApi->patch_sentry_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sentry_token_id** | **int**|  | 
 **body** | [**list[Body5]**](Body5.md)|  | 

### Return type

[**SentryToken**](SentryToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sentry_tokens**
> SentryToken post_sentry_tokens(app_name, dsn, enabled=enabled, owner_id=owner_id)

Create a new Sentry Token

**PERMISSIONS: At least Active user is required.**   Sentry Tokens are used for logging and error reporting in applications

### Example
```python
from __future__ import print_function
import time
import CredentialManager
from CredentialManager.requestor import APIException
from pprint import pprint

# Configure API key authorization: apiKey
config = CredentialManager.Configuration()
config.api_key['X-API-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# config.api_key_prefix['X-API-TOKEN'] = 'Bearer'
# Configure HTTP basic authorization: basic
config = CredentialManager.Configuration()
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = CredentialManager.SentryTokensApi(CredentialManager.ApiClient(config))
app_name = 'app_name_example' # str | Name of the Sentry Token
dsn = 'dsn_example' # str | DSN of the Sentry Token
enabled = true # bool |  (optional)
owner_id = 56 # int | Owner of the token. Requires Admin to create for other users. (optional)

try:
    # Create a new Sentry Token
    api_response = api_instance.post_sentry_tokens(app_name, dsn, enabled=enabled, owner_id=owner_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling SentryTokensApi->post_sentry_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Name of the Sentry Token | 
 **dsn** | **str**| DSN of the Sentry Token | 
 **enabled** | **bool**|  | [optional] 
 **owner_id** | **int**| Owner of the token. Requires Admin to create for other users. | [optional] 

### Return type

[**SentryToken**](SentryToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

