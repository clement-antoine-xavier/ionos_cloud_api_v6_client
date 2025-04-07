# NetworkLoadBalancerForwardingRuleProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Network Load Balancer forwarding rule. | 
**algorithm** | **str** | Balancing algorithm | 
**protocol** | **str** | Balancing protocol | 
**listener_ip** | **str** | Listening (inbound) IP. | 
**listener_port** | **int** | Listening (inbound) port number; valid range is 1 to 65535. | 
**health_check** | [**NetworkLoadBalancerForwardingRuleHealthCheck**](NetworkLoadBalancerForwardingRuleHealthCheck.md) |  | [optional] 
**targets** | [**List[NetworkLoadBalancerForwardingRuleTarget]**](NetworkLoadBalancerForwardingRuleTarget.md) | Array of items in the collection. | 

## Example

```python
from ionos_cloud_api_v6_client.models.network_load_balancer_forwarding_rule_properties import NetworkLoadBalancerForwardingRuleProperties

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerForwardingRuleProperties from a JSON string
network_load_balancer_forwarding_rule_properties_instance = NetworkLoadBalancerForwardingRuleProperties.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerForwardingRuleProperties.to_json())

# convert the object into a dict
network_load_balancer_forwarding_rule_properties_dict = network_load_balancer_forwarding_rule_properties_instance.to_dict()
# create an instance of NetworkLoadBalancerForwardingRuleProperties from a dict
network_load_balancer_forwarding_rule_properties_from_dict = NetworkLoadBalancerForwardingRuleProperties.from_dict(network_load_balancer_forwarding_rule_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


