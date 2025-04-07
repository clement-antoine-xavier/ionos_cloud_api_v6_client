# UsersEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owns** | [**ResourcesUsers**](ResourcesUsers.md) |  | [optional] 
**groups** | [**GroupUsers**](GroupUsers.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.users_entities import UsersEntities

# TODO update the JSON string below
json = "{}"
# create an instance of UsersEntities from a JSON string
users_entities_instance = UsersEntities.from_json(json)
# print the JSON string representation of the object
print(UsersEntities.to_json())

# convert the object into a dict
users_entities_dict = users_entities_instance.to_dict()
# create an instance of UsersEntities from a dict
users_entities_from_dict = UsersEntities.from_dict(users_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


