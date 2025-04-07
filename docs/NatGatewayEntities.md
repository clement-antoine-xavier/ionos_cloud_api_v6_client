# NatGatewayEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**NatGatewayRules**](NatGatewayRules.md) |  | [optional] 
**flowlogs** | [**FlowLogs**](FlowLogs.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.nat_gateway_entities import NatGatewayEntities

# TODO update the JSON string below
json = "{}"
# create an instance of NatGatewayEntities from a JSON string
nat_gateway_entities_instance = NatGatewayEntities.from_json(json)
# print the JSON string representation of the object
print(NatGatewayEntities.to_json())

# convert the object into a dict
nat_gateway_entities_dict = nat_gateway_entities_instance.to_dict()
# create an instance of NatGatewayEntities from a dict
nat_gateway_entities_from_dict = NatGatewayEntities.from_dict(nat_gateway_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


