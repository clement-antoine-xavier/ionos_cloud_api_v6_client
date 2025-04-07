# FlowLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[FlowLog]**](FlowLog.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.flow_logs import FlowLogs

# TODO update the JSON string below
json = "{}"
# create an instance of FlowLogs from a JSON string
flow_logs_instance = FlowLogs.from_json(json)
# print the JSON string representation of the object
print(FlowLogs.to_json())

# convert the object into a dict
flow_logs_dict = flow_logs_instance.to_dict()
# create an instance of FlowLogs from a dict
flow_logs_from_dict = FlowLogs.from_dict(flow_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


