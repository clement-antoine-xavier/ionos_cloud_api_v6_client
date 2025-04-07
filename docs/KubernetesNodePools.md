# KubernetesNodePools


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique representation of the Kubernetes node pool as a resource collection. | [optional] [readonly] 
**type** | **str** | The resource type within a collection. | [optional] [readonly] 
**href** | **str** | The URL to the collection representation (absolute path). | [optional] [readonly] 
**items** | [**List[KubernetesNodePool]**](KubernetesNodePool.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from openapi_client.models.kubernetes_node_pools import KubernetesNodePools

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodePools from a JSON string
kubernetes_node_pools_instance = KubernetesNodePools.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodePools.to_json())

# convert the object into a dict
kubernetes_node_pools_dict = kubernetes_node_pools_instance.to_dict()
# create an instance of KubernetesNodePools from a dict
kubernetes_node_pools_from_dict = KubernetesNodePools.from_dict(kubernetes_node_pools_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


