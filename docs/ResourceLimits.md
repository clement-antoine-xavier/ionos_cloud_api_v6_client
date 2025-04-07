# ResourceLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores_per_server** | **int** | The maximum number of CPU cores per server. | 
**cores_per_contract** | **int** | The maximum number of CPU cores per contract. | 
**cores_provisioned** | **int** | The number of CPU cores provisioned. | 
**ram_per_server** | **int** | The maximum amount of RAM (in MB) that can be provisioned for a particular server under this contract. | 
**ram_per_contract** | **int** | The maximum amount of RAM (in MB) that can be provisioned under this contract. | 
**ram_provisioned** | **int** | The amount of RAM (in MB) provisioned under this contract. | 
**hdd_limit_per_volume** | **int** | The maximum size (in MB) of an idividual hard disk volume. | 
**hdd_limit_per_contract** | **int** | The maximum amount of disk space (in MB) that can be provided under this contract. | 
**hdd_volume_provisioned** | **int** | The amount of hard disk space (in MB) that is currently provisioned. | 
**ssd_limit_per_volume** | **int** | The maximum size (in MB) of an individual solid state disk volume. | 
**ssd_limit_per_contract** | **int** | The maximum amount of solid state disk space (in MB) that can be provisioned under this contract. | 
**ssd_volume_provisioned** | **int** | The amount of solid state disk space (in MB) that is currently provisioned. | 
**das_volume_provisioned** | **int** | The amount of DAS disk space (in MB) in a Cube server that is currently provisioned. | 
**reservable_ips** | **int** | The maximum number of static public IP addresses that can be reserved by this customer across contracts. | 
**reserved_ips_on_contract** | **int** | The maximum number of static public IP addresses that can be reserved for this contract. | 
**reserved_ips_in_use** | **int** | The number of static public IP addresses in use. | 
**k8s_cluster_limit_total** | **int** | The maximum number of Kubernetes clusters that can be created under this contract. | 
**k8s_clusters_provisioned** | **int** | The amount of Kubernetes clusters that is currently provisioned. | 
**nlb_limit_total** | **int** | The NLB total limit. | 
**nlb_provisioned** | **int** | The NLBs provisioned. | 
**nat_gateway_limit_total** | **int** | The NAT Gateway total limit. | 
**nat_gateway_provisioned** | **int** | The NAT Gateways provisioned. | 
**security_groups_per_vdc** | **int** | The maximum number of security groups per VDC. | 
**security_groups_per_resource** | **int** | The maximum number of security groups that can be attached to a NIC or a VM individually. For example, a user can have maximum 10 security groups per NIC and 10 per VM. | 
**rules_per_security_group** | **int** | The maximum number of rules per security group. | 

## Example

```python
from openapi_client.models.resource_limits import ResourceLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLimits from a JSON string
resource_limits_instance = ResourceLimits.from_json(json)
# print the JSON string representation of the object
print(ResourceLimits.to_json())

# convert the object into a dict
resource_limits_dict = resource_limits_instance.to_dict()
# create an instance of ResourceLimits from a dict
resource_limits_from_dict = ResourceLimits.from_dict(resource_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


