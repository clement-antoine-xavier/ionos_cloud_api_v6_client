# KubernetesClusterPropertiesForPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A Kubernetes cluster name. Valid Kubernetes cluster name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. | 
**k8s_version** | **str** | The Kubernetes version that the cluster is running. This limits which Kubernetes versions can run in a cluster&#39;s node pools. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions. | [optional] 
**maintenance_window** | [**KubernetesMaintenanceWindow**](KubernetesMaintenanceWindow.md) |  | [optional] 
**api_subnet_allow_list** | **List[str]** | Access to the K8s API server is restricted to these CIDRs. Intra-cluster traffic is not affected by this restriction. If no AllowList is specified, access is not limited. If an IP is specified without a subnet mask, the default value is 32 for IPv4 and 128 for IPv6. | [optional] 
**s3_buckets** | [**List[S3Bucket]**](S3Bucket.md) | List of Object storage buckets configured for K8s usage. At the moment, it contains only one bucket that is used to store K8s API audit logs. | [optional] 

## Example

```python
from openapi_client.models.kubernetes_cluster_properties_for_put import KubernetesClusterPropertiesForPut

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesClusterPropertiesForPut from a JSON string
kubernetes_cluster_properties_for_put_instance = KubernetesClusterPropertiesForPut.from_json(json)
# print the JSON string representation of the object
print(KubernetesClusterPropertiesForPut.to_json())

# convert the object into a dict
kubernetes_cluster_properties_for_put_dict = kubernetes_cluster_properties_for_put_instance.to_dict()
# create an instance of KubernetesClusterPropertiesForPut from a dict
kubernetes_cluster_properties_for_put_from_dict = KubernetesClusterPropertiesForPut.from_dict(kubernetes_cluster_properties_for_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


