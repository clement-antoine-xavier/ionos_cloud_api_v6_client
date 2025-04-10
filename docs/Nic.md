# Nic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**NicProperties**](NicProperties.md) |  | 
**entities** | [**NicEntities**](NicEntities.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.nic import Nic

# TODO update the JSON string below
json = "{}"
# create an instance of Nic from a JSON string
nic_instance = Nic.from_json(json)
# print the JSON string representation of the object
print(Nic.to_json())

# convert the object into a dict
nic_dict = nic_instance.to_dict()
# create an instance of Nic from a dict
nic_from_dict = Nic.from_dict(nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


