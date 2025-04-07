# NetworkLoadBalancers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[NetworkLoadBalancer]**](NetworkLoadBalancer.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.network_load_balancers import NetworkLoadBalancers

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancers from a JSON string
network_load_balancers_instance = NetworkLoadBalancers.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancers.to_json())

# convert the object into a dict
network_load_balancers_dict = network_load_balancers_instance.to_dict()
# create an instance of NetworkLoadBalancers from a dict
network_load_balancers_from_dict = NetworkLoadBalancers.from_dict(network_load_balancers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


