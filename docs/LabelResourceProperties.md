# LabelResourceProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A label key | [optional] 
**value** | **str** | A label value | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.label_resource_properties import LabelResourceProperties

# TODO update the JSON string below
json = "{}"
# create an instance of LabelResourceProperties from a JSON string
label_resource_properties_instance = LabelResourceProperties.from_json(json)
# print the JSON string representation of the object
print(LabelResourceProperties.to_json())

# convert the object into a dict
label_resource_properties_dict = label_resource_properties_instance.to_dict()
# create an instance of LabelResourceProperties from a dict
label_resource_properties_from_dict = LabelResourceProperties.from_dict(label_resource_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


