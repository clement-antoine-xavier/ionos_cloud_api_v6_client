# SecurityGroupEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**FirewallRules**](FirewallRules.md) |  | [optional] 
**nics** | [**Nics**](Nics.md) |  | [optional] 
**servers** | [**Servers**](Servers.md) |  | [optional] 

## Example

```python
from openapi_client.models.security_group_entities import SecurityGroupEntities

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroupEntities from a JSON string
security_group_entities_instance = SecurityGroupEntities.from_json(json)
# print the JSON string representation of the object
print(SecurityGroupEntities.to_json())

# convert the object into a dict
security_group_entities_dict = security_group_entities_instance.to_dict()
# create an instance of SecurityGroupEntities from a dict
security_group_entities_from_dict = SecurityGroupEntities.from_dict(security_group_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


