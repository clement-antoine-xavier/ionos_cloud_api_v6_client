# KubernetesClusterEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodepools** | [**KubernetesNodePools**](KubernetesNodePools.md) |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_cluster_entities import KubernetesClusterEntities

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesClusterEntities from a JSON string
kubernetes_cluster_entities_instance = KubernetesClusterEntities.from_json(json)
# print the JSON string representation of the object
print(KubernetesClusterEntities.to_json())

# convert the object into a dict
kubernetes_cluster_entities_dict = kubernetes_cluster_entities_instance.to_dict()
# create an instance of KubernetesClusterEntities from a dict
kubernetes_cluster_entities_from_dict = KubernetesClusterEntities.from_dict(kubernetes_cluster_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


