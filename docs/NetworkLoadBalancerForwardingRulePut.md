# NetworkLoadBalancerForwardingRulePut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**properties** | [**NetworkLoadBalancerForwardingRuleProperties**](NetworkLoadBalancerForwardingRuleProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.network_load_balancer_forwarding_rule_put import NetworkLoadBalancerForwardingRulePut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerForwardingRulePut from a JSON string
network_load_balancer_forwarding_rule_put_instance = NetworkLoadBalancerForwardingRulePut.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerForwardingRulePut.to_json())

# convert the object into a dict
network_load_balancer_forwarding_rule_put_dict = network_load_balancer_forwarding_rule_put_instance.to_dict()
# create an instance of NetworkLoadBalancerForwardingRulePut from a dict
network_load_balancer_forwarding_rule_put_from_dict = NetworkLoadBalancerForwardingRulePut.from_dict(network_load_balancer_forwarding_rule_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


