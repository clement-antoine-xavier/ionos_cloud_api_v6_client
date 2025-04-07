# ResourceEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**ResourceGroups**](ResourceGroups.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.resource_entities import ResourceEntities

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceEntities from a JSON string
resource_entities_instance = ResourceEntities.from_json(json)
# print the JSON string representation of the object
print(ResourceEntities.to_json())

# convert the object into a dict
resource_entities_dict = resource_entities_instance.to_dict()
# create an instance of ResourceEntities from a dict
resource_entities_from_dict = ResourceEntities.from_dict(resource_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


