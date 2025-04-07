# Nics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Nic]**](Nic.md) | Array of items in the collection. | [optional] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.nics import Nics

# TODO update the JSON string below
json = "{}"
# create an instance of Nics from a JSON string
nics_instance = Nics.from_json(json)
# print the JSON string representation of the object
print(Nics.to_json())

# convert the object into a dict
nics_dict = nics_instance.to_dict()
# create an instance of Nics from a dict
nics_from_dict = Nics.from_dict(nics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


