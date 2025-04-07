# TargetGroupProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The target group name. | 
**algorithm** | **str** | The balancing algorithm. A balancing algorithm consists of predefined rules with the logic that a load balancer uses to distribute network traffic between servers.  - **Round Robin**: Targets are served alternately according to their weighting.  - **Least Connection**: The target with the least active connection is served.  - **Random**: The targets are served based on a consistent pseudorandom algorithm.  - **Source IP**: It is ensured that the same client IP address reaches the same target. | 
**protocol** | **str** | The forwarding protocol. Only the value &#39;HTTP&#39; is allowed. | 
**protocol_version** | **str** | The forwarding protocol version. Value is ignored when protocol is not &#39;HTTP&#39;. | [optional] 
**targets** | [**List[TargetGroupTarget]**](TargetGroupTarget.md) | Array of items in the collection. | [optional] 
**health_check** | [**TargetGroupHealthCheck**](TargetGroupHealthCheck.md) |  | [optional] 
**http_health_check** | [**TargetGroupHttpHealthCheck**](TargetGroupHttpHealthCheck.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.target_group_properties import TargetGroupProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroupProperties from a JSON string
target_group_properties_instance = TargetGroupProperties.from_json(json)
# print the JSON string representation of the object
print(TargetGroupProperties.to_json())

# convert the object into a dict
target_group_properties_dict = target_group_properties_instance.to_dict()
# create an instance of TargetGroupProperties from a dict
target_group_properties_from_dict = TargetGroupProperties.from_dict(target_group_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


