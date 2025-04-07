# KubernetesNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | **str** | The object type. | [optional] [readonly] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**KubernetesNodeMetadata**](KubernetesNodeMetadata.md) |  | [optional] 
**properties** | [**KubernetesNodeProperties**](KubernetesNodeProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.kubernetes_node import KubernetesNode

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNode from a JSON string
kubernetes_node_instance = KubernetesNode.from_json(json)
# print the JSON string representation of the object
print(KubernetesNode.to_json())

# convert the object into a dict
kubernetes_node_dict = kubernetes_node_instance.to_dict()
# create an instance of KubernetesNode from a dict
kubernetes_node_from_dict = KubernetesNode.from_dict(kubernetes_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


