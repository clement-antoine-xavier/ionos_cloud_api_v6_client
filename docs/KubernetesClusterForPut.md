# KubernetesClusterForPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | **str** | The type of object. | [optional] [readonly] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**KubernetesClusterPropertiesForPut**](KubernetesClusterPropertiesForPut.md) |  | 
**entities** | [**KubernetesClusterEntities**](KubernetesClusterEntities.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.kubernetes_cluster_for_put import KubernetesClusterForPut

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesClusterForPut from a JSON string
kubernetes_cluster_for_put_instance = KubernetesClusterForPut.from_json(json)
# print the JSON string representation of the object
print(KubernetesClusterForPut.to_json())

# convert the object into a dict
kubernetes_cluster_for_put_dict = kubernetes_cluster_for_put_instance.to_dict()
# create an instance of KubernetesClusterForPut from a dict
kubernetes_cluster_for_put_from_dict = KubernetesClusterForPut.from_dict(kubernetes_cluster_for_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


