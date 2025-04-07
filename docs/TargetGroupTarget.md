# TargetGroupTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IP address of the balanced target. | 
**port** | **int** | The port of the balanced target service; the valid range is 1 to 65535. | 
**weight** | **int** | The traffic is distributed proportionally to target weight, which is the ratio of the total weight of all targets. A target with higher weight receives a larger share of traffic. The valid range is from 0 to 256; the default value is &#39;1&#39;. Targets with a weight of &#39;0&#39; do not participate in load balancing but still accept persistent connections. We recommend using values in the middle range to leave room for later adjustments. | 
**proxy_protocol** | **str** | Proxy protocol version. | [optional] [default to 'none']
**health_check_enabled** | **bool** | When the health check is enabled, the target is available only when it accepts regular TCP or HTTP connection attempts for state checking. The state check consists of one connection attempt with the target&#39;s address and port. The default value is &#39;TRUE&#39;. | [optional] 
**maintenance_enabled** | **bool** | When the maintenance mode is enabled, the target is prevented from receiving traffic; the default value is &#39;FALSE&#39;. | [optional] 

## Example

```python
from openapi_client.models.target_group_target import TargetGroupTarget

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroupTarget from a JSON string
target_group_target_instance = TargetGroupTarget.from_json(json)
# print the JSON string representation of the object
print(TargetGroupTarget.to_json())

# convert the object into a dict
target_group_target_dict = target_group_target_instance.to_dict()
# create an instance of TargetGroupTarget from a dict
target_group_target_from_dict = TargetGroupTarget.from_dict(target_group_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


