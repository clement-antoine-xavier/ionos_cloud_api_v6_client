# S3Bucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Object storage bucket. | 

## Example

```python
from openapi_client.models.s3_bucket import S3Bucket

# TODO update the JSON string below
json = "{}"
# create an instance of S3Bucket from a JSON string
s3_bucket_instance = S3Bucket.from_json(json)
# print the JSON string representation of the object
print(S3Bucket.to_json())

# convert the object into a dict
s3_bucket_dict = s3_bucket_instance.to_dict()
# create an instance of S3Bucket from a dict
s3_bucket_from_dict = S3Bucket.from_dict(s3_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


