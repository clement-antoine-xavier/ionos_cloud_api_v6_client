# RequestStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**RequestStatusMetadata**](RequestStatusMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.request_status import RequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RequestStatus from a JSON string
request_status_instance = RequestStatus.from_json(json)
# print the JSON string representation of the object
print(RequestStatus.to_json())

# convert the object into a dict
request_status_dict = request_status_instance.to_dict()
# create an instance of RequestStatus from a dict
request_status_from_dict = RequestStatus.from_dict(request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


