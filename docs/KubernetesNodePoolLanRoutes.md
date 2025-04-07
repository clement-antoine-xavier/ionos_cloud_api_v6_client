# KubernetesNodePoolLanRoutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | IPv4 or IPv6 CIDR to be routed via the interface. | [optional] 
**gateway_ip** | **str** | IPv4 or IPv6 Gateway IP for the route. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.kubernetes_node_pool_lan_routes import KubernetesNodePoolLanRoutes

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodePoolLanRoutes from a JSON string
kubernetes_node_pool_lan_routes_instance = KubernetesNodePoolLanRoutes.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodePoolLanRoutes.to_json())

# convert the object into a dict
kubernetes_node_pool_lan_routes_dict = kubernetes_node_pool_lan_routes_instance.to_dict()
# create an instance of KubernetesNodePoolLanRoutes from a dict
kubernetes_node_pool_lan_routes_from_dict = KubernetesNodePoolLanRoutes.from_dict(kubernetes_node_pool_lan_routes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


