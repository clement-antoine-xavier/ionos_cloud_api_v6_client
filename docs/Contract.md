# Contract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Type**](Type.md) | The type of the resource. | [optional] 
**properties** | [**ContractProperties**](ContractProperties.md) |  | 

## Example

```python
from ionos_cloud_api_v6_client.models.contract import Contract

# TODO update the JSON string below
json = "{}"
# create an instance of Contract from a JSON string
contract_instance = Contract.from_json(json)
# print the JSON string representation of the object
print(Contract.to_json())

# convert the object into a dict
contract_dict = contract_instance.to_dict()
# create an instance of Contract from a dict
contract_from_dict = Contract.from_dict(contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


