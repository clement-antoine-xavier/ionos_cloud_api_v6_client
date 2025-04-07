# PrivateCrossConnects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[PrivateCrossConnect]**](PrivateCrossConnect.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from openapi_client.models.private_cross_connects import PrivateCrossConnects

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCrossConnects from a JSON string
private_cross_connects_instance = PrivateCrossConnects.from_json(json)
# print the JSON string representation of the object
print(PrivateCrossConnects.to_json())

# convert the object into a dict
private_cross_connects_dict = private_cross_connects_instance.to_dict()
# create an instance of PrivateCrossConnects from a dict
private_cross_connects_from_dict = PrivateCrossConnects.from_dict(private_cross_connects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


