# BackupUnitProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the  resource (alphanumeric characters only). | 
**password** | **str** | The password associated with that resource. | [optional] 
**email** | **str** | The email associated with the backup unit. Bear in mind that this email does not be the same email as of the user. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.backup_unit_properties import BackupUnitProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BackupUnitProperties from a JSON string
backup_unit_properties_instance = BackupUnitProperties.from_json(json)
# print the JSON string representation of the object
print(BackupUnitProperties.to_json())

# convert the object into a dict
backup_unit_properties_dict = backup_unit_properties_instance.to_dict()
# create an instance of BackupUnitProperties from a dict
backup_unit_properties_from_dict = BackupUnitProperties.from_dict(backup_unit_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


