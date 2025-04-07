# Datacenter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**DatacenterProperties**](DatacenterProperties.md) |  | 
**entities** | [**DatacenterEntities**](DatacenterEntities.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.datacenter import Datacenter

# TODO update the JSON string below
json = "{}"
# create an instance of Datacenter from a JSON string
datacenter_instance = Datacenter.from_json(json)
# print the JSON string representation of the object
print(Datacenter.to_json())

# convert the object into a dict
datacenter_dict = datacenter_instance.to_dict()
# create an instance of Datacenter from a dict
datacenter_from_dict = Datacenter.from_dict(datacenter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


