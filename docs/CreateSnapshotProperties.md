# CreateSnapshotProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the snapshot | [optional] 
**description** | **str** | The description of the snapshot | [optional] 
**sec_auth_protection** | **bool** | Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc. | [optional] 
**licence_type** | **str** | OS type of this Snapshot | [optional] 
**application_type** | **str** | The type of application that is hosted on this resource.  Only public images can have an Application type different than UNKNOWN. | [optional] [default to 'UNKNOWN']

## Example

```python
from openapi_client.models.create_snapshot_properties import CreateSnapshotProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotProperties from a JSON string
create_snapshot_properties_instance = CreateSnapshotProperties.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotProperties.to_json())

# convert the object into a dict
create_snapshot_properties_dict = create_snapshot_properties_instance.to_dict()
# create an instance of CreateSnapshotProperties from a dict
create_snapshot_properties_from_dict = CreateSnapshotProperties.from_dict(create_snapshot_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


