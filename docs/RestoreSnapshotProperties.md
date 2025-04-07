# RestoreSnapshotProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | The id of the snapshot | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.restore_snapshot_properties import RestoreSnapshotProperties

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreSnapshotProperties from a JSON string
restore_snapshot_properties_instance = RestoreSnapshotProperties.from_json(json)
# print the JSON string representation of the object
print(RestoreSnapshotProperties.to_json())

# convert the object into a dict
restore_snapshot_properties_dict = restore_snapshot_properties_instance.to_dict()
# create an instance of RestoreSnapshotProperties from a dict
restore_snapshot_properties_from_dict = RestoreSnapshotProperties.from_dict(restore_snapshot_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


