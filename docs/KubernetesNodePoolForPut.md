# KubernetesNodePoolForPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | **str** | The object type. | [optional] [readonly] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**KubernetesNodePoolPropertiesForPut**](KubernetesNodePoolPropertiesForPut.md) |  | 

## Example

```python
from openapi_client.models.kubernetes_node_pool_for_put import KubernetesNodePoolForPut

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodePoolForPut from a JSON string
kubernetes_node_pool_for_put_instance = KubernetesNodePoolForPut.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodePoolForPut.to_json())

# convert the object into a dict
kubernetes_node_pool_for_put_dict = kubernetes_node_pool_for_put_instance.to_dict()
# create an instance of KubernetesNodePoolForPut from a dict
kubernetes_node_pool_for_put_from_dict = KubernetesNodePoolForPut.from_dict(kubernetes_node_pool_for_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


