# IPFailover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**nic_uuid** | **str** |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.ip_failover import IPFailover

# TODO update the JSON string below
json = "{}"
# create an instance of IPFailover from a JSON string
ip_failover_instance = IPFailover.from_json(json)
# print the JSON string representation of the object
print(IPFailover.to_json())

# convert the object into a dict
ip_failover_dict = ip_failover_instance.to_dict()
# create an instance of IPFailover from a dict
ip_failover_from_dict = IPFailover.from_dict(ip_failover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


