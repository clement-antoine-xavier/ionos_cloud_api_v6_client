# NetworkLoadBalancerForwardingRuleHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_timeout** | **int** | The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds). | [optional] 
**connect_timeout** | **int** | The maximum time in milliseconds to wait for a connection attempt to a target to succeed; default is 5000 (five seconds). | [optional] 
**target_timeout** | **int** | The maximum time in milliseconds that a target can remain inactive; default is 50,000 (50 seconds). | [optional] 
**retries** | **int** | The maximum number of attempts to reconnect to a target after a connection failure. Valid range is 0 to 65535 and default is three reconnection attempts. | [optional] 

## Example

```python
from openapi_client.models.network_load_balancer_forwarding_rule_health_check import NetworkLoadBalancerForwardingRuleHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerForwardingRuleHealthCheck from a JSON string
network_load_balancer_forwarding_rule_health_check_instance = NetworkLoadBalancerForwardingRuleHealthCheck.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerForwardingRuleHealthCheck.to_json())

# convert the object into a dict
network_load_balancer_forwarding_rule_health_check_dict = network_load_balancer_forwarding_rule_health_check_instance.to_dict()
# create an instance of NetworkLoadBalancerForwardingRuleHealthCheck from a dict
network_load_balancer_forwarding_rule_health_check_from_dict = NetworkLoadBalancerForwardingRuleHealthCheck.from_dict(network_load_balancer_forwarding_rule_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


