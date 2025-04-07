# BalancedNics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Nic]**](Nic.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.balanced_nics import BalancedNics

# TODO update the JSON string below
json = "{}"
# create an instance of BalancedNics from a JSON string
balanced_nics_instance = BalancedNics.from_json(json)
# print the JSON string representation of the object
print(BalancedNics.to_json())

# convert the object into a dict
balanced_nics_dict = balanced_nics_instance.to_dict()
# create an instance of BalancedNics from a dict
balanced_nics_from_dict = BalancedNics.from_dict(balanced_nics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


