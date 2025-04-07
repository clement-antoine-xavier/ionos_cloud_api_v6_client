# LabelResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique representation of the label as a resource collection. | [optional] [readonly] 
**type** | **str** | The type of resource within a collection. | [optional] [readonly] 
**href** | **str** | URL to the collection representation (absolute path). | [optional] [readonly] 
**items** | [**List[LabelResource]**](LabelResource.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.label_resources import LabelResources

# TODO update the JSON string below
json = "{}"
# create an instance of LabelResources from a JSON string
label_resources_instance = LabelResources.from_json(json)
# print the JSON string representation of the object
print(LabelResources.to_json())

# convert the object into a dict
label_resources_dict = label_resources_instance.to_dict()
# create an instance of LabelResources from a dict
label_resources_from_dict = LabelResources.from_dict(label_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


