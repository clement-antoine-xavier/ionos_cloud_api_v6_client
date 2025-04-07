# ResourceGroups

Resources assigned to this group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of the resource. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Resource]**](Resource.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from openapi_client.models.resource_groups import ResourceGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGroups from a JSON string
resource_groups_instance = ResourceGroups.from_json(json)
# print the JSON string representation of the object
print(ResourceGroups.to_json())

# convert the object into a dict
resource_groups_dict = resource_groups_instance.to_dict()
# create an instance of ResourceGroups from a dict
resource_groups_from_dict = ResourceGroups.from_dict(resource_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


