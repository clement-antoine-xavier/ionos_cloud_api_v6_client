# Requests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Request]**](Request.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset, specified in the request (if not is specified, 0 is used by default). | 
**limit** | **float** | The limit, specified in the request (if not specified, the endpoint&#39;s default pagination limit is used). | 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | 

## Example

```python
from openapi_client.models.requests import Requests

# TODO update the JSON string below
json = "{}"
# create an instance of Requests from a JSON string
requests_instance = Requests.from_json(json)
# print the JSON string representation of the object
print(Requests.to_json())

# convert the object into a dict
requests_dict = requests_instance.to_dict()
# create an instance of Requests from a dict
requests_from_dict = Requests.from_dict(requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


