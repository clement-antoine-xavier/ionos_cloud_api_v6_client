# KubernetesNodeMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | The resource entity tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity tags are also added as &#39;ETag&#39; response headers to requests that do not use the &#39;depth&#39; parameter. | [optional] [readonly] 
**created_date** | **datetime** | The date the resource was created. | [optional] [readonly] 
**last_modified_date** | **datetime** | The date the resource was last modified. | [optional] [readonly] 
**state** | **str** | The resource state. | [optional] [readonly] 
**last_software_updated_date** | **datetime** | The date when the software on the node was last updated. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.kubernetes_node_metadata import KubernetesNodeMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodeMetadata from a JSON string
kubernetes_node_metadata_instance = KubernetesNodeMetadata.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodeMetadata.to_json())

# convert the object into a dict
kubernetes_node_metadata_dict = kubernetes_node_metadata_instance.to_dict()
# create an instance of KubernetesNodeMetadata from a dict
kubernetes_node_metadata_from_dict = KubernetesNodeMetadata.from_dict(kubernetes_node_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


