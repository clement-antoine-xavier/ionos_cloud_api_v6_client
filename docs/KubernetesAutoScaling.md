# KubernetesAutoScaling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_node_count** | **int** | The minimum number of working nodes that the managed node pool can scale must be &gt;&#x3D; 1 and &gt;&#x3D; nodeCount. Required if autoScaling is specified. | 
**max_node_count** | **int** | The maximum number of worker nodes that the managed node pool can scale in. Must be &gt;&#x3D; minNodeCount and must be &gt;&#x3D; nodeCount. Required if autoScaling is specified. | 

## Example

```python
from openapi_client.models.kubernetes_auto_scaling import KubernetesAutoScaling

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesAutoScaling from a JSON string
kubernetes_auto_scaling_instance = KubernetesAutoScaling.from_json(json)
# print the JSON string representation of the object
print(KubernetesAutoScaling.to_json())

# convert the object into a dict
kubernetes_auto_scaling_dict = kubernetes_auto_scaling_instance.to_dict()
# create an instance of KubernetesAutoScaling from a dict
kubernetes_auto_scaling_from_dict = KubernetesAutoScaling.from_dict(kubernetes_auto_scaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


