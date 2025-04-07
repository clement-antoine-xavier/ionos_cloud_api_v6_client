# Contracts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Contract]**](Contract.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from openapi_client.models.contracts import Contracts

# TODO update the JSON string below
json = "{}"
# create an instance of Contracts from a JSON string
contracts_instance = Contracts.from_json(json)
# print the JSON string representation of the object
print(Contracts.to_json())

# convert the object into a dict
contracts_dict = contracts_instance.to_dict()
# create an instance of Contracts from a dict
contracts_from_dict = Contracts.from_dict(contracts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


