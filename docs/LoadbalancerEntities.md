# LoadbalancerEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balancednics** | [**BalancedNics**](BalancedNics.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.loadbalancer_entities import LoadbalancerEntities

# TODO update the JSON string below
json = "{}"
# create an instance of LoadbalancerEntities from a JSON string
loadbalancer_entities_instance = LoadbalancerEntities.from_json(json)
# print the JSON string representation of the object
print(LoadbalancerEntities.to_json())

# convert the object into a dict
loadbalancer_entities_dict = loadbalancer_entities_instance.to_dict()
# create an instance of LoadbalancerEntities from a dict
loadbalancer_entities_from_dict = LoadbalancerEntities.from_dict(loadbalancer_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


