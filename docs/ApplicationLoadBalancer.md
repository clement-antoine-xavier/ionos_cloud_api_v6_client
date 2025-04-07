# ApplicationLoadBalancer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | The URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**ApplicationLoadBalancerProperties**](ApplicationLoadBalancerProperties.md) |  | 
**entities** | [**ApplicationLoadBalancerEntities**](ApplicationLoadBalancerEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_load_balancer import ApplicationLoadBalancer

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLoadBalancer from a JSON string
application_load_balancer_instance = ApplicationLoadBalancer.from_json(json)
# print the JSON string representation of the object
print(ApplicationLoadBalancer.to_json())

# convert the object into a dict
application_load_balancer_dict = application_load_balancer_instance.to_dict()
# create an instance of ApplicationLoadBalancer from a dict
application_load_balancer_from_dict = ApplicationLoadBalancer.from_dict(application_load_balancer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


