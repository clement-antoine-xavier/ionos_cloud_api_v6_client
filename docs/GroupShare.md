# GroupShare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | resource as generic type | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**properties** | [**GroupShareProperties**](GroupShareProperties.md) |  | 

## Example

```python
from openapi_client.models.group_share import GroupShare

# TODO update the JSON string below
json = "{}"
# create an instance of GroupShare from a JSON string
group_share_instance = GroupShare.from_json(json)
# print the JSON string representation of the object
print(GroupShare.to_json())

# convert the object into a dict
group_share_dict = group_share_instance.to_dict()
# create an instance of GroupShare from a dict
group_share_from_dict = GroupShare.from_dict(group_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


