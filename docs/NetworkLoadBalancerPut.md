# NetworkLoadBalancerPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**properties** | [**NetworkLoadBalancerProperties**](NetworkLoadBalancerProperties.md) |  | 

## Example

```python
from openapi_client.models.network_load_balancer_put import NetworkLoadBalancerPut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerPut from a JSON string
network_load_balancer_put_instance = NetworkLoadBalancerPut.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerPut.to_json())

# convert the object into a dict
network_load_balancer_put_dict = network_load_balancer_put_instance.to_dict()
# create an instance of NetworkLoadBalancerPut from a dict
network_load_balancer_put_from_dict = NetworkLoadBalancerPut.from_dict(network_load_balancer_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


