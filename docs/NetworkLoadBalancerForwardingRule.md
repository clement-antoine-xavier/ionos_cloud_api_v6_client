# NetworkLoadBalancerForwardingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**NetworkLoadBalancerForwardingRuleProperties**](NetworkLoadBalancerForwardingRuleProperties.md) |  | 

## Example

```python
from openapi_client.models.network_load_balancer_forwarding_rule import NetworkLoadBalancerForwardingRule

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerForwardingRule from a JSON string
network_load_balancer_forwarding_rule_instance = NetworkLoadBalancerForwardingRule.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerForwardingRule.to_json())

# convert the object into a dict
network_load_balancer_forwarding_rule_dict = network_load_balancer_forwarding_rule_instance.to_dict()
# create an instance of NetworkLoadBalancerForwardingRule from a dict
network_load_balancer_forwarding_rule_from_dict = NetworkLoadBalancerForwardingRule.from_dict(network_load_balancer_forwarding_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


