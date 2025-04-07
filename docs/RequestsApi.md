# openapi_client.RequestsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requests_find_by_id**](RequestsApi.md#requests_find_by_id) | **GET** /requests/{requestId} | Retrieve requests
[**requests_get**](RequestsApi.md#requests_get) | **GET** /requests | List requests
[**requests_status_get**](RequestsApi.md#requests_status_get) | **GET** /requests/{requestId}/status | Retrieve request status


# **requests_find_by_id**
> Request requests_find_by_id(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve requests

Retrieve the properties of the specified request.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.request import Request
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RequestsApi(api_client)
    request_id = 'request_id_example' # str | The unique ID of the request.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Retrieve requests
        api_response = api_instance.requests_find_by_id(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of RequestsApi->requests_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The unique ID of the request. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Request**](Request.md)

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

# **requests_get**
> Requests requests_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, filter_status=filter_status, filter_created_after=filter_created_after, filter_created_before=filter_created_before, filter_created_date=filter_created_date, filter_created_by=filter_created_by, filter_etag=filter_etag, filter_request_status=filter_request_status, filter_method=filter_method, filter_headers=filter_headers, filter_body=filter_body, filter_url=filter_url, offset=offset, limit=limit)

List requests

List all API requests.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.requests import Requests
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RequestsApi(api_client)
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)
    filter_status = 'filter_status_example' # str | Filter the list by request status [QUEUED, RUNNING, DONE, FAILED]. Filter is not affected by the depth query parameter. (optional)
    filter_created_after = 'filter_created_after_example' # str | Filter the list to only include the requests created after the date, specified in the yyyy-MM-dd HH:mm:ss format. Filter is not affected by the depth query parameter. (optional)
    filter_created_before = 'filter_created_before_example' # str | Filter the list to only include the requests created before the date, specified in the yyyy-MM-dd HH:mm:ss format. Filter is not affected by the depth query parameter. (optional)
    filter_created_date = 'filter_created_date_example' # str | Filter the list to only include the requests that contain the createdDate, specified in the yyyy-MM-dd HH:mm:ss format. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. (optional)
    filter_created_by = 'filter_created_by_example' # str | Filter the list to only include the requests that contain the createdBy, specified in the yyyy-MM-dd HH:mm:ss format. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. (optional)
    filter_etag = 'filter_etag_example' # str | Filter the list to only include the requests that contain the specified etag. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. (optional)
    filter_request_status = 'filter_request_status_example' # str | Filter the list to only include the requests that contain the specified requestStatus. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. (optional)
    filter_method = 'filter_method_example' # str | Filter the list to only include the requests that contain the specified method. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. (optional)
    filter_headers = 'filter_headers_example' # str | Filter the list to only include the requests that contain the specified headers. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. (optional)
    filter_body = 'filter_body_example' # str | Filter the list to only include the requests that contain the specified body. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. (optional)
    filter_url = 'filter_url_example' # str | Filter the list to only include the requests that contain the specified URL. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. (optional)
    offset = 0 # int | The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination). (optional) (default to 0)
    limit = 1000 # int | The maximum number of elements to return (use together with offset for pagination). (optional) (default to 1000)

    try:
        # List requests
        api_response = api_instance.requests_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, filter_status=filter_status, filter_created_after=filter_created_after, filter_created_before=filter_created_before, filter_created_date=filter_created_date, filter_created_by=filter_created_by, filter_etag=filter_etag, filter_request_status=filter_request_status, filter_method=filter_method, filter_headers=filter_headers, filter_body=filter_body, filter_url=filter_url, offset=offset, limit=limit)
        print("The response of RequestsApi->requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 
 **filter_status** | **str**| Filter the list by request status [QUEUED, RUNNING, DONE, FAILED]. Filter is not affected by the depth query parameter. | [optional] 
 **filter_created_after** | **str**| Filter the list to only include the requests created after the date, specified in the yyyy-MM-dd HH:mm:ss format. Filter is not affected by the depth query parameter. | [optional] 
 **filter_created_before** | **str**| Filter the list to only include the requests created before the date, specified in the yyyy-MM-dd HH:mm:ss format. Filter is not affected by the depth query parameter. | [optional] 
 **filter_created_date** | **str**| Filter the list to only include the requests that contain the createdDate, specified in the yyyy-MM-dd HH:mm:ss format. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional] 
 **filter_created_by** | **str**| Filter the list to only include the requests that contain the createdBy, specified in the yyyy-MM-dd HH:mm:ss format. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional] 
 **filter_etag** | **str**| Filter the list to only include the requests that contain the specified etag. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional] 
 **filter_request_status** | **str**| Filter the list to only include the requests that contain the specified requestStatus. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional] 
 **filter_method** | **str**| Filter the list to only include the requests that contain the specified method. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional] 
 **filter_headers** | **str**| Filter the list to only include the requests that contain the specified headers. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional] 
 **filter_body** | **str**| Filter the list to only include the requests that contain the specified body. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional] 
 **filter_url** | **str**| Filter the list to only include the requests that contain the specified URL. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional] 
 **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000]

### Return type

[**Requests**](Requests.md)

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

# **requests_status_get**
> RequestStatus requests_status_get(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve request status

Retrieve the status of the specified request.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.request_status import RequestStatus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.ionos.com/cloudapi/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RequestsApi(api_client)
    request_id = 'request_id_example' # str | The unique ID of the request.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Retrieve request status
        api_response = api_instance.requests_status_get(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of RequestsApi->requests_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The unique ID of the request. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**RequestStatus**](RequestStatus.md)

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

