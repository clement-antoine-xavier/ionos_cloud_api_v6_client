# RequestTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.request_target import RequestTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTarget from a JSON string
request_target_instance = RequestTarget.from_json(json)
# print the JSON string representation of the object
print(RequestTarget.to_json())

# convert the object into a dict
request_target_dict = request_target_instance.to_dict()
# create an instance of RequestTarget from a dict
request_target_from_dict = RequestTarget.from_dict(request_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


