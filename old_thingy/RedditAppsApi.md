# CredentialManager.RedditAppsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_reddit_app_by_id**](RedditAppsApi.md#delete_reddit_app_by_id) | **DELETE** /reddit_apps/{reddit_app_id} | Delete a Reddit App by ID
[**get_reddit_app_by_id**](RedditAppsApi.md#get_reddit_app_by_id) | **GET** /reddit_apps/{reddit_app_id} | Get Reddit App details by ID
[**get_reddit_apps**](RedditAppsApi.md#get_reddit_apps) | **GET** /reddit_apps/ | List of Reddit Apps
[**options_generate_auth_url**](RedditAppsApi.md#options_generate_auth_url) | **OPTIONS** /reddit_apps/{reddit_app_id}/generate_auth | Check which methods are allowed
[**options_reddit_app_by_id**](RedditAppsApi.md#options_reddit_app_by_id) | **OPTIONS** /reddit_apps/{reddit_app_id} | Check which methods are allowed
[**options_reddit_apps**](RedditAppsApi.md#options_reddit_apps) | **OPTIONS** /reddit_apps/ | Check which methods are allowed
[**patch_reddit_app_by_id**](RedditAppsApi.md#patch_reddit_app_by_id) | **PATCH** /reddit_apps/{reddit_app_id} | Patch reddit_app details by ID
[**post_generate_auth_url**](RedditAppsApi.md#post_generate_auth_url) | **POST** /reddit_apps/{reddit_app_id}/generate_auth | Generate a reddit auth url
[**post_reddit_app_by_id**](RedditAppsApi.md#post_reddit_app_by_id) | **POST** /reddit_apps/{reddit_app_id} | Get Refresh Token by reddit app and redditor
[**post_reddit_apps**](RedditAppsApi.md#post_reddit_apps) | **POST** /reddit_apps/ | Create a new Reddit App


# **delete_reddit_app_by_id**
> delete_reddit_app_by_id(reddit_app_id)

Delete a Reddit App by ID

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
reddit_app_id = 56 # int | 

try:
    # Delete a Reddit App by ID
    api_instance.delete_reddit_app_by_id(reddit_app_id)
except APIException as e:
    print("Exception when calling RedditAppsApi->delete_reddit_app_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reddit_app_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reddit_app_by_id**
> RedditApp get_reddit_app_by_id(reddit_app_id)

Get Reddit App details by ID

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
reddit_app_id = 56 # int | 

try:
    # Get Reddit App details by ID
    api_response = api_instance.get_reddit_app_by_id(reddit_app_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling RedditAppsApi->get_reddit_app_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reddit_app_id** | **int**|  | 

### Return type

[**RedditApp**](RedditApp.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reddit_apps**
> list[BaseRedditApp] get_reddit_apps(limit=limit, offset=offset, owner_id=owner_id)

List of Reddit Apps

**PERMISSIONS: At least Active user is required.**   Returns a list of Reddit Apps starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Reddit Apps for other users. Regular users will see their own Reddit Apps.

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
limit = 20 # int | limit a number of items (allowed range is 1-100), default is 20. (optional) (default to 20)
offset = 0 # int | a number of items to skip, default is 0. (optional) (default to 0)
owner_id = 56 # int |  (optional)

try:
    # List of Reddit Apps
    api_response = api_instance.get_reddit_apps(limit=limit, offset=offset, owner_id=owner_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling RedditAppsApi->get_reddit_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit a number of items (allowed range is 1-100), default is 20. | [optional] [default to 20]
 **offset** | **int**| a number of items to skip, default is 0. | [optional] [default to 0]
 **owner_id** | **int**|  | [optional] 

### Return type

[**list[BaseRedditApp]**](BaseRedditApp.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_generate_auth_url**
> options_generate_auth_url(reddit_app_id)

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
reddit_app_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_generate_auth_url(reddit_app_id)
except APIException as e:
    print("Exception when calling RedditAppsApi->options_generate_auth_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reddit_app_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_reddit_app_by_id**
> options_reddit_app_by_id(reddit_app_id)

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
reddit_app_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_reddit_app_by_id(reddit_app_id)
except APIException as e:
    print("Exception when calling RedditAppsApi->options_reddit_app_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reddit_app_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_reddit_apps**
> options_reddit_apps()

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_reddit_apps()
except APIException as e:
    print("Exception when calling RedditAppsApi->options_reddit_apps: %s\n" % e)
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

# **patch_reddit_app_by_id**
> RedditApp patch_reddit_app_by_id(reddit_app_id, body)

Patch reddit_app details by ID

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
reddit_app_id = 56 # int | 
body = [CredentialManager.Body3()] # list[Body3] | 

try:
    # Patch reddit_app details by ID
    api_response = api_instance.patch_reddit_app_by_id(reddit_app_id, body)
    pprint(api_response)
except APIException as e:
    print("Exception when calling RedditAppsApi->patch_reddit_app_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reddit_app_id** | **int**|  | 
 **body** | [**list[Body3]**](Body3.md)|  | 

### Return type

[**RedditApp**](RedditApp.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_generate_auth_url**
> AuthUrl post_generate_auth_url(reddit_app_id, scopes, duration=duration, user_verification_user_id=user_verification_user_id, user_verification_id=user_verification_id)

Generate a reddit auth url

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
reddit_app_id = 56 # int | 
scopes = ['scopes_example'] # list[str] | List of scopes needed for app
duration = 'duration_example' # str | Duration authorization is good for. Options are: `permanent` and `temporary`. Defaults to `permanent`. (optional)
user_verification_user_id = 'user_verification_user_id_example' # str | Specify a User Verification User ID to assoiate with auth url by User ID (optional)
user_verification_id = 56 # int | Specify a User Verification ID to assoiate with auth url by User Verification ID (optional)

try:
    # Generate a reddit auth url
    api_response = api_instance.post_generate_auth_url(reddit_app_id, scopes, duration=duration, user_verification_user_id=user_verification_user_id, user_verification_id=user_verification_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling RedditAppsApi->post_generate_auth_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reddit_app_id** | **int**|  | 
 **scopes** | [**list[str]**](str.md)| List of scopes needed for app | 
 **duration** | **str**| Duration authorization is good for. Options are: &#x60;permanent&#x60; and &#x60;temporary&#x60;. Defaults to &#x60;permanent&#x60;. | [optional] 
 **user_verification_user_id** | **str**| Specify a User Verification User ID to assoiate with auth url by User ID | [optional] 
 **user_verification_id** | **int**| Specify a User Verification ID to assoiate with auth url by User Verification ID | [optional] 

### Return type

[**AuthUrl**](AuthUrl.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reddit_app_by_id**
> RefreshToken post_reddit_app_by_id(reddit_app_id, redditor)

Get Refresh Token by reddit app and redditor

**PERMISSIONS: Owner/Admin may execute this action.**   Only Admins can see Refresh Tokens for other users' Reddit Apps. Regular users will see their own Reddit Apps' Refresh Tokens.

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
reddit_app_id = 56 # int | 
redditor = 'redditor_example' # str | Redditor the Refresh Token is for

try:
    # Get Refresh Token by reddit app and redditor
    api_response = api_instance.post_reddit_app_by_id(reddit_app_id, redditor)
    pprint(api_response)
except APIException as e:
    print("Exception when calling RedditAppsApi->post_reddit_app_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reddit_app_id** | **int**|  | 
 **redditor** | **str**| Redditor the Refresh Token is for | 

### Return type

[**RefreshToken**](RefreshToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reddit_apps**
> RedditApp post_reddit_apps(app_name, client_id, user_agent, app_type, redirect_uri, client_secret=client_secret, short_name=short_name, app_description=app_description, state=state, enabled=enabled, owner_id=owner_id)

Create a new Reddit App

**PERMISSIONS: At least Active user is required.**   Reddit Apps are used for interacting with reddit

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
api_instance = CredentialManager.RedditAppsApi(CredentialManager.ApiClient(config))
app_name = 'app_name_example' # str | 
client_id = 'client_id_example' # str | Client ID of the Reddit App
user_agent = 'user_agent_example' # str | User agent used for requests to Reddit's API
app_type = 'app_type_example' # str | Type of the app. One of `web`, `installed`, or `script`
redirect_uri = 'redirect_uri_example' # str | Redirect URI for Oauth2 flow. Defaults to user set redirect uri
client_secret = 'client_secret_example' # str | Client secret of the Reddit App (optional)
short_name = 'short_name_example' # str | Short name of the Reddit App (optional)
app_description = 'app_description_example' # str | Description of the Reddit App (optional)
state = 'state_example' # str |  (optional)
enabled = true # bool | Allows the app to be used (optional)
owner_id = 56 # int | Owner of the app. Requires Admin to create for other users. (optional)

try:
    # Create a new Reddit App
    api_response = api_instance.post_reddit_apps(app_name, client_id, user_agent, app_type, redirect_uri, client_secret=client_secret, short_name=short_name, app_description=app_description, state=state, enabled=enabled, owner_id=owner_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling RedditAppsApi->post_reddit_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**|  | 
 **client_id** | **str**| Client ID of the Reddit App | 
 **user_agent** | **str**| User agent used for requests to Reddit&#39;s API | 
 **app_type** | **str**| Type of the app. One of &#x60;web&#x60;, &#x60;installed&#x60;, or &#x60;script&#x60; | 
 **redirect_uri** | **str**| Redirect URI for Oauth2 flow. Defaults to user set redirect uri | 
 **client_secret** | **str**| Client secret of the Reddit App | [optional] 
 **short_name** | **str**| Short name of the Reddit App | [optional] 
 **app_description** | **str**| Description of the Reddit App | [optional] 
 **state** | **str**|  | [optional] 
 **enabled** | **bool**| Allows the app to be used | [optional] 
 **owner_id** | **int**| Owner of the app. Requires Admin to create for other users. | [optional] 

### Return type

[**RedditApp**](RedditApp.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

