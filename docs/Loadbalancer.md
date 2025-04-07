# Loadbalancer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**LoadbalancerProperties**](LoadbalancerProperties.md) |  | 
**entities** | [**LoadbalancerEntities**](LoadbalancerEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.loadbalancer import Loadbalancer

# TODO update the JSON string below
json = "{}"
# create an instance of Loadbalancer from a JSON string
loadbalancer_instance = Loadbalancer.from_json(json)
# print the JSON string representation of the object
print(Loadbalancer.to_json())

# convert the object into a dict
loadbalancer_dict = loadbalancer_instance.to_dict()
# create an instance of Loadbalancer from a dict
loadbalancer_from_dict = Loadbalancer.from_dict(loadbalancer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


