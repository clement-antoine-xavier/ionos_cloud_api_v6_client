# ApplicationLoadBalancerForwardingRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[ApplicationLoadBalancerForwardingRule]**](ApplicationLoadBalancerForwardingRule.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rules import ApplicationLoadBalancerForwardingRules

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLoadBalancerForwardingRules from a JSON string
application_load_balancer_forwarding_rules_instance = ApplicationLoadBalancerForwardingRules.from_json(json)
# print the JSON string representation of the object
print(ApplicationLoadBalancerForwardingRules.to_json())

# convert the object into a dict
application_load_balancer_forwarding_rules_dict = application_load_balancer_forwarding_rules_instance.to_dict()
# create an instance of ApplicationLoadBalancerForwardingRules from a dict
application_load_balancer_forwarding_rules_from_dict = ApplicationLoadBalancerForwardingRules.from_dict(application_load_balancer_forwarding_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


