# TargetGroupHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_timeout** | **int** | The maximum time in milliseconds is to wait for a target to respond to a check. For target VMs with a &#39;Check Interval&#39; set, the smaller of the two values is used once the TCP connection is established. | [optional] 
**check_interval** | **int** | The interval in milliseconds between consecutive health checks; the default value is &#39;2000&#39;. | [optional] 
**retries** | **int** | The maximum number of attempts to reconnect to a target after a connection failure. The valid range is &#39;0 to 65535&#39;; the default value is &#39;3&#39;. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.target_group_health_check import TargetGroupHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroupHealthCheck from a JSON string
target_group_health_check_instance = TargetGroupHealthCheck.from_json(json)
# print the JSON string representation of the object
print(TargetGroupHealthCheck.to_json())

# convert the object into a dict
target_group_health_check_dict = target_group_health_check_instance.to_dict()
# create an instance of TargetGroupHealthCheck from a dict
target_group_health_check_from_dict = TargetGroupHealthCheck.from_dict(target_group_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


