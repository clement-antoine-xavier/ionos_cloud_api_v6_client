# LocationProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The location name. | [optional] 
**features** | **List[str]** | A list of available features in the location. | [optional] [readonly] 
**image_aliases** | **List[str]** | A list of image aliases available in the location. | [optional] [readonly] 
**cpu_architecture** | [**List[CpuArchitectureProperties]**](CpuArchitectureProperties.md) | A list of available CPU types and related resources available in the location. | [optional] [readonly] 

## Example

```python
from openapi_client.models.location_properties import LocationProperties

# TODO update the JSON string below
json = "{}"
# create an instance of LocationProperties from a JSON string
location_properties_instance = LocationProperties.from_json(json)
# print the JSON string representation of the object
print(LocationProperties.to_json())

# convert the object into a dict
location_properties_dict = location_properties_instance.to_dict()
# create an instance of LocationProperties from a dict
location_properties_from_dict = LocationProperties.from_dict(location_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


