# NetworkLoadBalancerForwardingRuleTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IP of the balanced target VM. | 
**port** | **int** | The port of the balanced target service; valid range is 1 to 65535. | 
**weight** | **int** | Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1. Targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best to assign weights in the middle of the range to leave room for later adjustments. | 
**proxy_protocol** | **str** | Proxy protocol version. | [optional] [default to 'none']
**health_check** | [**NetworkLoadBalancerForwardingRuleTargetHealthCheck**](NetworkLoadBalancerForwardingRuleTargetHealthCheck.md) |  | [optional] 

## Example

```python
from openapi_client.models.network_load_balancer_forwarding_rule_target import NetworkLoadBalancerForwardingRuleTarget

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerForwardingRuleTarget from a JSON string
network_load_balancer_forwarding_rule_target_instance = NetworkLoadBalancerForwardingRuleTarget.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerForwardingRuleTarget.to_json())

# convert the object into a dict
network_load_balancer_forwarding_rule_target_dict = network_load_balancer_forwarding_rule_target_instance.to_dict()
# create an instance of NetworkLoadBalancerForwardingRuleTarget from a dict
network_load_balancer_forwarding_rule_target_from_dict = NetworkLoadBalancerForwardingRuleTarget.from_dict(network_load_balancer_forwarding_rule_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


