# NatGateway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**NatGatewayProperties**](NatGatewayProperties.md) |  | 
**entities** | [**NatGatewayEntities**](NatGatewayEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.nat_gateway import NatGateway

# TODO update the JSON string below
json = "{}"
# create an instance of NatGateway from a JSON string
nat_gateway_instance = NatGateway.from_json(json)
# print the JSON string representation of the object
print(NatGateway.to_json())

# convert the object into a dict
nat_gateway_dict = nat_gateway_instance.to_dict()
# create an instance of NatGateway from a dict
nat_gateway_from_dict = NatGateway.from_dict(nat_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


