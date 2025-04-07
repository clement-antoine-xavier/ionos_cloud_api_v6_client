# KubernetesNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique representation of the Kubernetes node pool as a resource collection. | [optional] [readonly] 
**type** | **str** | The resource type within a collection. | [optional] [readonly] 
**href** | **str** | The URL to the collection representation (absolute path). | [optional] [readonly] 
**items** | [**List[KubernetesNode]**](KubernetesNode.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.kubernetes_nodes import KubernetesNodes

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodes from a JSON string
kubernetes_nodes_instance = KubernetesNodes.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodes.to_json())

# convert the object into a dict
kubernetes_nodes_dict = kubernetes_nodes_instance.to_dict()
# create an instance of KubernetesNodes from a dict
kubernetes_nodes_from_dict = KubernetesNodes.from_dict(kubernetes_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


