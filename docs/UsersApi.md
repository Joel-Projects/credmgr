# CredentialManager.UsersApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_by_id**](UsersApi.md#delete_user_by_id) | **DELETE** /users/{user_id} | Delete a user by ID
[**get_apps_by_user_id**](UsersApi.md#get_apps_by_user_id) | **GET** /users/{user_id}/apps | Get items that is owned by user
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{user_id} | Get user details by ID
[**get_user_me**](UsersApi.md#get_user_me) | **GET** /users/me | Get current user details
[**get_users**](UsersApi.md#get_users) | **GET** /users/ | List of users
[**options_apps_by_user_id**](UsersApi.md#options_apps_by_user_id) | **OPTIONS** /users/{user_id}/apps | Check which methods are allowed
[**options_user_by_id**](UsersApi.md#options_user_by_id) | **OPTIONS** /users/{user_id} | Check which methods are allowed
[**options_user_me**](UsersApi.md#options_user_me) | **OPTIONS** /users/me | Check which methods are allowed
[**options_users**](UsersApi.md#options_users) | **OPTIONS** /users/ | Check which methods are allowed
[**patch_user_by_id**](UsersApi.md#patch_user_by_id) | **PATCH** /users/{user_id} | Patch user details by ID
[**post_users**](UsersApi.md#post_users) | **POST** /users/ | Create a new user


# **delete_user_by_id**
> delete_user_by_id(user_id)

Delete a user by ID

**PERMISSIONS: Admin role is required.**

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))
user_id = 56 # int | 

try:
    # Delete a user by ID
    api_instance.delete_user_by_id(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps_by_user_id**
> UserItems get_apps_by_user_id(user_id)

Get items that is owned by user

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))
user_id = 56 # int | 

try:
    # Get items that is owned by user
    api_response = api_instance.get_apps_by_user_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_apps_by_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserItems**](UserItems.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> User get_user_by_id(user_id)

Get user details by ID

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))
user_id = 56 # int | 

try:
    # Get user details by ID
    api_response = api_instance.get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_me**
> User get_user_me()

Get current user details

**PERMISSIONS: At least Active user is required.**

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))

try:
    # Get current user details
    api_response = api_instance.get_user_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[BaseUser] get_users(limit=limit, offset=offset)

List of users

**PERMISSIONS: Admin role is required.**   Returns a list of users starting from ``offset`` limited by ``limit`` parameter.

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))
limit = 20 # int | limit a number of items (allowed range is 1-100), default is 20. (optional) (default to 20)
offset = 0 # int | a number of items to skip, default is 0. (optional) (default to 0)

try:
    # List of users
    api_response = api_instance.get_users(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit a number of items (allowed range is 1-100), default is 20. | [optional] [default to 20]
 **offset** | **int**| a number of items to skip, default is 0. | [optional] [default to 0]

### Return type

[**list[BaseUser]**](BaseUser.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_apps_by_user_id**
> options_apps_by_user_id(user_id)

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))
user_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_apps_by_user_id(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->options_apps_by_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_user_by_id**
> options_user_by_id(user_id)

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))
user_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_user_by_id(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->options_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_user_me**
> options_user_me()

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_user_me()
except ApiException as e:
    print("Exception when calling UsersApi->options_user_me: %s\n" % e)
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

# **options_users**
> options_users()

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_users()
except ApiException as e:
    print("Exception when calling UsersApi->options_users: %s\n" % e)
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

# **patch_user_by_id**
> User patch_user_by_id(user_id, body)

Patch user details by ID

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))
user_id = 56 # int | 
body = [CredentialManager.Body7()] # list[Body7] | 

try:
    # Patch user details by ID
    api_response = api_instance.patch_user_by_id(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body** | [**list[Body7]**](Body7.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users**
> User post_users(username, password, default_settings=default_settings, is_admin=is_admin, is_active=is_active, is_regular_user=is_regular_user, is_internal=is_internal, reddit_username=reddit_username)

Create a new user

**PERMISSIONS: Admin role is required.**

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
api_instance = CredentialManager.UsersApi(CredentialManager.ApiClient(config))
username = 'username_example' # str | Username for new user (Example: ```spaz```)
password = 'password_example' # str | Password for new user (Example: ```supersecurepassword```)
default_settings = 'default_settings_example' # str | Default values to use for new apps (Example: ```{\"database_flavor\": \"postgres\", \"database_host\": \"localhost\"}```) (optional)
is_admin = true # bool | Is the user an admin? Allows the user to see all objects and create users (Default: ``false``) (optional)
is_active = true # bool | Is the user active? Allows the user to sign in (Default: ``true``) (optional)
is_regular_user = true # bool | (Internal use only) (optional)
is_internal = true # bool | (Internal use only) (optional)
reddit_username = 'reddit_username_example' # str |  (optional)

try:
    # Create a new user
    api_response = api_instance.post_users(username, password, default_settings=default_settings, is_admin=is_admin, is_active=is_active, is_regular_user=is_regular_user, is_internal=is_internal, reddit_username=reddit_username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for new user (Example: &#x60;&#x60;&#x60;spaz&#x60;&#x60;&#x60;) | 
 **password** | **str**| Password for new user (Example: &#x60;&#x60;&#x60;supersecurepassword&#x60;&#x60;&#x60;) | 
 **default_settings** | **str**| Default values to use for new apps (Example: &#x60;&#x60;&#x60;{\&quot;database_flavor\&quot;: \&quot;postgres\&quot;, \&quot;database_host\&quot;: \&quot;localhost\&quot;}&#x60;&#x60;&#x60;) | [optional] 
 **is_admin** | **bool**| Is the user an admin? Allows the user to see all objects and create users (Default: &#x60;&#x60;false&#x60;&#x60;) | [optional] 
 **is_active** | **bool**| Is the user active? Allows the user to sign in (Default: &#x60;&#x60;true&#x60;&#x60;) | [optional] 
 **is_regular_user** | **bool**| (Internal use only) | [optional] 
 **is_internal** | **bool**| (Internal use only) | [optional] 
 **reddit_username** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

