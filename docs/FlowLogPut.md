# FlowLogPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**properties** | [**FlowLogProperties**](FlowLogProperties.md) |  | 

## Example

```python
from openapi_client.models.flow_log_put import FlowLogPut

# TODO update the JSON string below
json = "{}"
# create an instance of FlowLogPut from a JSON string
flow_log_put_instance = FlowLogPut.from_json(json)
# print the JSON string representation of the object
print(FlowLogPut.to_json())

# convert the object into a dict
flow_log_put_dict = flow_log_put_instance.to_dict()
# create an instance of FlowLogPut from a dict
flow_log_put_from_dict = FlowLogPut.from_dict(flow_log_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


