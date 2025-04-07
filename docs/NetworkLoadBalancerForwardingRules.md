# NetworkLoadBalancerForwardingRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[NetworkLoadBalancerForwardingRule]**](NetworkLoadBalancerForwardingRule.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.network_load_balancer_forwarding_rules import NetworkLoadBalancerForwardingRules

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerForwardingRules from a JSON string
network_load_balancer_forwarding_rules_instance = NetworkLoadBalancerForwardingRules.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerForwardingRules.to_json())

# convert the object into a dict
network_load_balancer_forwarding_rules_dict = network_load_balancer_forwarding_rules_instance.to_dict()
# create an instance of NetworkLoadBalancerForwardingRules from a dict
network_load_balancer_forwarding_rules_from_dict = NetworkLoadBalancerForwardingRules.from_dict(network_load_balancer_forwarding_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


