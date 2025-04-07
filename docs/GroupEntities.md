# GroupEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**GroupMembers**](GroupMembers.md) |  | [optional] 
**resources** | [**ResourceGroups**](ResourceGroups.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_entities import GroupEntities

# TODO update the JSON string below
json = "{}"
# create an instance of GroupEntities from a JSON string
group_entities_instance = GroupEntities.from_json(json)
# print the JSON string representation of the object
print(GroupEntities.to_json())

# convert the object into a dict
group_entities_dict = group_entities_instance.to_dict()
# create an instance of GroupEntities from a dict
group_entities_from_dict = GroupEntities.from_dict(group_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


