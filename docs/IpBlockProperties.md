# IpBlockProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **List[str]** | Collection of IPs, associated with the IP Block. | [optional] [readonly] 
**location** | **str** | Location of that IP block. Property cannot be modified after it is created (disallowed in update requests). | 
**size** | **int** | The size of the IP block. | 
**name** | **str** | The name of the  resource. | [optional] 
**ip_consumers** | [**List[IpConsumer]**](IpConsumer.md) | Read-Only attribute. Lists consumption detail for an individual IP | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.ip_block_properties import IpBlockProperties

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockProperties from a JSON string
ip_block_properties_instance = IpBlockProperties.from_json(json)
# print the JSON string representation of the object
print(IpBlockProperties.to_json())

# convert the object into a dict
ip_block_properties_dict = ip_block_properties_instance.to_dict()
# create an instance of IpBlockProperties from a dict
ip_block_properties_from_dict = IpBlockProperties.from_dict(ip_block_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


