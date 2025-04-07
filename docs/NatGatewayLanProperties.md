# NatGatewayLanProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id for the LAN connected to the NAT Gateway | 
**gateway_ips** | **List[str]** | Collection of gateway IP addresses of the NAT Gateway. Will be auto-generated if not provided. Should ideally be an IP belonging to the same subnet as the LAN | [optional] 

## Example

```python
from openapi_client.models.nat_gateway_lan_properties import NatGatewayLanProperties

# TODO update the JSON string below
json = "{}"
# create an instance of NatGatewayLanProperties from a JSON string
nat_gateway_lan_properties_instance = NatGatewayLanProperties.from_json(json)
# print the JSON string representation of the object
print(NatGatewayLanProperties.to_json())

# convert the object into a dict
nat_gateway_lan_properties_dict = nat_gateway_lan_properties_instance.to_dict()
# create an instance of NatGatewayLanProperties from a dict
nat_gateway_lan_properties_from_dict = NatGatewayLanProperties.from_dict(nat_gateway_lan_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


