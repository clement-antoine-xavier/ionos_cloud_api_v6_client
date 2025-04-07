# RequestStatusMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**etag** | **str** | Resource&#39;s Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an &#39;ETag response header to requests which don&#39;t use &#39;depth&#39; parameter. | [optional] [readonly] 
**targets** | [**List[RequestTarget]**](RequestTarget.md) |  | [optional] 

## Example

```python
from openapi_client.models.request_status_metadata import RequestStatusMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RequestStatusMetadata from a JSON string
request_status_metadata_instance = RequestStatusMetadata.from_json(json)
# print the JSON string representation of the object
print(RequestStatusMetadata.to_json())

# convert the object into a dict
request_status_metadata_dict = request_status_metadata_instance.to_dict()
# create an instance of RequestStatusMetadata from a dict
request_status_metadata_from_dict = RequestStatusMetadata.from_dict(request_status_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


