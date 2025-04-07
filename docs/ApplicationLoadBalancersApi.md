# ionos_cloud_api_v6_client.ApplicationLoadBalancersApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacenters_applicationloadbalancers_delete**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Delete an Application Load Balancer by ID
[**datacenters_applicationloadbalancers_find_by_application_load_balancer_id**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_find_by_application_load_balancer_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Get an Application Load Balancer by ID
[**datacenters_applicationloadbalancers_flowlogs_delete**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Delete an ALB Flow Log by ID
[**datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Get an ALB Flow Log by ID
[**datacenters_applicationloadbalancers_flowlogs_get**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs | Get ALB Flow Logs
[**datacenters_applicationloadbalancers_flowlogs_patch**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Partially Modify an ALB Flow Log by ID
[**datacenters_applicationloadbalancers_flowlogs_post**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs | Create an ALB Flow Log
[**datacenters_applicationloadbalancers_flowlogs_put**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Modify an ALB Flow Log by ID
[**datacenters_applicationloadbalancers_forwardingrules_delete**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Delete an ALB Forwarding Rule by ID
[**datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Get an ALB Forwarding Rule by ID
[**datacenters_applicationloadbalancers_forwardingrules_get**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules | Get ALB Forwarding Rules
[**datacenters_applicationloadbalancers_forwardingrules_patch**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Partially modify an ALB Forwarding Rule by ID
[**datacenters_applicationloadbalancers_forwardingrules_post**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules | Create an ALB Forwarding Rule
[**datacenters_applicationloadbalancers_forwardingrules_put**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Modify an ALB Forwarding Rule by ID
[**datacenters_applicationloadbalancers_get**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers | Get Application Load Balancers
[**datacenters_applicationloadbalancers_patch**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Partially Modify an Application Load Balancer by ID
[**datacenters_applicationloadbalancers_post**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers | Create an Application Load Balancer
[**datacenters_applicationloadbalancers_put**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Modify an Application Load Balancer by ID


# **datacenters_applicationloadbalancers_delete**
> datacenters_applicationloadbalancers_delete(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an Application Load Balancer by ID

Removes the specified Application Load Balancer from the data center.

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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Delete an Application Load Balancer by ID
        api_instance.datacenters_applicationloadbalancers_delete(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
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

# **datacenters_applicationloadbalancers_find_by_application_load_balancer_id**
> ApplicationLoadBalancer datacenters_applicationloadbalancers_find_by_application_load_balancer_id(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get an Application Load Balancer by ID

Retrieves the properties of the specified Application Load Balancer within the data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer import ApplicationLoadBalancer
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get an Application Load Balancer by ID
        api_response = api_instance.datacenters_applicationloadbalancers_find_by_application_load_balancer_id(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_find_by_application_load_balancer_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_find_by_application_load_balancer_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancer**](ApplicationLoadBalancer.md)

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

# **datacenters_applicationloadbalancers_flowlogs_delete**
> datacenters_applicationloadbalancers_flowlogs_delete(datacenter_id, application_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an ALB Flow Log by ID

Deletes the Application Load Balancer flow log specified by its ID.

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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Delete an ALB Flow Log by ID
        api_instance.datacenters_applicationloadbalancers_flowlogs_delete(datacenter_id, application_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **flow_log_id** | **str**| The unique ID of the flow log. | 
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

# **datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id**
> FlowLog datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, application_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get an ALB Flow Log by ID

Retrieves the Application Load Balancer flow log specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.flow_log import FlowLog
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get an ALB Flow Log by ID
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, application_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **flow_log_id** | **str**| The unique ID of the flow log. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**FlowLog**](FlowLog.md)

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

# **datacenters_applicationloadbalancers_flowlogs_get**
> FlowLogs datacenters_applicationloadbalancers_flowlogs_get(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get ALB Flow Logs

Retrieves the flow logs for the specified Application Load Balancer.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.flow_logs import FlowLogs
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get ALB Flow Logs
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_get(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**FlowLogs**](FlowLogs.md)

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

# **datacenters_applicationloadbalancers_flowlogs_patch**
> FlowLog datacenters_applicationloadbalancers_flowlogs_patch(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially Modify an ALB Flow Log by ID

Updates the properties of the Application Load Balancer flow log specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.flow_log import FlowLog
from ionos_cloud_api_v6_client.models.flow_log_properties import FlowLogProperties
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log.
    application_load_balancer_flow_log_properties = ionos_cloud_api_v6_client.FlowLogProperties() # FlowLogProperties | The properties of the ALB flow log to be updated.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Partially Modify an ALB Flow Log by ID
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_patch(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **flow_log_id** | **str**| The unique ID of the flow log. | 
 **application_load_balancer_flow_log_properties** | [**FlowLogProperties**](FlowLogProperties.md)| The properties of the ALB flow log to be updated. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_applicationloadbalancers_flowlogs_post**
> FlowLog datacenters_applicationloadbalancers_flowlogs_post(datacenter_id, application_load_balancer_id, application_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create an ALB Flow Log

Creates a flow log for the Application Load Balancer specified by ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.flow_log import FlowLog
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    application_load_balancer_flow_log = ionos_cloud_api_v6_client.FlowLog() # FlowLog | The flow log to create.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Create an ALB Flow Log
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_post(datacenter_id, application_load_balancer_id, application_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **application_load_balancer_flow_log** | [**FlowLog**](FlowLog.md)| The flow log to create. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**FlowLog**](FlowLog.md)

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

# **datacenters_applicationloadbalancers_flowlogs_put**
> FlowLog datacenters_applicationloadbalancers_flowlogs_put(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify an ALB Flow Log by ID

Modifies the Application Load Balancer flow log specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.flow_log import FlowLog
from ionos_cloud_api_v6_client.models.flow_log_put import FlowLogPut
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log.
    application_load_balancer_flow_log = ionos_cloud_api_v6_client.FlowLogPut() # FlowLogPut | The modified ALB flow log.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Modify an ALB Flow Log by ID
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_put(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_flowlogs_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **flow_log_id** | **str**| The unique ID of the flow log. | 
 **application_load_balancer_flow_log** | [**FlowLogPut**](FlowLogPut.md)| The modified ALB flow log. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_applicationloadbalancers_forwardingrules_delete**
> datacenters_applicationloadbalancers_forwardingrules_delete(datacenter_id, application_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an ALB Forwarding Rule by ID

Deletes the Application Load Balancer forwarding rule specified by its ID.

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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Delete an ALB Forwarding Rule by ID
        api_instance.datacenters_applicationloadbalancers_forwardingrules_delete(datacenter_id, application_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. | 
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

# **datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id**
> ApplicationLoadBalancerForwardingRule datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, application_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get an ALB Forwarding Rule by ID

Retrieves the Application Load Balancer forwarding rule specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rule import ApplicationLoadBalancerForwardingRule
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get an ALB Forwarding Rule by ID
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, application_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancerForwardingRule**](ApplicationLoadBalancerForwardingRule.md)

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

# **datacenters_applicationloadbalancers_forwardingrules_get**
> ApplicationLoadBalancerForwardingRules datacenters_applicationloadbalancers_forwardingrules_get(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get ALB Forwarding Rules

Lists the forwarding rules of the specified Application Load Balancer.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rules import ApplicationLoadBalancerForwardingRules
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get ALB Forwarding Rules
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_get(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancerForwardingRules**](ApplicationLoadBalancerForwardingRules.md)

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

# **datacenters_applicationloadbalancers_forwardingrules_patch**
> ApplicationLoadBalancerForwardingRule datacenters_applicationloadbalancers_forwardingrules_patch(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify an ALB Forwarding Rule by ID

Updates the properties of the Application Load Balancer forwarding rule specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rule import ApplicationLoadBalancerForwardingRule
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rule_properties import ApplicationLoadBalancerForwardingRuleProperties
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    application_load_balancer_forwarding_rule_properties = ionos_cloud_api_v6_client.ApplicationLoadBalancerForwardingRuleProperties() # ApplicationLoadBalancerForwardingRuleProperties | The properties of the forwarding rule to be updated.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Partially modify an ALB Forwarding Rule by ID
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_patch(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. | 
 **application_load_balancer_forwarding_rule_properties** | [**ApplicationLoadBalancerForwardingRuleProperties**](ApplicationLoadBalancerForwardingRuleProperties.md)| The properties of the forwarding rule to be updated. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancerForwardingRule**](ApplicationLoadBalancerForwardingRule.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_applicationloadbalancers_forwardingrules_post**
> ApplicationLoadBalancerForwardingRule datacenters_applicationloadbalancers_forwardingrules_post(datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create an ALB Forwarding Rule

Creates a forwarding rule for the specified Application Load Balancer.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rule import ApplicationLoadBalancerForwardingRule
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    application_load_balancer_forwarding_rule = ionos_cloud_api_v6_client.ApplicationLoadBalancerForwardingRule() # ApplicationLoadBalancerForwardingRule | The forwarding rule to create.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Create an ALB Forwarding Rule
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_post(datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **application_load_balancer_forwarding_rule** | [**ApplicationLoadBalancerForwardingRule**](ApplicationLoadBalancerForwardingRule.md)| The forwarding rule to create. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancerForwardingRule**](ApplicationLoadBalancerForwardingRule.md)

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

# **datacenters_applicationloadbalancers_forwardingrules_put**
> ApplicationLoadBalancerForwardingRule datacenters_applicationloadbalancers_forwardingrules_put(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify an ALB Forwarding Rule by ID

Modifies the Application Load Balancer forwarding rule specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rule import ApplicationLoadBalancerForwardingRule
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rule_put import ApplicationLoadBalancerForwardingRulePut
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    application_load_balancer_forwarding_rule = ionos_cloud_api_v6_client.ApplicationLoadBalancerForwardingRulePut() # ApplicationLoadBalancerForwardingRulePut | The modified ALB forwarding rule.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Modify an ALB Forwarding Rule by ID
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_put(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_forwardingrules_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. | 
 **application_load_balancer_forwarding_rule** | [**ApplicationLoadBalancerForwardingRulePut**](ApplicationLoadBalancerForwardingRulePut.md)| The modified ALB forwarding rule. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancerForwardingRule**](ApplicationLoadBalancerForwardingRule.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_applicationloadbalancers_get**
> ApplicationLoadBalancers datacenters_applicationloadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

Get Application Load Balancers

Lists all Application Load Balancers within a data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancers import ApplicationLoadBalancers
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)
    offset = 0 # int | The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination). (optional) (default to 0)
    limit = 1000 # int | The maximum number of elements to return (use together with offset for pagination). (optional) (default to 1000)

    try:
        # Get Application Load Balancers
        api_response = api_instance.datacenters_applicationloadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 
 **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000]

### Return type

[**ApplicationLoadBalancers**](ApplicationLoadBalancers.md)

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

# **datacenters_applicationloadbalancers_patch**
> ApplicationLoadBalancer datacenters_applicationloadbalancers_patch(datacenter_id, application_load_balancer_id, application_load_balancer_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially Modify an Application Load Balancer by ID

Updates the properties of the specified Application Load Balancer within the data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer import ApplicationLoadBalancer
from ionos_cloud_api_v6_client.models.application_load_balancer_properties import ApplicationLoadBalancerProperties
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    application_load_balancer_properties = ionos_cloud_api_v6_client.ApplicationLoadBalancerProperties() # ApplicationLoadBalancerProperties | The Application Load Balancer properties to be updated.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Partially Modify an Application Load Balancer by ID
        api_response = api_instance.datacenters_applicationloadbalancers_patch(datacenter_id, application_load_balancer_id, application_load_balancer_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **application_load_balancer_properties** | [**ApplicationLoadBalancerProperties**](ApplicationLoadBalancerProperties.md)| The Application Load Balancer properties to be updated. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancer**](ApplicationLoadBalancer.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_applicationloadbalancers_post**
> ApplicationLoadBalancer datacenters_applicationloadbalancers_post(datacenter_id, application_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create an Application Load Balancer

Creates an Application Load Balancer within the data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer import ApplicationLoadBalancer
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer = ionos_cloud_api_v6_client.ApplicationLoadBalancer() # ApplicationLoadBalancer | The Application Load Balancer to create.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Create an Application Load Balancer
        api_response = api_instance.datacenters_applicationloadbalancers_post(datacenter_id, application_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer** | [**ApplicationLoadBalancer**](ApplicationLoadBalancer.md)| The Application Load Balancer to create. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancer**](ApplicationLoadBalancer.md)

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

# **datacenters_applicationloadbalancers_put**
> ApplicationLoadBalancer datacenters_applicationloadbalancers_put(datacenter_id, application_load_balancer_id, application_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify an Application Load Balancer by ID

Modifies the properties of the specified Application Load Balancer within the data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.application_load_balancer import ApplicationLoadBalancer
from ionos_cloud_api_v6_client.models.application_load_balancer_put import ApplicationLoadBalancerPut
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
    api_instance = ionos_cloud_api_v6_client.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    application_load_balancer = ionos_cloud_api_v6_client.ApplicationLoadBalancerPut() # ApplicationLoadBalancerPut | The modified Application Load Balancer.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Modify an Application Load Balancer by ID
        api_response = api_instance.datacenters_applicationloadbalancers_put(datacenter_id, application_load_balancer_id, application_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationLoadBalancersApi->datacenters_applicationloadbalancers_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. | 
 **application_load_balancer** | [**ApplicationLoadBalancerPut**](ApplicationLoadBalancerPut.md)| The modified Application Load Balancer. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**ApplicationLoadBalancer**](ApplicationLoadBalancer.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

