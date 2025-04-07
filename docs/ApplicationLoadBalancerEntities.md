# ApplicationLoadBalancerEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwardingrules** | [**ApplicationLoadBalancerForwardingRules**](ApplicationLoadBalancerForwardingRules.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_load_balancer_entities import ApplicationLoadBalancerEntities

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLoadBalancerEntities from a JSON string
application_load_balancer_entities_instance = ApplicationLoadBalancerEntities.from_json(json)
# print the JSON string representation of the object
print(ApplicationLoadBalancerEntities.to_json())

# convert the object into a dict
application_load_balancer_entities_dict = application_load_balancer_entities_instance.to_dict()
# create an instance of ApplicationLoadBalancerEntities from a dict
application_load_balancer_entities_from_dict = ApplicationLoadBalancerEntities.from_dict(application_load_balancer_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


