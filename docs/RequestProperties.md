# RequestProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**body** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.request_properties import RequestProperties

# TODO update the JSON string below
json = "{}"
# create an instance of RequestProperties from a JSON string
request_properties_instance = RequestProperties.from_json(json)
# print the JSON string representation of the object
print(RequestProperties.to_json())

# convert the object into a dict
request_properties_dict = request_properties_instance.to_dict()
# create an instance of RequestProperties from a dict
request_properties_from_dict = RequestProperties.from_dict(request_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


