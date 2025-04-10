# NatGatewayPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**properties** | [**NatGatewayProperties**](NatGatewayProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.nat_gateway_put import NatGatewayPut

# TODO update the JSON string below
json = "{}"
# create an instance of NatGatewayPut from a JSON string
nat_gateway_put_instance = NatGatewayPut.from_json(json)
# print the JSON string representation of the object
print(NatGatewayPut.to_json())

# convert the object into a dict
nat_gateway_put_dict = nat_gateway_put_instance.to_dict()
# create an instance of NatGatewayPut from a dict
nat_gateway_put_from_dict = NatGatewayPut.from_dict(nat_gateway_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


