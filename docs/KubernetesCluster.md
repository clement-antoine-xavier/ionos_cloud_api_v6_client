# KubernetesCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource unique identifier. | [optional] [readonly] 
**type** | **str** | The object type. | [optional] [readonly] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**KubernetesClusterProperties**](KubernetesClusterProperties.md) |  | 
**entities** | [**KubernetesClusterEntities**](KubernetesClusterEntities.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.kubernetes_cluster import KubernetesCluster

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesCluster from a JSON string
kubernetes_cluster_instance = KubernetesCluster.from_json(json)
# print the JSON string representation of the object
print(KubernetesCluster.to_json())

# convert the object into a dict
kubernetes_cluster_dict = kubernetes_cluster_instance.to_dict()
# create an instance of KubernetesCluster from a dict
kubernetes_cluster_from_dict = KubernetesCluster.from_dict(kubernetes_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


