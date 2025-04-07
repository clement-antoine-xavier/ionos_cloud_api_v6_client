# UserPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] 
**properties** | [**UserPropertiesPut**](UserPropertiesPut.md) |  | 

## Example

```python
from openapi_client.models.user_put import UserPut

# TODO update the JSON string below
json = "{}"
# create an instance of UserPut from a JSON string
user_put_instance = UserPut.from_json(json)
# print the JSON string representation of the object
print(UserPut.to_json())

# convert the object into a dict
user_put_dict = user_put_instance.to_dict()
# create an instance of UserPut from a dict
user_put_from_dict = UserPut.from_dict(user_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


