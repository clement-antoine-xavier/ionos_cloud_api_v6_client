# KubernetesClusterForPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource unique identifier. | [optional] [readonly] 
**type** | **str** | The object type. | [optional] [readonly] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**KubernetesClusterPropertiesForPost**](KubernetesClusterPropertiesForPost.md) |  | 
**entities** | [**KubernetesClusterEntities**](KubernetesClusterEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_cluster_for_post import KubernetesClusterForPost

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesClusterForPost from a JSON string
kubernetes_cluster_for_post_instance = KubernetesClusterForPost.from_json(json)
# print the JSON string representation of the object
print(KubernetesClusterForPost.to_json())

# convert the object into a dict
kubernetes_cluster_for_post_dict = kubernetes_cluster_for_post_instance.to_dict()
# create an instance of KubernetesClusterForPost from a dict
kubernetes_cluster_for_post_from_dict = KubernetesClusterForPost.from_dict(kubernetes_cluster_for_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


