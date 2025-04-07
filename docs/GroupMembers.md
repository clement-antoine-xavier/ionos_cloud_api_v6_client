# GroupMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[User]**](User.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from openapi_client.models.group_members import GroupMembers

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembers from a JSON string
group_members_instance = GroupMembers.from_json(json)
# print the JSON string representation of the object
print(GroupMembers.to_json())

# convert the object into a dict
group_members_dict = group_members_instance.to_dict()
# create an instance of GroupMembers from a dict
group_members_from_dict = GroupMembers.from_dict(group_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


