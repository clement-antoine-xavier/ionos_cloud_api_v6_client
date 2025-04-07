# Servers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Server]**](Server.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.servers import Servers

# TODO update the JSON string below
json = "{}"
# create an instance of Servers from a JSON string
servers_instance = Servers.from_json(json)
# print the JSON string representation of the object
print(Servers.to_json())

# convert the object into a dict
servers_dict = servers_instance.to_dict()
# create an instance of Servers from a dict
servers_from_dict = Servers.from_dict(servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


