# ResourcesUsers

Resources owned by a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of the resource. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Resource]**](Resource.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from openapi_client.models.resources_users import ResourcesUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesUsers from a JSON string
resources_users_instance = ResourcesUsers.from_json(json)
# print the JSON string representation of the object
print(ResourcesUsers.to_json())

# convert the object into a dict
resources_users_dict = resources_users_instance.to_dict()
# create an instance of ResourcesUsers from a dict
resources_users_from_dict = ResourcesUsers.from_dict(resources_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


