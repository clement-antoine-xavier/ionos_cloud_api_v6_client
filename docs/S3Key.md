# S3Key


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of the resource. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**S3KeyMetadata**](S3KeyMetadata.md) |  | [optional] 
**properties** | [**S3KeyProperties**](S3KeyProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.s3_key import S3Key

# TODO update the JSON string below
json = "{}"
# create an instance of S3Key from a JSON string
s3_key_instance = S3Key.from_json(json)
# print the JSON string representation of the object
print(S3Key.to_json())

# convert the object into a dict
s3_key_dict = s3_key_instance.to_dict()
# create an instance of S3Key from a dict
s3_key_from_dict = S3Key.from_dict(s3_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


