# KubernetesNodePoolForPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | **str** | The object type. | [optional] [readonly] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**KubernetesNodePoolPropertiesForPost**](KubernetesNodePoolPropertiesForPost.md) |  | 

## Example

```python
from openapi_client.models.kubernetes_node_pool_for_post import KubernetesNodePoolForPost

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodePoolForPost from a JSON string
kubernetes_node_pool_for_post_instance = KubernetesNodePoolForPost.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodePoolForPost.to_json())

# convert the object into a dict
kubernetes_node_pool_for_post_dict = kubernetes_node_pool_for_post_instance.to_dict()
# create an instance of KubernetesNodePoolForPost from a dict
kubernetes_node_pool_for_post_from_dict = KubernetesNodePoolForPost.from_dict(kubernetes_node_pool_for_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


