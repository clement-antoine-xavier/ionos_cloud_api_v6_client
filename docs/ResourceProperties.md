# ResourceProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource. | [optional] 
**sec_auth_protection** | **bool** | Boolean value representing if the resource is multi factor protected or not e.g. using two factor protection. Currently only data centers and snapshots are allowed to be multi factor protected, The value of attribute if null is intentional and it means that the resource doesn&#39;t support multi factor protection at all. | [optional] 

## Example

```python
from openapi_client.models.resource_properties import ResourceProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceProperties from a JSON string
resource_properties_instance = ResourceProperties.from_json(json)
# print the JSON string representation of the object
print(ResourceProperties.to_json())

# convert the object into a dict
resource_properties_dict = resource_properties_instance.to_dict()
# create an instance of ResourceProperties from a dict
resource_properties_from_dict = ResourceProperties.from_dict(resource_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


