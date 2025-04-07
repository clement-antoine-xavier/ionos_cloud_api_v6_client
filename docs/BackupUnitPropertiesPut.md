# BackupUnitPropertiesPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the  resource (alphanumeric characters only). | [optional] [readonly] 
**password** | **str** | The password associated with that resource. | [optional] 
**email** | **str** | The email associated with the backup unit. Bear in mind that this email does not be the same email as of the user. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.backup_unit_properties_put import BackupUnitPropertiesPut

# TODO update the JSON string below
json = "{}"
# create an instance of BackupUnitPropertiesPut from a JSON string
backup_unit_properties_put_instance = BackupUnitPropertiesPut.from_json(json)
# print the JSON string representation of the object
print(BackupUnitPropertiesPut.to_json())

# convert the object into a dict
backup_unit_properties_put_dict = backup_unit_properties_put_instance.to_dict()
# create an instance of BackupUnitPropertiesPut from a dict
backup_unit_properties_put_from_dict = BackupUnitPropertiesPut.from_dict(backup_unit_properties_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


