# Lan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**LanProperties**](LanProperties.md) |  | 
**entities** | [**LanEntities**](LanEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.lan import Lan

# TODO update the JSON string below
json = "{}"
# create an instance of Lan from a JSON string
lan_instance = Lan.from_json(json)
# print the JSON string representation of the object
print(Lan.to_json())

# convert the object into a dict
lan_dict = lan_instance.to_dict()
# create an instance of Lan from a dict
lan_from_dict = Lan.from_dict(lan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


