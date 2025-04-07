# AttachedVolumes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Volume]**](Volume.md) | Array of items in the collection. | [optional] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.attached_volumes import AttachedVolumes

# TODO update the JSON string below
json = "{}"
# create an instance of AttachedVolumes from a JSON string
attached_volumes_instance = AttachedVolumes.from_json(json)
# print the JSON string representation of the object
print(AttachedVolumes.to_json())

# convert the object into a dict
attached_volumes_dict = attached_volumes_instance.to_dict()
# create an instance of AttachedVolumes from a dict
attached_volumes_from_dict = AttachedVolumes.from_dict(attached_volumes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


