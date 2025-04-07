# GroupShares


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | Share representing groups and resource relationship | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[GroupShare]**](GroupShare.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.group_shares import GroupShares

# TODO update the JSON string below
json = "{}"
# create an instance of GroupShares from a JSON string
group_shares_instance = GroupShares.from_json(json)
# print the JSON string representation of the object
print(GroupShares.to_json())

# convert the object into a dict
group_shares_dict = group_shares_instance.to_dict()
# create an instance of GroupShares from a dict
group_shares_from_dict = GroupShares.from_dict(group_shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


