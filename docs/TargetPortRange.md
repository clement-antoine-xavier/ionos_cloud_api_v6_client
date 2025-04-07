# TargetPortRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | Target port range start associated with the NAT Gateway rule. | [optional] 
**end** | **int** | Target port range end associated with the NAT Gateway rule. | [optional] 

## Example

```python
from openapi_client.models.target_port_range import TargetPortRange

# TODO update the JSON string below
json = "{}"
# create an instance of TargetPortRange from a JSON string
target_port_range_instance = TargetPortRange.from_json(json)
# print the JSON string representation of the object
print(TargetPortRange.to_json())

# convert the object into a dict
target_port_range_dict = target_port_range_instance.to_dict()
# create an instance of TargetPortRange from a dict
target_port_range_from_dict = TargetPortRange.from_dict(target_port_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


