# S3KeyProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** | Secret of the Object storage key. | [optional] [readonly] 
**active** | **bool** | Denotes weather the Object storage key is active. | [optional] 

## Example

```python
from openapi_client.models.s3_key_properties import S3KeyProperties

# TODO update the JSON string below
json = "{}"
# create an instance of S3KeyProperties from a JSON string
s3_key_properties_instance = S3KeyProperties.from_json(json)
# print the JSON string representation of the object
print(S3KeyProperties.to_json())

# convert the object into a dict
s3_key_properties_dict = s3_key_properties_instance.to_dict()
# create an instance of S3KeyProperties from a dict
s3_key_properties_from_dict = S3KeyProperties.from_dict(s3_key_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


