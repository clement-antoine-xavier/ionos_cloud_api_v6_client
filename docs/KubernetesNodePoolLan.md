# KubernetesNodePoolLan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter_id** | **str** | The datacenter ID, requires system privileges, for internal usage only | [optional] 
**id** | **int** | The LAN ID of an existing LAN at the related data center | 
**dhcp** | **bool** | Specifies whether the Kubernetes node pool LAN reserves an IP with DHCP. | [optional] 
**routes** | [**List[KubernetesNodePoolLanRoutes]**](KubernetesNodePoolLanRoutes.md) | The array of additional LANs attached to worker nodes. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.kubernetes_node_pool_lan import KubernetesNodePoolLan

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodePoolLan from a JSON string
kubernetes_node_pool_lan_instance = KubernetesNodePoolLan.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodePoolLan.to_json())

# convert the object into a dict
kubernetes_node_pool_lan_dict = kubernetes_node_pool_lan_instance.to_dict()
# create an instance of KubernetesNodePoolLan from a dict
kubernetes_node_pool_lan_from_dict = KubernetesNodePoolLan.from_dict(kubernetes_node_pool_lan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


