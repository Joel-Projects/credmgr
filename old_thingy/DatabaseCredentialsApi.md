# CredentialManager.DatabaseCredentialsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_database_credential_by_id**](DatabaseCredentialsApi.md#delete_database_credential_by_id) | **DELETE** /database_credentials/{database_credential_id} | Delete a Database Credential by ID
[**get_database_credential_by_id**](DatabaseCredentialsApi.md#get_database_credential_by_id) | **GET** /database_credentials/{database_credential_id} | Get Database Credential details by ID
[**get_database_credentials**](DatabaseCredentialsApi.md#get_database_credentials) | **GET** /database_credentials/ | List of Database Credentials
[**options_database_credential_by_id**](DatabaseCredentialsApi.md#options_database_credential_by_id) | **OPTIONS** /database_credentials/{database_credential_id} | Check which methods are allowed
[**options_database_credentials**](DatabaseCredentialsApi.md#options_database_credentials) | **OPTIONS** /database_credentials/ | Check which methods are allowed
[**patch_database_credential_by_id**](DatabaseCredentialsApi.md#patch_database_credential_by_id) | **PATCH** /database_credentials/{database_credential_id} | Patch database_credential details by ID
[**post_database_credentials**](DatabaseCredentialsApi.md#post_database_credentials) | **POST** /database_credentials/ | Create a new Database Credential


# **delete_database_credential_by_id**
> delete_database_credential_by_id(database_credential_id)

Delete a Database Credential by ID

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
api_instance = CredentialManager.DatabaseCredentialsApi(CredentialManager.ApiClient(config))
database_credential_id = 56 # int | 

try:
    # Delete a Database Credential by ID
    api_instance.delete_database_credential_by_id(database_credential_id)
except APIException as e:
    print("Exception when calling DatabaseCredentialsApi->delete_database_credential_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_credential_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_credential_by_id**
> DatabaseCredential get_database_credential_by_id(database_credential_id)

Get Database Credential details by ID

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
api_instance = CredentialManager.DatabaseCredentialsApi(CredentialManager.ApiClient(config))
database_credential_id = 56 # int | 

try:
    # Get Database Credential details by ID
    api_response = api_instance.get_database_credential_by_id(database_credential_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling DatabaseCredentialsApi->get_database_credential_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_credential_id** | **int**|  | 

### Return type

[**DatabaseCredential**](DatabaseCredential.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_credentials**
> list[BaseDatabaseCredential] get_database_credentials(limit=limit, offset=offset, owner_id=owner_id)

List of Database Credentials

**PERMISSIONS: At least Active user is required.**   Returns a list of Database Credentials starting from ``offset`` limited by ``limit`` parameter.  Only Admins can specify ``owner`` to see Database Credentials for other users. Regular users will see their own Database Credentials.

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
api_instance = CredentialManager.DatabaseCredentialsApi(CredentialManager.ApiClient(config))
limit = 20 # int | limit a number of items (allowed range is 1-100), default is 20. (optional) (default to 20)
offset = 0 # int | a number of items to skip, default is 0. (optional) (default to 0)
owner_id = 56 # int |  (optional)

try:
    # List of Database Credentials
    api_response = api_instance.get_database_credentials(limit=limit, offset=offset, owner_id=owner_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling DatabaseCredentialsApi->get_database_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit a number of items (allowed range is 1-100), default is 20. | [optional] [default to 20]
 **offset** | **int**| a number of items to skip, default is 0. | [optional] [default to 0]
 **owner_id** | **int**|  | [optional] 

### Return type

[**list[BaseDatabaseCredential]**](BaseDatabaseCredential.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_database_credential_by_id**
> options_database_credential_by_id(database_credential_id)

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
api_instance = CredentialManager.DatabaseCredentialsApi(CredentialManager.ApiClient(config))
database_credential_id = 56 # int | 

try:
    # Check which methods are allowed
    api_instance.options_database_credential_by_id(database_credential_id)
except APIException as e:
    print("Exception when calling DatabaseCredentialsApi->options_database_credential_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_credential_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_database_credentials**
> options_database_credentials()

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
api_instance = CredentialManager.DatabaseCredentialsApi(CredentialManager.ApiClient(config))

try:
    # Check which methods are allowed
    api_instance.options_database_credentials()
except APIException as e:
    print("Exception when calling DatabaseCredentialsApi->options_database_credentials: %s\n" % e)
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

# **patch_database_credential_by_id**
> DatabaseCredential patch_database_credential_by_id(database_credential_id, body)

Patch database_credential details by ID

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
api_instance = CredentialManager.DatabaseCredentialsApi(CredentialManager.ApiClient(config))
database_credential_id = 56 # int | 
body = [CredentialManager.Body2()] # list[Body2] | 

try:
    # Patch database_credential details by ID
    api_response = api_instance.patch_database_credential_by_id(database_credential_id, body)
    pprint(api_response)
except APIException as e:
    print("Exception when calling DatabaseCredentialsApi->patch_database_credential_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_credential_id** | **int**|  | 
 **body** | [**list[Body2]**](Body2.md)|  | 

### Return type

[**DatabaseCredential**](DatabaseCredential.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_database_credentials**
> DatabaseCredential post_database_credentials(app_name, database_username, database_host, database_flavor, database=database, owner_id=owner_id)

Create a new Database Credential

**PERMISSIONS: At least Active user is required.**   Database Credentials are used for logging and error reporting in applications

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
api_instance = CredentialManager.DatabaseCredentialsApi(CredentialManager.ApiClient(config))
app_name = 'app_name_example' # str | Name of the Database Credential
database_username = 'database_username_example' # str | Username to use to connect to the database
database_host = 'database_host_example' # str | Database server address, defaults to `localhost`
database_flavor = 'database_flavor_example' # str | Type of database, defaults to `postgres`
database = 'database_example' # str | Working database to use, defaults to `postgres` (optional)
owner_id = 56 # int | Owner of the app. Requires Admin to create for other users. (optional)

try:
    # Create a new Database Credential
    api_response = api_instance.post_database_credentials(app_name, database_username, database_host, database_flavor, database=database, owner_id=owner_id)
    pprint(api_response)
except APIException as e:
    print("Exception when calling DatabaseCredentialsApi->post_database_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Name of the Database Credential | 
 **database_username** | **str**| Username to use to connect to the database | 
 **database_host** | **str**| Database server address, defaults to &#x60;localhost&#x60; | 
 **database_flavor** | **str**| Type of database, defaults to &#x60;postgres&#x60; | 
 **database** | **str**| Working database to use, defaults to &#x60;postgres&#x60; | [optional] 
 **owner_id** | **int**| Owner of the app. Requires Admin to create for other users. | [optional] 

### Return type

[**DatabaseCredential**](DatabaseCredential.md)

### Authorization

[apiKey](../README.md#apiKey), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

