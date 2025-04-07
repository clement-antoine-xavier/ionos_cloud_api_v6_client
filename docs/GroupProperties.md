# GroupProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource. | [optional] 
**create_datacenter** | **bool** | Create data center privilege. | [optional] 
**create_snapshot** | **bool** | Create snapshot privilege. | [optional] 
**reserve_ip** | **bool** | Reserve IP block privilege. | [optional] 
**access_activity_log** | **bool** | Activity log access privilege. | [optional] 
**create_pcc** | **bool** | User privilege to create a cross connect. | [optional] 
**s3_privilege** | **bool** | S3 privilege. | [optional] 
**create_backup_unit** | **bool** | Create backup unit privilege. | [optional] 
**create_internet_access** | **bool** | Create internet access privilege. | [optional] 
**create_k8s_cluster** | **bool** | Create Kubernetes cluster privilege. | [optional] 
**create_flow_log** | **bool** | Create Flow Logs privilege. | [optional] 
**access_and_manage_monitoring** | **bool** | Privilege for a group to access and manage monitoring related functionality (access metrics, CRUD on alarms, alarm-actions etc) using Monotoring-as-a-Service (MaaS). | [optional] 
**access_and_manage_certificates** | **bool** | Privilege for a group to access and manage certificates. | [optional] 
**manage_d_baa_s** | **bool** | Privilege for a group to manage DBaaS related functionality. | [optional] 
**access_and_manage_dns** | **bool** | Privilege for a group to access and manage dns records. | [optional] 
**manage_registry** | **bool** | Privilege for group accessing container registry related functionality. | [optional] 
**manage_dataplatform** | **bool** | Privilege for a group to access and manage the Data Platform. | [optional] 
**access_and_manage_logging** | **bool** | Privilege for a group to access and manage Logs. | [optional] 
**access_and_manage_cdn** | **bool** | Privilege for a group to access and manage CDN. | [optional] 
**access_and_manage_vpn** | **bool** | Privilege for a group to access and manage VPN. | [optional] 
**access_and_manage_api_gateway** | **bool** | Privilege for a group to access and manage API Gateway. | [optional] 
**access_and_manage_kaas** | **bool** | Privilege for a group to access and manage KaaS. | [optional] 
**access_and_manage_network_file_storage** | **bool** | Privilege for a group to access and manage Network File Storage. | [optional] 
**access_and_manage_ai_model_hub** | **bool** | Privilege for a group to access and manage AI Model Hub. | [optional] 
**access_and_manage_iam_resources** | **bool** | Privilege for a group to access and manage Password Policies. | [optional] 
**create_network_security_groups** | **bool** | Privilege for a group to access and manage Network Security Groups. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.group_properties import GroupProperties

# TODO update the JSON string below
json = "{}"
# create an instance of GroupProperties from a JSON string
group_properties_instance = GroupProperties.from_json(json)
# print the JSON string representation of the object
print(GroupProperties.to_json())

# convert the object into a dict
group_properties_dict = group_properties_instance.to_dict()
# create an instance of GroupProperties from a dict
group_properties_from_dict = GroupProperties.from_dict(group_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


