# LanEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nics** | [**LanNics**](LanNics.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.lan_entities import LanEntities

# TODO update the JSON string below
json = "{}"
# create an instance of LanEntities from a JSON string
lan_entities_instance = LanEntities.from_json(json)
# print the JSON string representation of the object
print(LanEntities.to_json())

# convert the object into a dict
lan_entities_dict = lan_entities_instance.to_dict()
# create an instance of LanEntities from a dict
lan_entities_from_dict = LanEntities.from_dict(lan_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


