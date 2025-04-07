# SecurityGroupEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**FirewallRules**](FirewallRules.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.security_group_entities_request import SecurityGroupEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroupEntitiesRequest from a JSON string
security_group_entities_request_instance = SecurityGroupEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(SecurityGroupEntitiesRequest.to_json())

# convert the object into a dict
security_group_entities_request_dict = security_group_entities_request_instance.to_dict()
# create an instance of SecurityGroupEntitiesRequest from a dict
security_group_entities_request_from_dict = SecurityGroupEntitiesRequest.from_dict(security_group_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


