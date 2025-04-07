# SecurityGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[SecurityGroup]**](SecurityGroup.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.security_groups import SecurityGroups

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroups from a JSON string
security_groups_instance = SecurityGroups.from_json(json)
# print the JSON string representation of the object
print(SecurityGroups.to_json())

# convert the object into a dict
security_groups_dict = security_groups_instance.to_dict()
# create an instance of SecurityGroups from a dict
security_groups_from_dict = SecurityGroups.from_dict(security_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


