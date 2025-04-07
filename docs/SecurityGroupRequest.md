# SecurityGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**SecurityGroupProperties**](SecurityGroupProperties.md) |  | 
**entities** | [**SecurityGroupEntitiesRequest**](SecurityGroupEntitiesRequest.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.security_group_request import SecurityGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroupRequest from a JSON string
security_group_request_instance = SecurityGroupRequest.from_json(json)
# print the JSON string representation of the object
print(SecurityGroupRequest.to_json())

# convert the object into a dict
security_group_request_dict = security_group_request_instance.to_dict()
# create an instance of SecurityGroupRequest from a dict
security_group_request_from_dict = SecurityGroupRequest.from_dict(security_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


