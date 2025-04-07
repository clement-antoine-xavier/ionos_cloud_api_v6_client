# ConnectableDatacenter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the virtual data center that can be connected to the Cross Connect. | [optional] 
**name** | **str** | Name of the virtual data center that can be connected to the Cross Connect. | [optional] 
**location** | **str** | Location of the virtual data center that can be connected to the Cross Connect. | [optional] 

## Example

```python
from openapi_client.models.connectable_datacenter import ConnectableDatacenter

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectableDatacenter from a JSON string
connectable_datacenter_instance = ConnectableDatacenter.from_json(json)
# print the JSON string representation of the object
print(ConnectableDatacenter.to_json())

# convert the object into a dict
connectable_datacenter_dict = connectable_datacenter_instance.to_dict()
# create an instance of ConnectableDatacenter from a dict
connectable_datacenter_from_dict = ConnectableDatacenter.from_dict(connectable_datacenter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


