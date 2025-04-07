# TargetGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[TargetGroup]**](TargetGroup.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset, specified in the request (if not is specified, 0 is used by default). | [optional] 
**limit** | **float** | The limit, specified in the request (if not specified, the endpoint&#39;s default pagination limit is used). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.target_groups import TargetGroups

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroups from a JSON string
target_groups_instance = TargetGroups.from_json(json)
# print the JSON string representation of the object
print(TargetGroups.to_json())

# convert the object into a dict
target_groups_dict = target_groups_instance.to_dict()
# create an instance of TargetGroups from a dict
target_groups_from_dict = TargetGroups.from_dict(target_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


