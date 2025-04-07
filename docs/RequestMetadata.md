# RequestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | The last time the resource was created. | [optional] [readonly] 
**created_by** | **str** | The user who created the resource. | [optional] [readonly] 
**etag** | **str** | Resource&#39;s Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an &#39;ETag response header to requests which don&#39;t use &#39;depth&#39; parameter. | [optional] [readonly] 
**request_status** | [**RequestStatus**](RequestStatus.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.request_metadata import RequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMetadata from a JSON string
request_metadata_instance = RequestMetadata.from_json(json)
# print the JSON string representation of the object
print(RequestMetadata.to_json())

# convert the object into a dict
request_metadata_dict = request_metadata_instance.to_dict()
# create an instance of RequestMetadata from a dict
request_metadata_from_dict = RequestMetadata.from_dict(request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


