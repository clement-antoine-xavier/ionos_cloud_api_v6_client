# NoStateMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | Resource&#39;s Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an &#39;ETag response header to requests which don&#39;t use &#39;depth&#39; parameter. | [optional] [readonly] 
**created_date** | **datetime** | The time when the resource was created. | [optional] [readonly] 
**created_by** | **str** | The user who has created the resource. | [optional] [readonly] 
**created_by_user_id** | **str** | The unique ID of the user who created the resource. | [optional] [readonly] 
**last_modified_date** | **datetime** | The last time the resource was modified. | [optional] [readonly] 
**last_modified_by** | **str** | The user who last modified the resource. | [optional] [readonly] 
**last_modified_by_user_id** | **str** | The unique ID of the user who last modified the resource. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.no_state_meta_data import NoStateMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of NoStateMetaData from a JSON string
no_state_meta_data_instance = NoStateMetaData.from_json(json)
# print the JSON string representation of the object
print(NoStateMetaData.to_json())

# convert the object into a dict
no_state_meta_data_dict = no_state_meta_data_instance.to_dict()
# create an instance of NoStateMetaData from a dict
no_state_meta_data_from_dict = NoStateMetaData.from_dict(no_state_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


