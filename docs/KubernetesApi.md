# ionos_cloud_api_v6_client.KubernetesApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**k8s_delete**](KubernetesApi.md#k8s_delete) | **DELETE** /k8s/{k8sClusterId} | Delete a Kubernetes Cluster by ID
[**k8s_find_by_cluster_id**](KubernetesApi.md#k8s_find_by_cluster_id) | **GET** /k8s/{k8sClusterId} | Get a Kubernetes Cluster by ID
[**k8s_get**](KubernetesApi.md#k8s_get) | **GET** /k8s | Get Kubernetes Clusters
[**k8s_kubeconfig_get**](KubernetesApi.md#k8s_kubeconfig_get) | **GET** /k8s/{k8sClusterId}/kubeconfig | Get Kubernetes Configuration File
[**k8s_nodepools_delete**](KubernetesApi.md#k8s_nodepools_delete) | **DELETE** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Delete a Kubernetes Node Pool by ID
[**k8s_nodepools_find_by_id**](KubernetesApi.md#k8s_nodepools_find_by_id) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Get a Kubernetes Node Pool by ID
[**k8s_nodepools_get**](KubernetesApi.md#k8s_nodepools_get) | **GET** /k8s/{k8sClusterId}/nodepools | Get Kubernetes Node Pools
[**k8s_nodepools_nodes_delete**](KubernetesApi.md#k8s_nodepools_nodes_delete) | **DELETE** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId} | Delete a Kubernetes Node by ID
[**k8s_nodepools_nodes_find_by_id**](KubernetesApi.md#k8s_nodepools_nodes_find_by_id) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId} | Get Kubernetes Node by ID
[**k8s_nodepools_nodes_get**](KubernetesApi.md#k8s_nodepools_nodes_get) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes | Get Kubernetes Nodes
[**k8s_nodepools_nodes_replace_post**](KubernetesApi.md#k8s_nodepools_nodes_replace_post) | **POST** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId}/replace | Recreate a Kubernetes Node by ID
[**k8s_nodepools_post**](KubernetesApi.md#k8s_nodepools_post) | **POST** /k8s/{k8sClusterId}/nodepools | Create a Kubernetes Node Pool
[**k8s_nodepools_put**](KubernetesApi.md#k8s_nodepools_put) | **PUT** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Modify a Kubernetes Node Pool by ID
[**k8s_post**](KubernetesApi.md#k8s_post) | **POST** /k8s | Create a Kubernetes Cluster
[**k8s_put**](KubernetesApi.md#k8s_put) | **PUT** /k8s/{k8sClusterId} | Modify a Kubernetes Cluster by ID
[**k8s_versions_default_get**](KubernetesApi.md#k8s_versions_default_get) | **GET** /k8s/versions/default | Get Default Kubernetes Version
[**k8s_versions_get**](KubernetesApi.md#k8s_versions_get) | **GET** /k8s/versions | Get Kubernetes Versions


# **k8s_delete**
> k8s_delete(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Kubernetes Cluster by ID

Deletes the K8s cluster specified  by its ID.

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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Delete a Kubernetes Cluster by ID
        api_instance.k8s_delete(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
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
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k8s_find_by_cluster_id**
> KubernetesCluster k8s_find_by_cluster_id(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get a Kubernetes Cluster by ID

Retrieves the K8s cluster specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_cluster import KubernetesCluster
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the K8s cluster to be retrieved.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get a Kubernetes Cluster by ID
        api_response = api_instance.k8s_find_by_cluster_id(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_find_by_cluster_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_find_by_cluster_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the K8s cluster to be retrieved. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesCluster**](KubernetesCluster.md)

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

# **k8s_get**
> KubernetesClusters k8s_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Kubernetes Clusters

Retrieves a list of all K8s clusters provisioned under your account.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_clusters import KubernetesClusters
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get Kubernetes Clusters
        api_response = api_instance.k8s_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesClusters**](KubernetesClusters.md)

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

# **k8s_kubeconfig_get**
> str k8s_kubeconfig_get(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Kubernetes Configuration File

Retrieves the configuration file for the specified K8s cluster. You can define the format (YAML or JSON) of the returned file in the Accept header. By default, 'application/yaml' is specified.

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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get Kubernetes Configuration File
        api_response = api_instance.k8s_kubeconfig_get(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_kubeconfig_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_kubeconfig_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

**str**

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/x-yaml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k8s_nodepools_delete**
> k8s_nodepools_delete(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Kubernetes Node Pool by ID

Deletes the K8s node pool specified by its ID.

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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Delete a Kubernetes Node Pool by ID
        api_instance.k8s_nodepools_delete(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. | 
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
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k8s_nodepools_find_by_id**
> KubernetesNodePool k8s_nodepools_find_by_id(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get a Kubernetes Node Pool by ID

Retrieves the K8s node pool specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_node_pool import KubernetesNodePool
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get a Kubernetes Node Pool by ID
        api_response = api_instance.k8s_nodepools_find_by_id(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_nodepools_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesNodePool**](KubernetesNodePool.md)

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

# **k8s_nodepools_get**
> KubernetesNodePools k8s_nodepools_get(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Kubernetes Node Pools

Retrieves a list of K8s node pools of a cluster specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_node_pools import KubernetesNodePools
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get Kubernetes Node Pools
        api_response = api_instance.k8s_nodepools_get(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_nodepools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesNodePools**](KubernetesNodePools.md)

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

# **k8s_nodepools_nodes_delete**
> k8s_nodepools_nodes_delete(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Kubernetes Node by ID

Deletes the K8s node specified by its ID.

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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    node_id = 'node_id_example' # str | The unique ID of the Kubernetes node.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Delete a Kubernetes Node by ID
        api_instance.k8s_nodepools_nodes_delete(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_nodes_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. | 
 **node_id** | **str**| The unique ID of the Kubernetes node. | 
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
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k8s_nodepools_nodes_find_by_id**
> KubernetesNode k8s_nodepools_nodes_find_by_id(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Kubernetes Node by ID

Retrieves the K8s node specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_node import KubernetesNode
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    node_id = 'node_id_example' # str | The unique ID of the Kubernetes node.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get Kubernetes Node by ID
        api_response = api_instance.k8s_nodepools_nodes_find_by_id(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_nodepools_nodes_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_nodes_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. | 
 **node_id** | **str**| The unique ID of the Kubernetes node. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesNode**](KubernetesNode.md)

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

# **k8s_nodepools_nodes_get**
> KubernetesNodes k8s_nodepools_nodes_get(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Kubernetes Nodes

Retrieves the list of all K8s nodes of the specified node pool.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_nodes import KubernetesNodes
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Get Kubernetes Nodes
        api_response = api_instance.k8s_nodepools_nodes_get(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_nodepools_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_nodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesNodes**](KubernetesNodes.md)

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

# **k8s_nodepools_nodes_replace_post**
> k8s_nodepools_nodes_replace_post(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Recreate a Kubernetes Node by ID

Recreates the K8s node specified by its ID.

If a node becomes unusable, Managed Kubernetes allows you to recreate it with a configuration based on the node pool template. Once the status is 'Active,' all the pods from the failed node will be migrated to the new node. The node pool has an additional billable 'active' node during this process.

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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    node_id = 'node_id_example' # str | The unique ID of the Kubernetes node.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Recreate a Kubernetes Node by ID
        api_instance.k8s_nodepools_nodes_replace_post(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_nodes_replace_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. | 
 **node_id** | **str**| The unique ID of the Kubernetes node. | 
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
**202** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k8s_nodepools_post**
> KubernetesNodePool k8s_nodepools_post(k8s_cluster_id, kubernetes_node_pool, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Kubernetes Node Pool

Creates a node pool inside the specified K8s cluster.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_node_pool import KubernetesNodePool
from ionos_cloud_api_v6_client.models.kubernetes_node_pool_for_post import KubernetesNodePoolForPost
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    kubernetes_node_pool = ionos_cloud_api_v6_client.KubernetesNodePoolForPost() # KubernetesNodePoolForPost | The Kubernetes node pool to create.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Create a Kubernetes Node Pool
        api_response = api_instance.k8s_nodepools_post(k8s_cluster_id, kubernetes_node_pool, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_nodepools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **kubernetes_node_pool** | [**KubernetesNodePoolForPost**](KubernetesNodePoolForPost.md)| The Kubernetes node pool to create. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesNodePool**](KubernetesNodePool.md)

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

# **k8s_nodepools_put**
> KubernetesNodePool k8s_nodepools_put(k8s_cluster_id, nodepool_id, kubernetes_node_pool, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Kubernetes Node Pool by ID

Modifies the K8s node pool specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_node_pool import KubernetesNodePool
from ionos_cloud_api_v6_client.models.kubernetes_node_pool_for_put import KubernetesNodePoolForPut
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    kubernetes_node_pool = ionos_cloud_api_v6_client.KubernetesNodePoolForPut() # KubernetesNodePoolForPut | Details of the Kubernetes Node Pool
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Modify a Kubernetes Node Pool by ID
        api_response = api_instance.k8s_nodepools_put(k8s_cluster_id, nodepool_id, kubernetes_node_pool, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_nodepools_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_nodepools_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. | 
 **kubernetes_node_pool** | [**KubernetesNodePoolForPut**](KubernetesNodePoolForPut.md)| Details of the Kubernetes Node Pool | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesNodePool**](KubernetesNodePool.md)

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

# **k8s_post**
> KubernetesCluster k8s_post(kubernetes_cluster, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Kubernetes Cluster

Creates a K8s cluster provisioned under your account.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_cluster import KubernetesCluster
from ionos_cloud_api_v6_client.models.kubernetes_cluster_for_post import KubernetesClusterForPost
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    kubernetes_cluster = ionos_cloud_api_v6_client.KubernetesClusterForPost() # KubernetesClusterForPost | The Kubernetes cluster to create.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Create a Kubernetes Cluster
        api_response = api_instance.k8s_post(kubernetes_cluster, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_cluster** | [**KubernetesClusterForPost**](KubernetesClusterForPost.md)| The Kubernetes cluster to create. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesCluster**](KubernetesCluster.md)

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

# **k8s_put**
> KubernetesCluster k8s_put(k8s_cluster_id, kubernetes_cluster, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Kubernetes Cluster by ID

Modifies the K8s cluster specified by its ID.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import ionos_cloud_api_v6_client
from ionos_cloud_api_v6_client.models.kubernetes_cluster import KubernetesCluster
from ionos_cloud_api_v6_client.models.kubernetes_cluster_for_put import KubernetesClusterForPut
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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    kubernetes_cluster = ionos_cloud_api_v6_client.KubernetesClusterForPut() # KubernetesClusterForPut | The modified Kubernetes cluster.
    pretty = True # bool | Controls whether the response is pretty-printed (with indentations and new lines). (optional) (default to True)
    depth = 0 # int | Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users with multiple contracts must provide the contract number, for which all API requests are to be executed. (optional)

    try:
        # Modify a Kubernetes Cluster by ID
        api_response = api_instance.k8s_put(k8s_cluster_id, kubernetes_cluster, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        print("The response of KubernetesApi->k8s_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. | 
 **kubernetes_cluster** | [**KubernetesClusterForPut**](KubernetesClusterForPut.md)| The modified Kubernetes cluster. | 
 **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True]
 **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional] 

### Return type

[**KubernetesCluster**](KubernetesCluster.md)

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

# **k8s_versions_default_get**
> str k8s_versions_default_get()

Get Default Kubernetes Version

Retrieves the current default K8s version to be used by the clusters and node pools.

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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)

    try:
        # Get Default Kubernetes Version
        api_response = api_instance.k8s_versions_default_get()
        print("The response of KubernetesApi->k8s_versions_default_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_versions_default_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 401 (auth error), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type), 422 (validation error), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k8s_versions_get**
> List[str] k8s_versions_get()

Get Kubernetes Versions

Lists available K8s versions.

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
    api_instance = ionos_cloud_api_v6_client.KubernetesApi(api_client)

    try:
        # Get Kubernetes Versions
        api_response = api_instance.k8s_versions_get()
        print("The response of KubernetesApi->k8s_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->k8s_versions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-RateLimit-Remaining - The number of requests that can still be made without triggering a failure response. <br>  * X-RateLimit-Limit - The average number of requests per minute allowed. <br>  * X-RateLimit-Burst - The maximum number of concurrent API requests allowed. <br>  |
**0** | Any erroneous status code: 401 (auth error), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type), 422 (validation error), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

