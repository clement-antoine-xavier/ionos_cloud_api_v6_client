# S3KeyMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | Resource&#39;s Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an &#39;ETag response header to requests which don&#39;t use &#39;depth&#39; parameter. | [optional] [readonly] 
**created_date** | **datetime** | The time when the Object storage key was created. | [optional] [readonly] 
**created_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly] 
**created_by_user_id** | **str** | The unique ID of the user who created the Object storage key. | [optional] [readonly] 
**last_modified_date** | **datetime** | The last time the Object storage key was modified. | [optional] [readonly] 
**last_modified_by** | **str** | Unique name of the identity that last modified the Object storage key. | [optional] [readonly] 
**last_modified_by_user_id** | **str** | The unique ID of the user who last modified the Object storage key. | [optional] [readonly] 

## Example

```python
from openapi_client.models.s3_key_metadata import S3KeyMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of S3KeyMetadata from a JSON string
s3_key_metadata_instance = S3KeyMetadata.from_json(json)
# print the JSON string representation of the object
print(S3KeyMetadata.to_json())

# convert the object into a dict
s3_key_metadata_dict = s3_key_metadata_instance.to_dict()
# create an instance of S3KeyMetadata from a dict
s3_key_metadata_from_dict = S3KeyMetadata.from_dict(s3_key_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


