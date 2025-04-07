# PrivateCrossConnectProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Cross Connect. | [optional] 
**description** | **str** | Human-readable description of the Cross Connect. | [optional] 
**peers** | [**List[Peer]**](Peer.md) | Read-Only attribute. Lists LAN&#39;s connected to this Cross Connect. | [optional] [readonly] 
**connectable_datacenters** | [**List[ConnectableDatacenter]**](ConnectableDatacenter.md) | Read-Only attribute. Lists data centers that can be connected to this Cross Connect. If the Cross Connect is not connected to any LANs it lists all VDCs the user has access to. If the Cross Connect is connected to at least 1 LAN it lists all VDCs the user has access to in the location of the connected LAN. | [optional] [readonly] 

## Example

```python
from openapi_client.models.private_cross_connect_properties import PrivateCrossConnectProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCrossConnectProperties from a JSON string
private_cross_connect_properties_instance = PrivateCrossConnectProperties.from_json(json)
# print the JSON string representation of the object
print(PrivateCrossConnectProperties.to_json())

# convert the object into a dict
private_cross_connect_properties_dict = private_cross_connect_properties_instance.to_dict()
# create an instance of PrivateCrossConnectProperties from a dict
private_cross_connect_properties_from_dict = PrivateCrossConnectProperties.from_dict(private_cross_connect_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


