# TargetGroupPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**properties** | [**TargetGroupProperties**](TargetGroupProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.target_group_put import TargetGroupPut

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroupPut from a JSON string
target_group_put_instance = TargetGroupPut.from_json(json)
# print the JSON string representation of the object
print(TargetGroupPut.to_json())

# convert the object into a dict
target_group_put_dict = target_group_put_instance.to_dict()
# create an instance of TargetGroupPut from a dict
target_group_put_from_dict = TargetGroupPut.from_dict(target_group_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


