# BackupUnitSSO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_url** | **str** | The backup unit single sign on url | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.backup_unit_sso import BackupUnitSSO

# TODO update the JSON string below
json = "{}"
# create an instance of BackupUnitSSO from a JSON string
backup_unit_sso_instance = BackupUnitSSO.from_json(json)
# print the JSON string representation of the object
print(BackupUnitSSO.to_json())

# convert the object into a dict
backup_unit_sso_dict = backup_unit_sso_instance.to_dict()
# create an instance of BackupUnitSSO from a dict
backup_unit_sso_from_dict = BackupUnitSSO.from_dict(backup_unit_sso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


