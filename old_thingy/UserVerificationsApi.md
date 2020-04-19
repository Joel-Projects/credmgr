# CredentialManager.UserVerificationsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_verification_by_id**](UserVerificationsApi.md#delete_user_verification_by_id) | **DELETE** /user_verifications/{user_verification_id} | Delete a User Verification by ID
[**get_user_verification_by_id**](UserVerificationsApi.md#get_user_verification_by_id) | **GET** /user_verifications/{user_verification_id} | Get User Verification details by ID
[**get_user_verifications**](UserVerificationsApi.md#get_user_verifications) | **GET** /user_verifications/ | List of User Verifications
[**options_get_user_verification_by_user_id**](UserVerificationsApi.md#options_get_user_verification_by_user_id) | **OPTIONS** /user_verifications/get_redditor | Check which methods are allowed
[**options_user_verification_by_id**](UserVerificationsApi.md#options_user_verification_by_id) | **OPTIONS** /user_verifications/{user_verification_id} | Check which methods are allowed
[**options_user_verifications**](UserVerificationsApi.md#options_user_verifications) | **OPTIONS** /user_verifications/ | Check which methods are allowed
[**patch_user_verification_by_id**](UserVerificationsApi.md#patch_user_verification_by_id) | **PATCH** /user_verifications/{user_verification_id} | Patch user_verification details by ID
[**post_get_user_verification_by_user_id**](UserVerificationsApi.md#post_get_user_verification_by_user_id) | **POST** /user_verifications/get_redditor | Get User Verification by User ID
[**post_user_verifications**](UserVerificationsApi.md#post_user_verifications) | **POST** /user_verifications/ | Create a new User Verification


# **delete_user_verification_by_id**
> delete_user_verification_by_id(user_verification_id)

Delete a User Verification by ID

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))
user_verification_id = 56 # int | 

try:
    # Delete a User Verification by ID
    api_instance.delete_user_verification_by_id(user_verification_id)
except APIException as e:
    print("Exception when calling UserVerificationsApi->delete_user_verification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_verification_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_verification_by_id**
> UserVerification get_user_verification_by_id(user_verification_id)

Get User Verification details by ID

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))
user_verification_id = 56 # int | 

try:
    # Get User Verification details by ID
    api_response = api_instance.get_user_verification_by_id(user_verification_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling UserVerificationsApi->get_user_verification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_verification_id** | **int**|  | 

### Return type

[**UserVerification**](UserVerification.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_verifications**
> list[BaseUserVerification] get_user_verifications(limit=limit, offset=offset, owner_id=owner_id)

List of User Verifications

**PERMISSIONS: At least Active user is required.**   Returns a list of User Verifications starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see User Verifications for other users. Regular users will see their own User Verifications.

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))
limit = 20 # int | limit a number of items (allowed range is 1-100), default is 20. (optional) (default to 20)
offset = 0 # int | a number of items to skip, default is 0. (optional) (default to 0)
owner_id = 56 # int |  (optional)

try:
    # List of User Verifications
    api_response = api_instance.get_user_verifications(limit=limit, offset=offset, owner_id=owner_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling UserVerificationsApi->get_user_verifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit a number of items (allowed range is 1-100), default is 20. | [optional] [default to 20]
 **offset** | **int**| a number of items to skip, default is 0. | [optional] [default to 0]
 **owner_id** | **int**|  | [optional] 

### Return type

[**list[BaseUserVerification]**](BaseUserVerification.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_get_user_verification_by_user_id**
> options_get_user_verification_by_user_id()

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_get_user_verification_by_user_id()
except APIException as e:
    print("Exception when calling UserVerificationsApi->options_get_user_verification_by_user_id: %s\n" % e)
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

# **options_user_verification_by_id**
> options_user_verification_by_id(user_verification_id)

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))
user_verification_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_user_verification_by_id(user_verification_id)
except APIException as e:
    print("Exception when calling UserVerificationsApi->options_user_verification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_verification_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_user_verifications**
> options_user_verifications()

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_user_verifications()
except APIException as e:
    print("Exception when calling UserVerificationsApi->options_user_verifications: %s\n" % e)
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

# **patch_user_verification_by_id**
> UserVerification patch_user_verification_by_id(user_verification_id, body)

Patch user_verification details by ID

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))
user_verification_id = 56 # int | 
body = [CredentialManager.Body6()] # list[Body6] | 

try:
    # Patch user_verification details by ID
    api_response = api_instance.patch_user_verification_by_id(user_verification_id, body)
    pprint(api_response)
except APIException as e:
    print("Exception when calling UserVerificationsApi->patch_user_verification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_verification_id** | **int**|  | 
 **body** | [**list[Body6]**](Body6.md)|  | 

### Return type

[**UserVerification**](UserVerification.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_user_verification_by_user_id**
> UserVerification post_get_user_verification_by_user_id(user_id, reddit_app_id=reddit_app_id)

Get User Verification by User ID

**PERMISSIONS: At least Active user is required.**   Optionally filter by Reddit App ID  Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))
user_id = 'user_id_example' # str | User ID to associate Redditor with
reddit_app_id = 56 # int | Optionally specify a Reddit app the User Verification belongs to (optional)

try:
    # Get User Verification by User ID
    api_response = api_instance.post_get_user_verification_by_user_id(user_id, reddit_app_id=reddit_app_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling UserVerificationsApi->post_get_user_verification_by_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID to associate Redditor with | 
 **reddit_app_id** | **int**| Optionally specify a Reddit app the User Verification belongs to | [optional] 

### Return type

[**UserVerification**](UserVerification.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_verifications**
> UserVerification post_user_verifications(user_id, reddit_app_id, redditor=redditor, extra_data=extra_data, owner_id=owner_id)

Create a new User Verification

**PERMISSIONS: At least Active user is required.**   User Verifications for verifying a redditor with a User ID

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
api_instance = CredentialManager.UserVerificationsApi(CredentialManager.ApiClient(config))
user_id = 'user_id_example' # str | User ID to associate Redditor with
reddit_app_id = 56 # int | Reddit app the User Verification is for
redditor = 'redditor_example' # str | Redditor the User Verification is for (optional)
extra_data = 'extra_data_example' # str | Extra JSON data to include with verification (optional)
owner_id = 56 # int | Owner of the verification. Requires Admin to create for other users. (optional)

try:
    # Create a new User Verification
    api_response = api_instance.post_user_verifications(user_id, reddit_app_id, redditor=redditor, extra_data=extra_data, owner_id=owner_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling UserVerificationsApi->post_user_verifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID to associate Redditor with | 
 **reddit_app_id** | **int**| Reddit app the User Verification is for | 
 **redditor** | **str**| Redditor the User Verification is for | [optional] 
 **extra_data** | **str**| Extra JSON data to include with verification | [optional] 
 **owner_id** | **int**| Owner of the verification. Requires Admin to create for other users. | [optional] 

### Return type

[**UserVerification**](UserVerification.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

