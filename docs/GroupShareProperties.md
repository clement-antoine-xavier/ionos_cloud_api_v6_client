# GroupShareProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_privilege** | **bool** | edit privilege on a resource | [optional] 
**share_privilege** | **bool** | share privilege on a resource | [optional] 

## Example

```python
from openapi_client.models.group_share_properties import GroupShareProperties

# TODO update the JSON string below
json = "{}"
# create an instance of GroupShareProperties from a JSON string
group_share_properties_instance = GroupShareProperties.from_json(json)
# print the JSON string representation of the object
print(GroupShareProperties.to_json())

# convert the object into a dict
group_share_properties_dict = group_share_properties_instance.to_dict()
# create an instance of GroupShareProperties from a dict
group_share_properties_from_dict = GroupShareProperties.from_dict(group_share_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


