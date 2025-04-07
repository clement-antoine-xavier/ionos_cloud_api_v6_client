# ServerEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdroms** | [**Cdroms**](Cdroms.md) |  | [optional] 
**volumes** | [**AttachedVolumes**](AttachedVolumes.md) |  | [optional] 
**nics** | [**Nics**](Nics.md) |  | [optional] 
**securitygroups** | [**SecurityGroups**](SecurityGroups.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.server_entities import ServerEntities

# TODO update the JSON string below
json = "{}"
# create an instance of ServerEntities from a JSON string
server_entities_instance = ServerEntities.from_json(json)
# print the JSON string representation of the object
print(ServerEntities.to_json())

# convert the object into a dict
server_entities_dict = server_entities_instance.to_dict()
# create an instance of ServerEntities from a dict
server_entities_from_dict = ServerEntities.from_dict(server_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


