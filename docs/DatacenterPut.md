# DatacenterPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**DatacenterPropertiesPut**](DatacenterPropertiesPut.md) |  | 
**entities** | [**DatacenterEntities**](DatacenterEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.datacenter_put import DatacenterPut

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterPut from a JSON string
datacenter_put_instance = DatacenterPut.from_json(json)
# print the JSON string representation of the object
print(DatacenterPut.to_json())

# convert the object into a dict
datacenter_put_dict = datacenter_put_instance.to_dict()
# create an instance of DatacenterPut from a dict
datacenter_put_from_dict = DatacenterPut.from_dict(datacenter_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


