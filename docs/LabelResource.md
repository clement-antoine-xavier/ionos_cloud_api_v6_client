# LabelResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Label on a resource is identified using label key. | [optional] [readonly] 
**type** | **str** | The type of object that has been created. | [optional] [readonly] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**NoStateMetaData**](NoStateMetaData.md) |  | [optional] 
**properties** | [**LabelResourceProperties**](LabelResourceProperties.md) |  | 

## Example

```python
from openapi_client.models.label_resource import LabelResource

# TODO update the JSON string below
json = "{}"
# create an instance of LabelResource from a JSON string
label_resource_instance = LabelResource.from_json(json)
# print the JSON string representation of the object
print(LabelResource.to_json())

# convert the object into a dict
label_resource_dict = label_resource_instance.to_dict()
# create an instance of LabelResource from a dict
label_resource_from_dict = LabelResource.from_dict(label_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


