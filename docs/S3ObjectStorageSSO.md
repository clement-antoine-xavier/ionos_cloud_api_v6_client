# S3ObjectStorageSSO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_url** | **str** | The Ionos object storage single sign on url | [optional] [readonly] 

## Example

```python
from openapi_client.models.s3_object_storage_sso import S3ObjectStorageSSO

# TODO update the JSON string below
json = "{}"
# create an instance of S3ObjectStorageSSO from a JSON string
s3_object_storage_sso_instance = S3ObjectStorageSSO.from_json(json)
# print the JSON string representation of the object
print(S3ObjectStorageSSO.to_json())

# convert the object into a dict
s3_object_storage_sso_dict = s3_object_storage_sso_instance.to_dict()
# create an instance of S3ObjectStorageSSO from a dict
s3_object_storage_sso_from_dict = S3ObjectStorageSSO.from_dict(s3_object_storage_sso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


