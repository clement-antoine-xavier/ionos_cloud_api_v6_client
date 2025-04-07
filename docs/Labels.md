# Labels


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique representation of the label as a resource collection. | [optional] [readonly] 
**type** | **str** | The type of resource within a collection. | [optional] [readonly] 
**href** | **str** | URL to the collection representation (absolute path). | [optional] [readonly] 
**items** | [**List[Label]**](Label.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.labels import Labels

# TODO update the JSON string below
json = "{}"
# create an instance of Labels from a JSON string
labels_instance = Labels.from_json(json)
# print the JSON string representation of the object
print(Labels.to_json())

# convert the object into a dict
labels_dict = labels_instance.to_dict()
# create an instance of Labels from a dict
labels_from_dict = Labels.from_dict(labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


