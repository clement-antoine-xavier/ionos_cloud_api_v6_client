# UserPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**UserPropertiesPost**](UserPropertiesPost.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.user_post import UserPost

# TODO update the JSON string below
json = "{}"
# create an instance of UserPost from a JSON string
user_post_instance = UserPost.from_json(json)
# print the JSON string representation of the object
print(UserPost.to_json())

# convert the object into a dict
user_post_dict = user_post_instance.to_dict()
# create an instance of UserPost from a dict
user_post_from_dict = UserPost.from_dict(user_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


