# Volumes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Volume]**](Volume.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.volumes import Volumes

# TODO update the JSON string below
json = "{}"
# create an instance of Volumes from a JSON string
volumes_instance = Volumes.from_json(json)
# print the JSON string representation of the object
print(Volumes.to_json())

# convert the object into a dict
volumes_dict = volumes_instance.to_dict()
# create an instance of Volumes from a dict
volumes_from_dict = Volumes.from_dict(volumes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


