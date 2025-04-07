# KubernetesNodePool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | **str** | The object type. | [optional] [readonly] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**KubernetesNodePoolProperties**](KubernetesNodePoolProperties.md) |  | 

## Example

```python
from openapi_client.models.kubernetes_node_pool import KubernetesNodePool

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodePool from a JSON string
kubernetes_node_pool_instance = KubernetesNodePool.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodePool.to_json())

# convert the object into a dict
kubernetes_node_pool_dict = kubernetes_node_pool_instance.to_dict()
# create an instance of KubernetesNodePool from a dict
kubernetes_node_pool_from_dict = KubernetesNodePool.from_dict(kubernetes_node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


