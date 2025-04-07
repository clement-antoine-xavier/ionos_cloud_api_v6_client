# ContractProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **int** | The contract number. | [optional] [readonly] 
**owner** | **str** | The contract owner&#39;s user name. | [optional] [readonly] 
**status** | **str** | The contract status. | [optional] [readonly] 
**reg_domain** | **str** | The registration domain of the contract. | [optional] [readonly] 
**resource_limits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 

## Example

```python
from openapi_client.models.contract_properties import ContractProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ContractProperties from a JSON string
contract_properties_instance = ContractProperties.from_json(json)
# print the JSON string representation of the object
print(ContractProperties.to_json())

# convert the object into a dict
contract_properties_dict = contract_properties_instance.to_dict()
# create an instance of ContractProperties from a dict
contract_properties_from_dict = ContractProperties.from_dict(contract_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


