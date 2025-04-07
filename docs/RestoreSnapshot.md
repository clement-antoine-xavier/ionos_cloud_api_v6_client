# RestoreSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**RestoreSnapshotProperties**](RestoreSnapshotProperties.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.restore_snapshot import RestoreSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreSnapshot from a JSON string
restore_snapshot_instance = RestoreSnapshot.from_json(json)
# print the JSON string representation of the object
print(RestoreSnapshot.to_json())

# convert the object into a dict
restore_snapshot_dict = restore_snapshot_instance.to_dict()
# create an instance of RestoreSnapshot from a dict
restore_snapshot_from_dict = RestoreSnapshot.from_dict(restore_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


