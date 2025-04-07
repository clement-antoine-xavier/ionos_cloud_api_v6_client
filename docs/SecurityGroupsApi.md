# openapi_client.SecurityGroupsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacenters_securitygroups_delete**](SecurityGroupsApi.md#datacenters_securitygroups_delete) | **DELETE** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Delete a Security Group
[**datacenters_securitygroups_find_by_id**](SecurityGroupsApi.md#datacenters_securitygroups_find_by_id) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Retrieve a Security Group
[**datacenters_securitygroups_firewallrules_delete**](SecurityGroupsApi.md#datacenters_securitygroups_firewallrules_delete) | **DELETE** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Remove a Firewall Rule from a Security Group
[**datacenters_securitygroups_firewallrules_post**](SecurityGroupsApi.md#datacenters_securitygroups_firewallrules_post) | **POST** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules | Create Firewall rule to a Security Group
[**datacenters_securitygroups_get**](SecurityGroupsApi.md#datacenters_securitygroups_get) | **GET** /datacenters/{datacenterId}/securitygroups | List Security Groups
[**datacenters_securitygroups_patch**](SecurityGroupsApi.md#datacenters_securitygroups_patch) | **PATCH** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Partially modify Security Group
[**datacenters_securitygroups_post**](SecurityGroupsApi.md#datacenters_securitygroups_post) | **POST** /datacenters/{datacenterId}/securitygroups | Create a Security Group
[**datacenters_securitygroups_put**](SecurityGroupsApi.md#datacenters_securitygroups_put) | **PUT** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Modify Security Group
[**datacenters_securitygroups_rules_find_by_id**](SecurityGroupsApi.md#datacenters_securitygroups_rules_find_by_id) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Retrieve security group rule by id
[**datacenters_securitygroups_rules_get**](SecurityGroupsApi.md#datacenters_securitygroups_rules_get) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules | List Security Group rules
[**datacenters_securitygroups_rules_patch**](SecurityGroupsApi.md#datacenters_securitygroups_rules_patch) | **PATCH** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Partially modify Security Group Rules
[**datacenters_securitygroups_rules_put**](SecurityGroupsApi.md#datacenters_securitygroups_rules_put) | **PUT** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Modify a Security Group Rule
[**datacenters_servers_nics_securitygroups_put**](SecurityGroupsApi.md#datacenters_servers_nics_securitygroups_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/securitygroups | Attach a list of Security Groups to a NIC
[**datacenters_servers_securitygroups_put**](SecurityGroupsApi.md#datacenters_servers_securitygroups_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/securitygroups | Attach a list of Security Groups to a Server


# **datacenters_securitygroups_delete**
> datacenters_securitygroups_delete(datacenter_id, security_group_id, pretty=pretty)

Delete a Security Group

Deletes the specified Security Group.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the Security Group.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)

    try:
        # Delete a Security Group
        api_instance.datacenters_securitygroups_delete(datacenter_id, security_group_id, pretty=pretty)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **security_group_id** | **str**| The unique ID of the Security Group. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]

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
**202** | Accepted. The request has been accepted for processing. |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_find_by_id**
> SecurityGroup datacenters_securitygroups_find_by_id(datacenter_id, security_group_id, pretty=pretty, depth=depth)

Retrieve a Security Group

Retrieves the attributes of a given Security Group.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.security_group import SecurityGroup
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Retrieve a Security Group
        api_response = api_instance.datacenters_securitygroups_find_by_id(datacenter_id, security_group_id, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center | 
 **security_group_id** | **str**| The unique ID of the security group. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**SecurityGroup**](SecurityGroup.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_firewallrules_delete**
> datacenters_securitygroups_firewallrules_delete(datacenter_id, security_group_id, rule_id)

Remove a Firewall Rule from a Security Group

Removes the specific Firewall Rule from the Security Group and delete the Firewall rule

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    rule_id = 'rule_id_example' # str | The unique ID of the firewall rule.

    try:
        # Remove a Firewall Rule from a Security Group
        api_instance.datacenters_securitygroups_firewallrules_delete(datacenter_id, security_group_id, rule_id)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_firewallrules_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center | 
 **security_group_id** | **str**| The unique ID of the security group. | 
 **rule_id** | **str**| The unique ID of the firewall rule. | 

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
**202** | Accepted. The request has been accepted for processing. |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_firewallrules_post**
> FirewallRule datacenters_securitygroups_firewallrules_post(datacenter_id, security_group_id, firewall_rule)

Create Firewall rule to a Security Group

Create one firewall rule and attach it to the existing security group

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.firewall_rule import FirewallRule
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    firewall_rule = openapi_client.FirewallRule() # FirewallRule | The firewall to be attached (or created and attached).

    try:
        # Create Firewall rule to a Security Group
        api_response = api_instance.datacenters_securitygroups_firewallrules_post(datacenter_id, security_group_id, firewall_rule)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_firewallrules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_firewallrules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center | 
 **security_group_id** | **str**| The unique ID of the security group. | 
 **firewall_rule** | [**FirewallRule**](FirewallRule.md)| The firewall to be attached (or created and attached). | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_get**
> SecurityGroups datacenters_securitygroups_get(datacenter_id, pretty=pretty, depth=depth, offset=offset, limit=limit)

List Security Groups

Retrieve a list of available security groups.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.security_groups import SecurityGroups
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)
    offset = 0 # int | The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination). (optional) (default to 0)
    limit = 1000 # int | The maximum number of elements to return (use together with offset for pagination). (optional) (default to 1000)

    try:
        # List Security Groups
        api_response = api_instance.datacenters_securitygroups_get(datacenter_id, pretty=pretty, depth=depth, offset=offset, limit=limit)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]
 **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000]

### Return type

[**SecurityGroups**](SecurityGroups.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_patch**
> SecurityGroup datacenters_securitygroups_patch(datacenter_id, security_group_id, security_group, pretty=pretty, depth=depth)

Partially modify Security Group

Modify the properties of the specified Security Group within the data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.security_group import SecurityGroup
from openapi_client.models.security_group_properties import SecurityGroupProperties
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the Security Group.
    security_group = openapi_client.SecurityGroupProperties() # SecurityGroupProperties | The modified Security Group
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Partially modify Security Group
        api_response = api_instance.datacenters_securitygroups_patch(datacenter_id, security_group_id, security_group, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **security_group_id** | **str**| The unique ID of the Security Group. | 
 **security_group** | [**SecurityGroupProperties**](SecurityGroupProperties.md)| The modified Security Group | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**SecurityGroup**](SecurityGroup.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_post**
> SecurityGroup datacenters_securitygroups_post(datacenter_id, security_group, pretty=pretty, depth=depth)

Create a Security Group

Creates a security group within the data center. This will allow you to define which IP addresses and networks have access to your servers.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.security_group import SecurityGroup
from openapi_client.models.security_group_request import SecurityGroupRequest
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group = openapi_client.SecurityGroupRequest() # SecurityGroupRequest | The security group to be created
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Create a Security Group
        api_response = api_instance.datacenters_securitygroups_post(datacenter_id, security_group, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **security_group** | [**SecurityGroupRequest**](SecurityGroupRequest.md)| The security group to be created | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**SecurityGroup**](SecurityGroup.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. The request has been accepted for processing. |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_put**
> SecurityGroup datacenters_securitygroups_put(datacenter_id, security_group_id, security_group, pretty=pretty, depth=depth)

Modify Security Group

Modify the properties of the specified Security Group within the data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.security_group import SecurityGroup
from openapi_client.models.security_group_request import SecurityGroupRequest
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the Security Group.
    security_group = openapi_client.SecurityGroupRequest() # SecurityGroupRequest | The modified Security Group
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Modify Security Group
        api_response = api_instance.datacenters_securitygroups_put(datacenter_id, security_group_id, security_group, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **security_group_id** | **str**| The unique ID of the Security Group. | 
 **security_group** | [**SecurityGroupRequest**](SecurityGroupRequest.md)| The modified Security Group | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**SecurityGroup**](SecurityGroup.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_rules_find_by_id**
> FirewallRule datacenters_securitygroups_rules_find_by_id(datacenter_id, security_group_id, rule_id, pretty=pretty, depth=depth)

Retrieve security group rule by id

Retrieve the properties of the specified Security Group rule.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.firewall_rule import FirewallRule
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the Security Group.
    rule_id = 'rule_id_example' # str | The unique ID of the Security Group rule.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Retrieve security group rule by id
        api_response = api_instance.datacenters_securitygroups_rules_find_by_id(datacenter_id, security_group_id, rule_id, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_rules_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_rules_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **security_group_id** | **str**| The unique ID of the Security Group. | 
 **rule_id** | **str**| The unique ID of the Security Group rule. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_rules_get**
> FirewallRules datacenters_securitygroups_rules_get(datacenter_id, security_group_id, pretty=pretty, depth=depth, offset=offset, limit=limit)

List Security Group rules

List all rules for the specified Security Group.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.firewall_rules import FirewallRules
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)
    offset = 0 # int | The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination). (optional) (default to 0)
    limit = 1000 # int | The maximum number of elements to return (use together with offset for pagination). (optional) (default to 1000)

    try:
        # List Security Group rules
        api_response = api_instance.datacenters_securitygroups_rules_get(datacenter_id, security_group_id, pretty=pretty, depth=depth, offset=offset, limit=limit)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_rules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **security_group_id** | **str**| The unique ID of the security group. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]
 **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000]

### Return type

[**FirewallRules**](FirewallRules.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_rules_patch**
> FirewallRule datacenters_securitygroups_rules_patch(datacenter_id, security_group_id, rule_id, rule, pretty=pretty, depth=depth)

Partially modify Security Group Rules

Update the properties of the specified Security Group rule.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.firewall_rule import FirewallRule
from openapi_client.models.firewallrule_properties import FirewallruleProperties
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    rule_id = 'rule_id_example' # str | The unique ID of the Security Group Rule.
    rule = openapi_client.FirewallruleProperties() # FirewallruleProperties | The properties of the Security Group Rule to be updated.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Partially modify Security Group Rules
        api_response = api_instance.datacenters_securitygroups_rules_patch(datacenter_id, security_group_id, rule_id, rule, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_rules_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_rules_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **security_group_id** | **str**| The unique ID of the security group. | 
 **rule_id** | **str**| The unique ID of the Security Group Rule. | 
 **rule** | [**FirewallruleProperties**](FirewallruleProperties.md)| The properties of the Security Group Rule to be updated. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_securitygroups_rules_put**
> FirewallRule datacenters_securitygroups_rules_put(datacenter_id, security_group_id, rule_id, rule, pretty=pretty, depth=depth)

Modify a Security Group Rule

Modifies the properties of the specified Security Group Rule.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.firewall_rule import FirewallRule
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    rule_id = 'rule_id_example' # str | The unique ID of the Security Group Rule.
    rule = openapi_client.FirewallRule() # FirewallRule | The modified Security Group Rule.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Modify a Security Group Rule
        api_response = api_instance.datacenters_securitygroups_rules_put(datacenter_id, security_group_id, rule_id, rule, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_securitygroups_rules_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_securitygroups_rules_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **security_group_id** | **str**| The unique ID of the security group. | 
 **rule_id** | **str**| The unique ID of the Security Group Rule. | 
 **rule** | [**FirewallRule**](FirewallRule.md)| The modified Security Group Rule. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_servers_nics_securitygroups_put**
> SecurityGroups datacenters_servers_nics_securitygroups_put(datacenter_id, server_id, nic_id, securitygroups, pretty=pretty, depth=depth)

Attach a list of Security Groups to a NIC

Updating the list of Security Groups attached to an existing NIC specified by its ID.  Security Groups should already exist as part of the datacenter.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.list_of_ids import ListOfIds
from openapi_client.models.security_groups import SecurityGroups
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    nic_id = 'nic_id_example' # str | The unique ID of the server.
    securitygroups = openapi_client.ListOfIds() # ListOfIds | The list of NIC attached Security Groups IDs.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Attach a list of Security Groups to a NIC
        api_response = api_instance.datacenters_servers_nics_securitygroups_put(datacenter_id, server_id, nic_id, securitygroups, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_servers_nics_securitygroups_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_servers_nics_securitygroups_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **nic_id** | **str**| The unique ID of the server. | 
 **securitygroups** | [**ListOfIds**](ListOfIds.md)| The list of NIC attached Security Groups IDs. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**SecurityGroups**](SecurityGroups.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_servers_securitygroups_put**
> SecurityGroups datacenters_servers_securitygroups_put(datacenter_id, server_id, securitygroups, pretty=pretty, depth=depth)

Attach a list of Security Groups to a Server

Updating the list of Security Groups attached to an existing server specified by its ID.  Security Groups should already exist as part of the datacenter.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.list_of_ids import ListOfIds
from openapi_client.models.security_groups import SecurityGroups
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
    api_instance = openapi_client.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    securitygroups = openapi_client.ListOfIds() # ListOfIds | The list of server attached Security Groups IDs.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on (optional) (default to 0)

    try:
        # Attach a list of Security Groups to a Server
        api_response = api_instance.datacenters_servers_securitygroups_put(datacenter_id, server_id, securitygroups, pretty=pretty, depth=depth)
        print("The response of SecurityGroupsApi->datacenters_servers_securitygroups_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityGroupsApi->datacenters_servers_securitygroups_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **securitygroups** | [**ListOfIds**](ListOfIds.md)| The list of server attached Security Groups IDs. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0]

### Return type

[**SecurityGroups**](SecurityGroups.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  * Location - Callback URL to poll async operation status. <br>  |
**0** | Any erroneous status code:   400 (parse error),   401 (auth error),   402 (trial access),   403 (insufficient privileges),   404 (not found),   405 (unsupported HTTP method),   415 (unsupported content type),   422 (validation error),   429 (request rate limit exceeded),   500 (server error),   or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

