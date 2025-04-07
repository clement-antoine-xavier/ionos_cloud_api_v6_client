# IpBlocks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[IpBlock]**](IpBlock.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset, specified in the request (if not is specified, 0 is used by default). | [optional] 
**limit** | **float** | The limit, specified in the request (if not specified, the endpoint&#39;s default pagination limit is used). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.ip_blocks import IpBlocks

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlocks from a JSON string
ip_blocks_instance = IpBlocks.from_json(json)
# print the JSON string representation of the object
print(IpBlocks.to_json())

# convert the object into a dict
ip_blocks_dict = ip_blocks_instance.to_dict()
# create an instance of IpBlocks from a dict
ip_blocks_from_dict = IpBlocks.from_dict(ip_blocks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


