# ErrorMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Application internal error code. | [optional] [readonly] 
**message** | **str** | A human-readable message. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.error_message import ErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessage from a JSON string
error_message_instance = ErrorMessage.from_json(json)
# print the JSON string representation of the object
print(ErrorMessage.to_json())

# convert the object into a dict
error_message_dict = error_message_instance.to_dict()
# create an instance of ErrorMessage from a dict
error_message_from_dict = ErrorMessage.from_dict(error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


