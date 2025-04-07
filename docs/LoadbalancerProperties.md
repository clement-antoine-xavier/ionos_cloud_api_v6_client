# LoadbalancerProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the  resource. | [optional] 
**ip** | **str** | IPv4 address of the loadbalancer. All attached NICs will inherit this IP. Leaving value null will assign IP automatically. | [optional] 
**dhcp** | **bool** | Indicates if the loadbalancer will reserve an IP using DHCP. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.loadbalancer_properties import LoadbalancerProperties

# TODO update the JSON string below
json = "{}"
# create an instance of LoadbalancerProperties from a JSON string
loadbalancer_properties_instance = LoadbalancerProperties.from_json(json)
# print the JSON string representation of the object
print(LoadbalancerProperties.to_json())

# convert the object into a dict
loadbalancer_properties_dict = loadbalancer_properties_instance.to_dict()
# create an instance of LoadbalancerProperties from a dict
loadbalancer_properties_from_dict = LoadbalancerProperties.from_dict(loadbalancer_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


