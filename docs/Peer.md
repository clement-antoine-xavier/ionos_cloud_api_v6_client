# Peer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the LAN connected to the Cross Connect. | [optional] 
**name** | **str** | Name of the LAN connected to the Cross Connect. | [optional] 
**datacenter_id** | **str** | Identifier of the virtual data center connected to the Cross Connect. | [optional] 
**datacenter_name** | **str** | Name of the virtual data center connected to the Cross Connect. | [optional] 
**location** | **str** | Location of the virtual data center connected to the Cross Connect. | [optional] 

## Example

```python
from openapi_client.models.peer import Peer

# TODO update the JSON string below
json = "{}"
# create an instance of Peer from a JSON string
peer_instance = Peer.from_json(json)
# print the JSON string representation of the object
print(Peer.to_json())

# convert the object into a dict
peer_dict = peer_instance.to_dict()
# create an instance of Peer from a dict
peer_from_dict = Peer.from_dict(peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


