# PrivateCrossConnect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**PrivateCrossConnectProperties**](PrivateCrossConnectProperties.md) |  | 

## Example

```python
from openapi_client.models.private_cross_connect import PrivateCrossConnect

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCrossConnect from a JSON string
private_cross_connect_instance = PrivateCrossConnect.from_json(json)
# print the JSON string representation of the object
print(PrivateCrossConnect.to_json())

# convert the object into a dict
private_cross_connect_dict = private_cross_connect_instance.to_dict()
# create an instance of PrivateCrossConnect from a dict
private_cross_connect_from_dict = PrivateCrossConnect.from_dict(private_cross_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


