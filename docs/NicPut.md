# NicPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**properties** | [**NicProperties**](NicProperties.md) |  | 

## Example

```python
from openapi_client.models.nic_put import NicPut

# TODO update the JSON string below
json = "{}"
# create an instance of NicPut from a JSON string
nic_put_instance = NicPut.from_json(json)
# print the JSON string representation of the object
print(NicPut.to_json())

# convert the object into a dict
nic_put_dict = nic_put_instance.to_dict()
# create an instance of NicPut from a dict
nic_put_from_dict = NicPut.from_dict(nic_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


