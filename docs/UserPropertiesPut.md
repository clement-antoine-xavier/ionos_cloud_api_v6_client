# UserPropertiesPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firstname** | **str** | The first name of the user. | [optional] 
**lastname** | **str** | The last name of the user. | [optional] 
**email** | **str** | The email address of the user. | [optional] 
**password** | **str** | password of the user | [optional] 
**administrator** | **bool** | Indicates if the user has admin rights. | [optional] 
**force_sec_auth** | **bool** | Indicates if secure authentication should be forced on the user. | [optional] 
**sec_auth_active** | **bool** | Indicates if secure authentication is active for the user. | [optional] 
**active** | **bool** | Indicates if the user is active. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.user_properties_put import UserPropertiesPut

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertiesPut from a JSON string
user_properties_put_instance = UserPropertiesPut.from_json(json)
# print the JSON string representation of the object
print(UserPropertiesPut.to_json())

# convert the object into a dict
user_properties_put_dict = user_properties_put_instance.to_dict()
# create an instance of UserPropertiesPut from a dict
user_properties_put_from_dict = UserPropertiesPut.from_dict(user_properties_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


