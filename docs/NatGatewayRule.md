# NatGatewayRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**NatGatewayRuleProperties**](NatGatewayRuleProperties.md) |  | 

## Example

```python
from openapi_client.models.nat_gateway_rule import NatGatewayRule

# TODO update the JSON string below
json = "{}"
# create an instance of NatGatewayRule from a JSON string
nat_gateway_rule_instance = NatGatewayRule.from_json(json)
# print the JSON string representation of the object
print(NatGatewayRule.to_json())

# convert the object into a dict
nat_gateway_rule_dict = nat_gateway_rule_instance.to_dict()
# create an instance of NatGatewayRule from a dict
nat_gateway_rule_from_dict = NatGatewayRule.from_dict(nat_gateway_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


