# Label


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Label is identified using standard URN. | [optional] [readonly] 
**type** | **str** | The type of object that has been created. | [optional] [readonly] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**NoStateMetaData**](NoStateMetaData.md) |  | [optional] 
**properties** | [**LabelProperties**](LabelProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.label import Label

# TODO update the JSON string below
json = "{}"
# create an instance of Label from a JSON string
label_instance = Label.from_json(json)
# print the JSON string representation of the object
print(Label.to_json())

# convert the object into a dict
label_dict = label_instance.to_dict()
# create an instance of Label from a dict
label_from_dict = Label.from_dict(label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


