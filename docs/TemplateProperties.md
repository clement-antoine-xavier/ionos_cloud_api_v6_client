# TemplateProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name. | 
**cores** | **float** | The CPU cores count. | 
**ram** | **float** | The RAM size in MB. | 
**storage_size** | **float** | The storage size in GB. | 
**category** | **str** | The description of the template. | 

## Example

```python
from openapi_client.models.template_properties import TemplateProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateProperties from a JSON string
template_properties_instance = TemplateProperties.from_json(json)
# print the JSON string representation of the object
print(TemplateProperties.to_json())

# convert the object into a dict
template_properties_dict = template_properties_instance.to_dict()
# create an instance of TemplateProperties from a dict
template_properties_from_dict = TemplateProperties.from_dict(template_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


