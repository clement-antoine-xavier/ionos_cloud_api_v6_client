# DatacenterEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | [**Servers**](Servers.md) |  | [optional] 
**volumes** | [**Volumes**](Volumes.md) |  | [optional] 
**loadbalancers** | [**Loadbalancers**](Loadbalancers.md) |  | [optional] 
**lans** | [**Lans**](Lans.md) |  | [optional] 
**networkloadbalancers** | [**NetworkLoadBalancers**](NetworkLoadBalancers.md) |  | [optional] 
**natgateways** | [**NatGateways**](NatGateways.md) |  | [optional] 
**securitygroups** | [**SecurityGroups**](SecurityGroups.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.datacenter_entities import DatacenterEntities

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterEntities from a JSON string
datacenter_entities_instance = DatacenterEntities.from_json(json)
# print the JSON string representation of the object
print(DatacenterEntities.to_json())

# convert the object into a dict
datacenter_entities_dict = datacenter_entities_instance.to_dict()
# create an instance of DatacenterEntities from a dict
datacenter_entities_from_dict = DatacenterEntities.from_dict(datacenter_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


