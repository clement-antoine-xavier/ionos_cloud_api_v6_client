# ionos_cloud_api_v6_client.ServersApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacenters_servers_cdroms_delete**](ServersApi.md#datacenters_servers_cdroms_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/cdroms/{cdromId} | Detach a CD-ROM by ID
[**datacenters_servers_cdroms_find_by_id**](ServersApi.md#datacenters_servers_cdroms_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/cdroms/{cdromId} | Get Attached CD-ROM by ID
[**datacenters_servers_cdroms_get**](ServersApi.md#datacenters_servers_cdroms_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/cdroms | Get Attached CD-ROMs 
[**datacenters_servers_cdroms_post**](ServersApi.md#datacenters_servers_cdroms_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/cdroms | Attach a CD-ROM
[**datacenters_servers_delete**](ServersApi.md#datacenters_servers_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId} | Delete servers
[**datacenters_servers_find_by_id**](ServersApi.md#datacenters_servers_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId} | Retrieve servers by ID
[**datacenters_servers_get**](ServersApi.md#datacenters_servers_get) | **GET** /datacenters/{datacenterId}/servers | List servers 
[**datacenters_servers_patch**](ServersApi.md#datacenters_servers_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId} | Partially modify servers
[**datacenters_servers_post**](ServersApi.md#datacenters_servers_post) | **POST** /datacenters/{datacenterId}/servers | Create a Server
[**datacenters_servers_put**](ServersApi.md#datacenters_servers_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId} | Modify a Server by ID
[**datacenters_servers_reboot_post**](ServersApi.md#datacenters_servers_reboot_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/reboot | Reboot servers
[**datacenters_servers_remote_console_get**](ServersApi.md#datacenters_servers_remote_console_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/remoteconsole | Get Remote Console link
[**datacenters_servers_resume_post**](ServersApi.md#datacenters_servers_resume_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/resume | Resume a Cube Server by ID
[**datacenters_servers_start_post**](ServersApi.md#datacenters_servers_start_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/start | Start an Enterprise Server by ID
[**datacenters_servers_stop_post**](ServersApi.md#datacenters_servers_stop_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/stop | Stop an Enterprise Server by ID
[**datacenters_servers_suspend_post**](ServersApi.md#datacenters_servers_suspend_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/suspend | Suspend a Cube Server by ID
[**datacenters_servers_token_get**](ServersApi.md#datacenters_servers_token_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/token | Get JSON Web Token
[**datacenters_servers_upgrade_post**](ServersApi.md#datacenters_servers_upgrade_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/upgrade | Upgrade a Server by ID
[**datacenters_servers_volumes_delete**](ServersApi.md#datacenters_servers_volumes_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/volumes/{volumeId} | Detach a Volume by ID
[**datacenters_servers_volumes_find_by_id**](ServersApi.md#datacenters_servers_volumes_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/volumes/{volumeId} | Get Attached Volume by ID
[**datacenters_servers_volumes_get**](ServersApi.md#datacenters_servers_volumes_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/volumes | Get Attached Volumes
[**datacenters_servers_volumes_post**](ServersApi.md#datacenters_servers_volumes_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/volumes | Attach a Volume to a Server


# **datacenters_servers_cdroms_delete**
> datacenters_servers_cdroms_delete(datacenter_id, server_id, cdrom_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Detach a CD-ROM by ID

Detachs the specified CD-ROM from the server.

Detaching a CD-ROM deletes the CD-ROM. The image will not be deleted.

Note that detaching a CD-ROM leads to a reset of the server.

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    cdrom_id = 'cdrom_id_example' # str | The unique ID of the CD-ROM.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Detach a CD-ROM by ID
        api_instance.datacenters_servers_cdroms_delete(datacenter_id, server_id, cdrom_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_cdroms_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **cdrom_id** | **str**| The unique ID of the CD-ROM. | 
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

# **datacenters_servers_cdroms_find_by_id**
> Image datacenters_servers_cdroms_find_by_id(datacenter_id, server_id, cdrom_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Attached CD-ROM by ID

Retrieves the properties of the CD-ROM attached to the specified server.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.image import Image
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    cdrom_id = 'cdrom_id_example' # str | The unique ID of the CD-ROM.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get Attached CD-ROM by ID
        api_response = api_instance.datacenters_servers_cdroms_find_by_id(datacenter_id, server_id, cdrom_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_cdroms_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_cdroms_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **cdrom_id** | **str**| The unique ID of the CD-ROM. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Image**](Image.md)

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

# **datacenters_servers_cdroms_get**
> Cdroms datacenters_servers_cdroms_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

Get Attached CD-ROMs 

Lists all CD-ROMs attached to the specified server.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.cdroms import Cdroms
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)
    offset = 0 # int | The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination). (optional) (default to 0)
    limit = 1000 # int | The maximum number of elements to return (use together with offset for pagination). (optional) (default to 1000)

    try:
        # Get Attached CD-ROMs 
        api_response = api_instance.datacenters_servers_cdroms_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        print("The response of ServersApi->datacenters_servers_cdroms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_cdroms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 
 **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000]

### Return type

[**Cdroms**](Cdroms.md)

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

# **datacenters_servers_cdroms_post**
> Image datacenters_servers_cdroms_post(datacenter_id, server_id, cdrom, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Attach a CD-ROM

Attachs a CD-ROM to an existing server specified by its ID. 

CD-ROMs cannot be created stand-alone like volumes. They are either attached to a server or do not exist. They always have an ISO-Image associated; empty CD-ROMs can not be provisioned. It is possible to attach up to two CD-ROMs to the same server. 

Note that attaching a CD-ROM leads to a reset of the server.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.image import Image
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    cdrom = ionos_cloud_api_v6_client.Image() # Image | The CD-ROM to be attached.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Attach a CD-ROM
        api_response = api_instance.datacenters_servers_cdroms_post(datacenter_id, server_id, cdrom, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_cdroms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_cdroms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **cdrom** | [**Image**](Image.md)| The CD-ROM to be attached. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Image**](Image.md)

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

# **datacenters_servers_delete**
> datacenters_servers_delete(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, delete_volumes=delete_volumes)

Delete servers

Delete the specified server in your data center. The attached storage volumes will also be removed if the query parameter is set to true otherwise a separate API call must be made for these actions.

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)
    delete_volumes = True # bool | If true, all attached storage volumes will also be deleted. (optional)

    try:
        # Delete servers
        api_instance.datacenters_servers_delete(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, delete_volumes=delete_volumes)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 
 **delete_volumes** | **bool**| If true, all attached storage volumes will also be deleted. | [optional] 

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

# **datacenters_servers_find_by_id**
> Server datacenters_servers_find_by_id(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve servers by ID

Retrieve information about the specified server within the data center, such as its configuration, provisioning status, and so on.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.server import Server
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Retrieve servers by ID
        api_response = api_instance.datacenters_servers_find_by_id(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Server**](Server.md)

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

# **datacenters_servers_get**
> Servers datacenters_servers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List servers 

List all servers within the data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.servers import Servers
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)
    offset = 0 # int | The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination). (optional) (default to 0)
    limit = 1000 # int | The maximum number of elements to return (use together with offset for pagination). (optional) (default to 1000)

    try:
        # List servers 
        api_response = api_instance.datacenters_servers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        print("The response of ServersApi->datacenters_servers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_get: %s\n" % e)
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

[**Servers**](Servers.md)

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

# **datacenters_servers_patch**
> Server datacenters_servers_patch(datacenter_id, server_id, server, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify servers

Update the properties of the specified server within the data center.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.server import Server
from ionos_cloud_api_v6_client.models.server_properties import ServerProperties
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    server = ionos_cloud_api_v6_client.ServerProperties() # ServerProperties | The properties of the server to be updated.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Partially modify servers
        api_response = api_instance.datacenters_servers_patch(datacenter_id, server_id, server, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **server** | [**ServerProperties**](ServerProperties.md)| The properties of the server to be updated. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Server**](Server.md)

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

# **datacenters_servers_post**
> Server datacenters_servers_post(datacenter_id, server, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Server

Creates a server within the specified data center. You can also use this request to configure the boot volumes and connect to existing LANs at the same time.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.server import Server
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server = ionos_cloud_api_v6_client.Server() # Server | The server to create.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Create a Server
        api_response = api_instance.datacenters_servers_post(datacenter_id, server, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server** | [**Server**](Server.md)| The server to create. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Server**](Server.md)

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

# **datacenters_servers_put**
> Server datacenters_servers_put(datacenter_id, server_id, server, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Server by ID

Modifies the properties of the specified server within the data center.

Starting with v5, the 'allowReboot' attribute is retired; while previously required for changing certain server properties, this behavior is now implicit, and the backend will perform this automatically. For example, in earlier versions, when the CPU family is changed, 'allowReboot' had to be set to 'true'; this is no longer required, the reboot will be performed automatically.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.server import Server
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    server = ionos_cloud_api_v6_client.Server() # Server | The modified server
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Modify a Server by ID
        api_response = api_instance.datacenters_servers_put(datacenter_id, server_id, server, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **server** | [**Server**](Server.md)| The modified server | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Server**](Server.md)

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

# **datacenters_servers_reboot_post**
> datacenters_servers_reboot_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Reboot servers

Force a hard reboot of the specified server within the data center. Don't use this method if you wish to reboot gracefully. This is an equivalent of powering down a computer and turning it back on.

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Reboot servers
        api_instance.datacenters_servers_reboot_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_reboot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
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

# **datacenters_servers_remote_console_get**
> RemoteConsoleUrl datacenters_servers_remote_console_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Remote Console link

Retrieve a link with a JSON Web Token for accessing the server's Remote Console.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.remote_console_url import RemoteConsoleUrl
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get Remote Console link
        api_response = api_instance.datacenters_servers_remote_console_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_remote_console_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_remote_console_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**RemoteConsoleUrl**](RemoteConsoleUrl.md)

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

# **datacenters_servers_resume_post**
> datacenters_servers_resume_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Resume a Cube Server by ID

Resumes a suspended Cube Server specified by its ID.

Since the suspended instance was not deleted the allocated resources continue to be billed. You can perform this operation only for Cube Servers.

To check the status of the request, you can use the 'Location' HTTP header in the response (see 'Requests' for more information).

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Resume a Cube Server by ID
        api_instance.datacenters_servers_resume_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
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

# **datacenters_servers_start_post**
> datacenters_servers_start_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Start an Enterprise Server by ID

Starts the Enterprise Server specified by its ID.

>Note that you cannot use this method to start a Cube Server.

By starting the Enterprise Server, cores and RAM are provisioned, and the billing continues.

If the server's public IPv4 address has been deallocated, a new IPv4 address will be assigned. IPv6 blocks and addresses will remain unchanged when stopping and starting a server.

To check the status of the request, you can use the 'Location' HTTP header in the response (see 'Requests' for more information).

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Start an Enterprise Server by ID
        api_instance.datacenters_servers_start_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
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

# **datacenters_servers_stop_post**
> datacenters_servers_stop_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Stop an Enterprise Server by ID

Stops the Enterprise Server specified by its ID. 

>Note that you cannot use this method to stop a Cube Server.

 By stopping the Enterprise Server, cores and RAM are freed and no longer charged.

Public IPv4 IPs that are not reserved are returned to the IPv4 pool. IPv6 blocks and addresses will remain unchanged when stopping and starting a server.

To check the status of the request, you can use the 'Location' HTTP header in the response (see 'Requests' for more information).

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Stop an Enterprise Server by ID
        api_instance.datacenters_servers_stop_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
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

# **datacenters_servers_suspend_post**
> datacenters_servers_suspend_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Suspend a Cube Server by ID

Suspends the specified Cubes instance within the data center. 

The instance is not deleted and allocated resources continue to be billed. You can perform this operation only for Cube Servers.

To check the status of the request, you can use the 'Location' HTTP header in the response (see 'Requests' for more information).

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Suspend a Cube Server by ID
        api_instance.datacenters_servers_suspend_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_suspend_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
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

# **datacenters_servers_token_get**
> Token datacenters_servers_token_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get JSON Web Token

Retrieve a JSON Web Token from the server for use in login operations (such as accessing the server's console).

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.token import Token
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get JSON Web Token
        api_response = api_instance.datacenters_servers_token_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Token**](Token.md)

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

# **datacenters_servers_upgrade_post**
> datacenters_servers_upgrade_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Upgrade a Server by ID

Upgrades the server version.

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Upgrade a Server by ID
        api_instance.datacenters_servers_upgrade_post(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_upgrade_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
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

# **datacenters_servers_volumes_delete**
> datacenters_servers_volumes_delete(datacenter_id, server_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Detach a Volume by ID

Detachs the specified volume from the server.

Note that only the volume's connection to the specified server is disconnected. If you want to delete the volume, you must submit a separate request to perform the deletion.

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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Detach a Volume by ID
        api_instance.datacenters_servers_volumes_delete(datacenter_id, server_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_volumes_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **volume_id** | **str**| The unique ID of the volume. | 
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

# **datacenters_servers_volumes_find_by_id**
> Volume datacenters_servers_volumes_find_by_id(datacenter_id, server_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Attached Volume by ID

Retrieves the properties of the volume attached to the specified server.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.volume import Volume
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get Attached Volume by ID
        api_response = api_instance.datacenters_servers_volumes_find_by_id(datacenter_id, server_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_volumes_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_volumes_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **volume_id** | **str**| The unique ID of the volume. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Volume**](Volume.md)

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

# **datacenters_servers_volumes_get**
> AttachedVolumes datacenters_servers_volumes_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

Get Attached Volumes

Lists all volumes attached to the specified server.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.attached_volumes import AttachedVolumes
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)
    offset = 0 # int | The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination). (optional) (default to 0)
    limit = 1000 # int | The maximum number of elements to return (use together with offset for pagination). (optional) (default to 1000)

    try:
        # Get Attached Volumes
        api_response = api_instance.datacenters_servers_volumes_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        print("The response of ServersApi->datacenters_servers_volumes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_volumes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 
 **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000]

### Return type

[**AttachedVolumes**](AttachedVolumes.md)

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

# **datacenters_servers_volumes_post**
> Volume datacenters_servers_volumes_post(datacenter_id, server_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Attach a Volume to a Server

Attachs an existing storage volume to the specified server.

You can attach an existing volume in the VDC to a server. To move a volume from one server to another, you must first detach the volume from the first server and attach it to the second server.

It is also possible to create and attach a volume in one step by simply providing a new volume description as a payload. The only difference is the URL; see 'Creating a Volume' for details about volumes.

Note that the combined total of attached volumes and NICs cannot exceed 24 per server.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.volume import Volume
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
    api_instance = ionos_cloud_api_v6_client.ServersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    volume = ionos_cloud_api_v6_client.Volume() # Volume | The volume to be attached (or created and attached).
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Attach a Volume to a Server
        api_response = api_instance.datacenters_servers_volumes_post(datacenter_id, server_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of ServersApi->datacenters_servers_volumes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->datacenters_servers_volumes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the data center. | 
 **server_id** | **str**| The unique ID of the server. | 
 **volume** | [**Volume**](Volume.md)| The volume to be attached (or created and attached). | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**Volume**](Volume.md)

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

