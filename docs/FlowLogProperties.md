# FlowLogProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The resource name. | 
**action** | **str** | Specifies the traffic action pattern. | 
**direction** | **str** | Specifies the traffic direction pattern. | 
**bucket** | **str** | The bucket name of an existing IONOS Cloud Object storage bucket. | 

## Example

```python
from ionos_cloud_api_v6_client.models.flow_log_properties import FlowLogProperties

# TODO update the JSON string below
json = "{}"
# create an instance of FlowLogProperties from a JSON string
flow_log_properties_instance = FlowLogProperties.from_json(json)
# print the JSON string representation of the object
print(FlowLogProperties.to_json())

# convert the object into a dict
flow_log_properties_dict = flow_log_properties_instance.to_dict()
# create an instance of FlowLogProperties from a dict
flow_log_properties_from_dict = FlowLogProperties.from_dict(flow_log_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


