# BackupUnits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | **str** | The type of object that has been created. | [optional] [readonly] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[BackupUnit]**](BackupUnit.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.backup_units import BackupUnits

# TODO update the JSON string below
json = "{}"
# create an instance of BackupUnits from a JSON string
backup_units_instance = BackupUnits.from_json(json)
# print the JSON string representation of the object
print(BackupUnits.to_json())

# convert the object into a dict
backup_units_dict = backup_units_instance.to_dict()
# create an instance of BackupUnits from a dict
backup_units_from_dict = BackupUnits.from_dict(backup_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


