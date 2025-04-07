# S3Keys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of the resource. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[S3Key]**](S3Key.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.s3_keys import S3Keys

# TODO update the JSON string below
json = "{}"
# create an instance of S3Keys from a JSON string
s3_keys_instance = S3Keys.from_json(json)
# print the JSON string representation of the object
print(S3Keys.to_json())

# convert the object into a dict
s3_keys_dict = s3_keys_instance.to_dict()
# create an instance of S3Keys from a dict
s3_keys_from_dict = S3Keys.from_dict(s3_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


