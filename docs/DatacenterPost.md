# DatacenterPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**DatacenterPropertiesPost**](DatacenterPropertiesPost.md) |  | 
**entities** | [**DatacenterEntities**](DatacenterEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.datacenter_post import DatacenterPost

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterPost from a JSON string
datacenter_post_instance = DatacenterPost.from_json(json)
# print the JSON string representation of the object
print(DatacenterPost.to_json())

# convert the object into a dict
datacenter_post_dict = datacenter_post_instance.to_dict()
# create an instance of DatacenterPost from a dict
datacenter_post_from_dict = DatacenterPost.from_dict(datacenter_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


