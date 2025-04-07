# Lans


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Lan]**](Lan.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.lans import Lans

# TODO update the JSON string below
json = "{}"
# create an instance of Lans from a JSON string
lans_instance = Lans.from_json(json)
# print the JSON string representation of the object
print(Lans.to_json())

# convert the object into a dict
lans_dict = lans_instance.to_dict()
# create an instance of Lans from a dict
lans_from_dict = Lans.from_dict(lans_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


