# UserProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firstname** | **str** | The first name of the user. | [optional] 
**lastname** | **str** | The last name of the user. | [optional] 
**email** | **str** | The email address of the user. | [optional] 
**administrator** | **bool** | Indicates if the user has admin rights. | [optional] 
**force_sec_auth** | **bool** | Indicates if secure authentication should be forced on the user. | [optional] 
**sec_auth_active** | **bool** | Indicates if secure authentication is active for the user. | [optional] 
**s3_canonical_user_id** | **str** | Canonical (Object storage) ID of the user for a given identity. | [optional] 
**active** | **bool** | Indicates if the user is active. | [optional] 

## Example

```python
from openapi_client.models.user_properties import UserProperties

# TODO update the JSON string below
json = "{}"
# create an instance of UserProperties from a JSON string
user_properties_instance = UserProperties.from_json(json)
# print the JSON string representation of the object
print(UserProperties.to_json())

# convert the object into a dict
user_properties_dict = user_properties_instance.to_dict()
# create an instance of UserProperties from a dict
user_properties_from_dict = UserProperties.from_dict(user_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


