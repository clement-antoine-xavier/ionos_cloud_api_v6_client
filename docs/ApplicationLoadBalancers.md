# ApplicationLoadBalancers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[ApplicationLoadBalancer]**](ApplicationLoadBalancer.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.application_load_balancers import ApplicationLoadBalancers

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLoadBalancers from a JSON string
application_load_balancers_instance = ApplicationLoadBalancers.from_json(json)
# print the JSON string representation of the object
print(ApplicationLoadBalancers.to_json())

# convert the object into a dict
application_load_balancers_dict = application_load_balancers_instance.to_dict()
# create an instance of ApplicationLoadBalancers from a dict
application_load_balancers_from_dict = ApplicationLoadBalancers.from_dict(application_load_balancers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


