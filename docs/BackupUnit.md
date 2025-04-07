# BackupUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | **str** | The type of object that has been created. | [optional] [readonly] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**metadata** | [**DatacenterElementMetadata**](DatacenterElementMetadata.md) |  | [optional] 
**properties** | [**BackupUnitProperties**](BackupUnitProperties.md) |  | 

## Example

```python
from openapi_client.models.backup_unit import BackupUnit

# TODO update the JSON string below
json = "{}"
# create an instance of BackupUnit from a JSON string
backup_unit_instance = BackupUnit.from_json(json)
# print the JSON string representation of the object
print(BackupUnit.to_json())

# convert the object into a dict
backup_unit_dict = backup_unit_instance.to_dict()
# create an instance of BackupUnit from a dict
backup_unit_from_dict = BackupUnit.from_dict(backup_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


