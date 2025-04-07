# Images


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Image]**](Image.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.images import Images

# TODO update the JSON string below
json = "{}"
# create an instance of Images from a JSON string
images_instance = Images.from_json(json)
# print the JSON string representation of the object
print(Images.to_json())

# convert the object into a dict
images_dict = images_instance.to_dict()
# create an instance of Images from a dict
images_from_dict = Images.from_dict(images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


