# FlowLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**FlowLogProperties**](FlowLogProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.flow_log import FlowLog

# TODO update the JSON string below
json = "{}"
# create an instance of FlowLog from a JSON string
flow_log_instance = FlowLog.from_json(json)
# print the JSON string representation of the object
print(FlowLog.to_json())

# convert the object into a dict
flow_log_dict = flow_log_instance.to_dict()
# create an instance of FlowLog from a dict
flow_log_from_dict = FlowLog.from_dict(flow_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


