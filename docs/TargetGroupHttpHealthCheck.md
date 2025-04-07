# TargetGroupHttpHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The destination URL for HTTP the health check; the default is &#39;/&#39;. | [optional] 
**method** | **str** | The method used for the health check request. | [optional] 
**match_type** | **str** | Specify the target&#39;s response type to match ALB&#39;s request. | 
**response** | **str** | The response returned by the request. It can be a status code or a response body depending on the definition of &#39;matchType&#39;. | 
**regex** | **bool** | Specifies whether to use a regular expression to parse the response body; the default value is &#39;FALSE&#39;.  By using regular expressions, you can flexibly customize the expected response from a healthy server. | [optional] 
**negate** | **bool** | Specifies whether to negate an individual entry; the default value is &#39;FALSE&#39;. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.target_group_http_health_check import TargetGroupHttpHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroupHttpHealthCheck from a JSON string
target_group_http_health_check_instance = TargetGroupHttpHealthCheck.from_json(json)
# print the JSON string representation of the object
print(TargetGroupHttpHealthCheck.to_json())

# convert the object into a dict
target_group_http_health_check_dict = target_group_http_health_check_instance.to_dict()
# create an instance of TargetGroupHttpHealthCheck from a dict
target_group_http_health_check_from_dict = TargetGroupHttpHealthCheck.from_dict(target_group_http_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


