# CreateSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**CreateSnapshotProperties**](CreateSnapshotProperties.md) |  | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.create_snapshot import CreateSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshot from a JSON string
create_snapshot_instance = CreateSnapshot.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshot.to_json())

# convert the object into a dict
create_snapshot_dict = create_snapshot_instance.to_dict()
# create an instance of CreateSnapshot from a dict
create_snapshot_from_dict = CreateSnapshot.from_dict(create_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


