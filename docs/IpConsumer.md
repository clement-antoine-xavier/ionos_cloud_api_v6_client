# IpConsumer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**mac** | **str** |  | [optional] 
**nic_id** | **str** |  | [optional] 
**server_id** | **str** |  | [optional] 
**server_name** | **str** |  | [optional] 
**datacenter_id** | **str** |  | [optional] 
**datacenter_name** | **str** |  | [optional] 
**k8s_node_pool_uuid** | **str** |  | [optional] 
**k8s_cluster_uuid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ip_consumer import IpConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of IpConsumer from a JSON string
ip_consumer_instance = IpConsumer.from_json(json)
# print the JSON string representation of the object
print(IpConsumer.to_json())

# convert the object into a dict
ip_consumer_dict = ip_consumer_instance.to_dict()
# create an instance of IpConsumer from a dict
ip_consumer_from_dict = IpConsumer.from_dict(ip_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


