# NetworkLoadBalancerForwardingRuleTargetHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check** | **bool** | Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. | [optional] 
**check_interval** | **int** | The interval in milliseconds between consecutive health checks; default is 2000. | [optional] 
**maintenance** | **bool** | Maintenance mode prevents the target from receiving balanced traffic. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.network_load_balancer_forwarding_rule_target_health_check import NetworkLoadBalancerForwardingRuleTargetHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerForwardingRuleTargetHealthCheck from a JSON string
network_load_balancer_forwarding_rule_target_health_check_instance = NetworkLoadBalancerForwardingRuleTargetHealthCheck.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerForwardingRuleTargetHealthCheck.to_json())

# convert the object into a dict
network_load_balancer_forwarding_rule_target_health_check_dict = network_load_balancer_forwarding_rule_target_health_check_instance.to_dict()
# create an instance of NetworkLoadBalancerForwardingRuleTargetHealthCheck from a dict
network_load_balancer_forwarding_rule_target_health_check_from_dict = NetworkLoadBalancerForwardingRuleTargetHealthCheck.from_dict(network_load_balancer_forwarding_rule_target_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


