# NatGateways


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[NatGateway]**](NatGateway.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.nat_gateways import NatGateways

# TODO update the JSON string below
json = "{}"
# create an instance of NatGateways from a JSON string
nat_gateways_instance = NatGateways.from_json(json)
# print the JSON string representation of the object
print(NatGateways.to_json())

# convert the object into a dict
nat_gateways_dict = nat_gateways_instance.to_dict()
# create an instance of NatGateways from a dict
nat_gateways_from_dict = NatGateways.from_dict(nat_gateways_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


