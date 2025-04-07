# NatGatewayRuleProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the NAT Gateway rule. | 
**type** | [**NatGatewayRuleType**](NatGatewayRuleType.md) | Type of the NAT Gateway rule. | [optional] 
**protocol** | [**NatGatewayRuleProtocol**](NatGatewayRuleProtocol.md) | Protocol of the NAT Gateway rule. Defaults to ALL. If protocol is &#39;ICMP&#39; then targetPortRange start and end cannot be set. | [optional] 
**source_subnet** | **str** | Source subnet of the NAT Gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address. | 
**public_ip** | **str** | Public IP address of the NAT Gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT Gateway resource | 
**target_subnet** | **str** | Target or destination subnet of the NAT Gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address. | [optional] 
**target_port_range** | [**TargetPortRange**](TargetPortRange.md) |  | [optional] 

## Example

```python
from openapi_client.models.nat_gateway_rule_properties import NatGatewayRuleProperties

# TODO update the JSON string below
json = "{}"
# create an instance of NatGatewayRuleProperties from a JSON string
nat_gateway_rule_properties_instance = NatGatewayRuleProperties.from_json(json)
# print the JSON string representation of the object
print(NatGatewayRuleProperties.to_json())

# convert the object into a dict
nat_gateway_rule_properties_dict = nat_gateway_rule_properties_instance.to_dict()
# create an instance of NatGatewayRuleProperties from a dict
nat_gateway_rule_properties_from_dict = NatGatewayRuleProperties.from_dict(nat_gateway_rule_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


