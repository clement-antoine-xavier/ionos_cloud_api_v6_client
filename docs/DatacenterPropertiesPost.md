# DatacenterPropertiesPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the  resource. | [optional] 
**description** | **str** | A description for the datacenter, such as staging, production. | [optional] 
**location** | **str** | The physical location where the datacenter will be created. This will be where all of your servers live. Property cannot be modified after datacenter creation (disallowed in update requests). | 
**version** | **int** | The version of the data center; incremented with every change. | [optional] [readonly] 
**features** | **List[str]** | List of features supported by the location where this data center is provisioned. | [optional] [readonly] 
**sec_auth_protection** | **bool** | Boolean value representing if the data center requires extra protection, such as two-step verification. | [optional] 
**cpu_architecture** | [**List[CpuArchitectureProperties]**](CpuArchitectureProperties.md) | Array of features and CPU families available in a location | [optional] [readonly] 
**ipv6_cidr_block** | **str** | This value is either &#39;null&#39; or contains an automatically-assigned /56 IPv6 CIDR block if IPv6 is enabled on this virtual data center. It can neither be changed nor removed. | [optional] [readonly] 
**create_default_security_group** | **bool** | If true, a default security group, with predefined rules, will be created for the datacenter. Default value is false. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.datacenter_properties_post import DatacenterPropertiesPost

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterPropertiesPost from a JSON string
datacenter_properties_post_instance = DatacenterPropertiesPost.from_json(json)
# print the JSON string representation of the object
print(DatacenterPropertiesPost.to_json())

# convert the object into a dict
datacenter_properties_post_dict = datacenter_properties_post_instance.to_dict()
# create an instance of DatacenterPropertiesPost from a dict
datacenter_properties_post_from_dict = DatacenterPropertiesPost.from_dict(datacenter_properties_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


