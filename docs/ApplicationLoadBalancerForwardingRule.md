# ApplicationLoadBalancerForwardingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**ApplicationLoadBalancerForwardingRuleProperties**](ApplicationLoadBalancerForwardingRuleProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.application_load_balancer_forwarding_rule import ApplicationLoadBalancerForwardingRule

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLoadBalancerForwardingRule from a JSON string
application_load_balancer_forwarding_rule_instance = ApplicationLoadBalancerForwardingRule.from_json(json)
# print the JSON string representation of the object
print(ApplicationLoadBalancerForwardingRule.to_json())

# convert the object into a dict
application_load_balancer_forwarding_rule_dict = application_load_balancer_forwarding_rule_instance.to_dict()
# create an instance of ApplicationLoadBalancerForwardingRule from a dict
application_load_balancer_forwarding_rule_from_dict = ApplicationLoadBalancerForwardingRule.from_dict(application_load_balancer_forwarding_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


