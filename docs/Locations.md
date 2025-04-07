# Locations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Location]**](Location.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from openapi_client.models.locations import Locations

# TODO update the JSON string below
json = "{}"
# create an instance of Locations from a JSON string
locations_instance = Locations.from_json(json)
# print the JSON string representation of the object
print(Locations.to_json())

# convert the object into a dict
locations_dict = locations_instance.to_dict()
# create an instance of Locations from a dict
locations_from_dict = Locations.from_dict(locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


