# KubernetesNodeProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kubernetes node name. | 
**public_ip** | **str** | The public IP associated with the node. | [optional] 
**private_ip** | **str** | The private IP associated with the node. | [optional] 
**k8s_version** | **str** | The Kubernetes version running in the node pool. Note that this imposes restrictions on which Kubernetes versions can run in the node pools of a cluster. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions. | 

## Example

```python
from openapi_client.models.kubernetes_node_properties import KubernetesNodeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodeProperties from a JSON string
kubernetes_node_properties_instance = KubernetesNodeProperties.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodeProperties.to_json())

# convert the object into a dict
kubernetes_node_properties_dict = kubernetes_node_properties_instance.to_dict()
# create an instance of KubernetesNodeProperties from a dict
kubernetes_node_properties_from_dict = KubernetesNodeProperties.from_dict(kubernetes_node_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


