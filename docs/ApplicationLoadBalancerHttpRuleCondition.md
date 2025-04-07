# ApplicationLoadBalancerHttpRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The HTTP rule condition type. | 
**condition** | **str** | The matching rule for the HTTP rule condition attribute; this parameter is mandatory for &#39;HEADER&#39;, &#39;PATH&#39;, &#39;QUERY&#39;, &#39;METHOD&#39;, &#39;HOST&#39;, and &#39;COOKIE&#39; types. It must be &#39;null&#39; if the type is &#39;SOURCE_IP&#39;. | 
**negate** | **bool** | Specifies whether the condition should be negated; the default value is &#39;FALSE&#39;. | [optional] 
**key** | **str** | The key can only be set when the HTTP rule condition type is &#39;COOKIES&#39;, &#39;HEADER&#39;, or &#39;QUERY&#39;. For the type &#39;PATH&#39;, &#39;METHOD&#39;, &#39;HOST&#39;, or &#39;SOURCE_IP&#39; the value must be &#39;null&#39;. | [optional] 
**value** | **str** | This parameter is mandatory for the conditions &#39;CONTAINS&#39;, &#39;EQUALS&#39;, &#39;MATCHES&#39;, &#39;STARTS_WITH&#39;, &#39;ENDS_WITH&#39;, or if the type is &#39;SOURCE_IP&#39;. Specify a valid CIDR. If the condition is &#39;EXISTS&#39;, the value must be &#39;null&#39;. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.application_load_balancer_http_rule_condition import ApplicationLoadBalancerHttpRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLoadBalancerHttpRuleCondition from a JSON string
application_load_balancer_http_rule_condition_instance = ApplicationLoadBalancerHttpRuleCondition.from_json(json)
# print the JSON string representation of the object
print(ApplicationLoadBalancerHttpRuleCondition.to_json())

# convert the object into a dict
application_load_balancer_http_rule_condition_dict = application_load_balancer_http_rule_condition_instance.to_dict()
# create an instance of ApplicationLoadBalancerHttpRuleCondition from a dict
application_load_balancer_http_rule_condition_from_dict = ApplicationLoadBalancerHttpRuleCondition.from_dict(application_load_balancer_http_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


