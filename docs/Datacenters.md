# Datacenters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Datacenter]**](Datacenter.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.datacenters import Datacenters

# TODO update the JSON string below
json = "{}"
# create an instance of Datacenters from a JSON string
datacenters_instance = Datacenters.from_json(json)
# print the JSON string representation of the object
print(Datacenters.to_json())

# convert the object into a dict
datacenters_dict = datacenters_instance.to_dict()
# create an instance of Datacenters from a dict
datacenters_from_dict = Datacenters.from_dict(datacenters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


