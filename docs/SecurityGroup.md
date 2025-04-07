# SecurityGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**SecurityGroupProperties**](SecurityGroupProperties.md) |  | 
**entities** | [**SecurityGroupEntities**](SecurityGroupEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.security_group import SecurityGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroup from a JSON string
security_group_instance = SecurityGroup.from_json(json)
# print the JSON string representation of the object
print(SecurityGroup.to_json())

# convert the object into a dict
security_group_dict = security_group_instance.to_dict()
# create an instance of SecurityGroup from a dict
security_group_from_dict = SecurityGroup.from_dict(security_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


