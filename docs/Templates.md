# Templates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Template]**](Template.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from openapi_client.models.templates import Templates

# TODO update the JSON string below
json = "{}"
# create an instance of Templates from a JSON string
templates_instance = Templates.from_json(json)
# print the JSON string representation of the object
print(Templates.to_json())

# convert the object into a dict
templates_dict = templates_instance.to_dict()
# create an instance of Templates from a dict
templates_from_dict = Templates.from_dict(templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


