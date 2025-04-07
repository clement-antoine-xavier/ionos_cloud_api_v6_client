# NetworkLoadBalancerEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flowlogs** | [**FlowLogs**](FlowLogs.md) |  | [optional] 
**forwardingrules** | [**NetworkLoadBalancerForwardingRules**](NetworkLoadBalancerForwardingRules.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.network_load_balancer_entities import NetworkLoadBalancerEntities

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerEntities from a JSON string
network_load_balancer_entities_instance = NetworkLoadBalancerEntities.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerEntities.to_json())

# convert the object into a dict
network_load_balancer_entities_dict = network_load_balancer_entities_instance.to_dict()
# create an instance of NetworkLoadBalancerEntities from a dict
network_load_balancer_entities_from_dict = NetworkLoadBalancerEntities.from_dict(network_load_balancer_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


