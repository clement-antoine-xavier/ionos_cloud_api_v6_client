# Snapshots


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[Snapshot]**](Snapshot.md) | Array of items in the collection. | [optional] [readonly] 

## Example

```python
from ionos_cloud_api_v6_client.models.snapshots import Snapshots

# TODO update the JSON string below
json = "{}"
# create an instance of Snapshots from a JSON string
snapshots_instance = Snapshots.from_json(json)
# print the JSON string representation of the object
print(Snapshots.to_json())

# convert the object into a dict
snapshots_dict = snapshots_instance.to_dict()
# create an instance of Snapshots from a dict
snapshots_from_dict = Snapshots.from_dict(snapshots_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


