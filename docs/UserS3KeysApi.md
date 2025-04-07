# ionos_cloud_api_v6_client.UserS3KeysApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**um_users_s3keys_delete**](UserS3KeysApi.md#um_users_s3keys_delete) | **DELETE** /um/users/{userId}/s3keys/{keyId} | Delete Object storage keys
[**um_users_s3keys_find_by_key_id**](UserS3KeysApi.md#um_users_s3keys_find_by_key_id) | **GET** /um/users/{userId}/s3keys/{keyId} | Retrieve user Object storage keys by key ID
[**um_users_s3keys_get**](UserS3KeysApi.md#um_users_s3keys_get) | **GET** /um/users/{userId}/s3keys | List user Object storage keys
[**um_users_s3keys_post**](UserS3KeysApi.md#um_users_s3keys_post) | **POST** /um/users/{userId}/s3keys | Create user Object storage keys
[**um_users_s3keys_put**](UserS3KeysApi.md#um_users_s3keys_put) | **PUT** /um/users/{userId}/s3keys/{keyId} | Modify a Object storage Key by Key ID
[**um_users_s3ssourl_get**](UserS3KeysApi.md#um_users_s3ssourl_get) | **GET** /um/users/{userId}/s3ssourl | Retrieve Object storage single sign-on URLs


# **um_users_s3keys_delete**
> um_users_s3keys_delete(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete Object storage keys

Delete the specified user Object storage key.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_api_v6_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = ionos_cloud_api_v6_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with ionos_cloud_api_v6_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_api_v6_client.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    key_id = 'key_id_example' # str | The unique ID of the Object storage key.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Delete Object storage keys
        api_instance.um_users_s3keys_delete(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling UserS3KeysApi->um_users_s3keys_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique ID of the user. | 
 **key_id** | **str**| The unique ID of the Object storage key. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **um_users_s3keys_find_by_key_id**
> S3Key um_users_s3keys_find_by_key_id(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve user Object storage keys by key ID

Retrieve the specified user Object storage key. The user ID is in the response body when the user is created, and in the list of the users, returned by GET. The key ID is in the response body when the Object storage key is created, and in the list of all user Object storage keys, returned by GET.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.s3_key import S3Key
from ionos_cloud_api_v6_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_api_v6_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = ionos_cloud_api_v6_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with ionos_cloud_api_v6_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_api_v6_client.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    key_id = 'key_id_example' # str | The unique ID of the Object storage key.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Retrieve user Object storage keys by key ID
        api_response = api_instance.um_users_s3keys_find_by_key_id(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of UserS3KeysApi->um_users_s3keys_find_by_key_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserS3KeysApi->um_users_s3keys_find_by_key_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique ID of the user. | 
 **key_id** | **str**| The unique ID of the Object storage key. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**S3Key**](S3Key.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **um_users_s3keys_get**
> S3Keys um_users_s3keys_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List user Object storage keys

List Object storage keys by user ID. The user ID is in the response body when the user is created, and in the list of the users, returned by GET.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.s3_keys import S3Keys
from ionos_cloud_api_v6_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_api_v6_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = ionos_cloud_api_v6_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with ionos_cloud_api_v6_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_api_v6_client.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # List user Object storage keys
        api_response = api_instance.um_users_s3keys_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of UserS3KeysApi->um_users_s3keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserS3KeysApi->um_users_s3keys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique ID of the user. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**S3Keys**](S3Keys.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **um_users_s3keys_post**
> S3Key um_users_s3keys_post(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create user Object storage keys

Create an Object storage key for the specified user. The user ID is in the response body when the user is created, and in the list of the users, returned by GET. A maximum of five keys per user can be generated.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.s3_key import S3Key
from ionos_cloud_api_v6_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_api_v6_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = ionos_cloud_api_v6_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with ionos_cloud_api_v6_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_api_v6_client.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Create user Object storage keys
        api_response = api_instance.um_users_s3keys_post(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of UserS3KeysApi->um_users_s3keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserS3KeysApi->um_users_s3keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique ID of the user. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**S3Key**](S3Key.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **um_users_s3keys_put**
> S3Key um_users_s3keys_put(user_id, key_id, s3_key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Object storage Key by Key ID

Enables or disables the specified user Object storage key.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.s3_key import S3Key
from ionos_cloud_api_v6_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_api_v6_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = ionos_cloud_api_v6_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with ionos_cloud_api_v6_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_api_v6_client.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    key_id = 'key_id_example' # str | The unique ID of the Object storage key.
    s3_key = ionos_cloud_api_v6_client.S3Key() # S3Key | The modified Object storage key.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Modify a Object storage Key by Key ID
        api_response = api_instance.um_users_s3keys_put(user_id, key_id, s3_key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of UserS3KeysApi->um_users_s3keys_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserS3KeysApi->um_users_s3keys_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique ID of the user. | 
 **key_id** | **str**| The unique ID of the Object storage key. | 
 **s3_key** | [**S3Key**](S3Key.md)| The modified Object storage key. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**S3Key**](S3Key.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **um_users_s3ssourl_get**
> S3ObjectStorageSSO um_users_s3ssourl_get(user_id, pretty=pretty, x_contract_number=x_contract_number)

Retrieve Object storage single sign-on URLs

Retrieve Ionos Object Storage single sign-on URLs for the the specified user. The user ID is in the response body when the user is created, and in the list of the users, returned by GET.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.s3_object_storage_sso import S3ObjectStorageSSO
from ionos_cloud_api_v6_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_api_v6_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = ionos_cloud_api_v6_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with ionos_cloud_api_v6_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_api_v6_client.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Retrieve Object storage single sign-on URLs
        api_response = api_instance.um_users_s3ssourl_get(user_id, pretty=pretty, x_contract_number=x_contract_number)
        print("The response of UserS3KeysApi->um_users_s3ssourl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserS3KeysApi->um_users_s3ssourl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The unique ID of the user. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**S3ObjectStorageSSO**](S3ObjectStorageSSO.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

