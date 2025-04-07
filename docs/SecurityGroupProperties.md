# SecurityGroupProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the security group. | 
**description** | **str** | The description of the security group. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.security_group_properties import SecurityGroupProperties

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroupProperties from a JSON string
security_group_properties_instance = SecurityGroupProperties.from_json(json)
# print the JSON string representation of the object
print(SecurityGroupProperties.to_json())

# convert the object into a dict
security_group_properties_dict = security_group_properties_instance.to_dict()
# create an instance of SecurityGroupProperties from a dict
security_group_properties_from_dict = SecurityGroupProperties.from_dict(security_group_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


