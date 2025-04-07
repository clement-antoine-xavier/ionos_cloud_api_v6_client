# NicEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flowlogs** | [**FlowLogs**](FlowLogs.md) |  | [optional] 
**firewallrules** | [**FirewallRules**](FirewallRules.md) |  | [optional] 
**securitygroups** | [**SecurityGroups**](SecurityGroups.md) |  | [optional] 

## Example

```python
from openapi_client.models.nic_entities import NicEntities

# TODO update the JSON string below
json = "{}"
# create an instance of NicEntities from a JSON string
nic_entities_instance = NicEntities.from_json(json)
# print the JSON string representation of the object
print(NicEntities.to_json())

# convert the object into a dict
nic_entities_dict = nic_entities_instance.to_dict()
# create an instance of NicEntities from a dict
nic_entities_from_dict = NicEntities.from_dict(nic_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


