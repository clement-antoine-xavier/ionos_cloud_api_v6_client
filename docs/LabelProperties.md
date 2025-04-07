# LabelProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A label key | [optional] 
**value** | **str** | A label value | [optional] 
**resource_id** | **str** | The ID of the resource. | [optional] 
**resource_type** | **str** | The type of the resource on which the label is applied. | [optional] 
**resource_href** | **str** | URL to the Resource (absolute path) on which the label is applied. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.label_properties import LabelProperties

# TODO update the JSON string below
json = "{}"
# create an instance of LabelProperties from a JSON string
label_properties_instance = LabelProperties.from_json(json)
# print the JSON string representation of the object
print(LabelProperties.to_json())

# convert the object into a dict
label_properties_dict = label_properties_instance.to_dict()
# create an instance of LabelProperties from a dict
label_properties_from_dict = LabelProperties.from_dict(label_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


