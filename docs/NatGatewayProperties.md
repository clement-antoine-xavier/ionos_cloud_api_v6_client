# NatGatewayProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the NAT Gateway. | 
**public_ips** | **List[str]** | Collection of public IP addresses of the NAT Gateway. Should be customer reserved IP addresses in that location. | 
**lans** | [**List[NatGatewayLanProperties]**](NatGatewayLanProperties.md) | Collection of LANs connected to the NAT Gateway. IPs must contain a valid subnet mask. If no IP is provided, the system will generate an IP with /24 subnet. | [optional] 

## Example

```python
from openapi_client.models.nat_gateway_properties import NatGatewayProperties

# TODO update the JSON string below
json = "{}"
# create an instance of NatGatewayProperties from a JSON string
nat_gateway_properties_instance = NatGatewayProperties.from_json(json)
# print the JSON string representation of the object
print(NatGatewayProperties.to_json())

# convert the object into a dict
nat_gateway_properties_dict = nat_gateway_properties_instance.to_dict()
# create an instance of NatGatewayProperties from a dict
nat_gateway_properties_from_dict = NatGatewayProperties.from_dict(nat_gateway_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


