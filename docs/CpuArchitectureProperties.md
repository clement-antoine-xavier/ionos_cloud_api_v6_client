# CpuArchitectureProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_family** | **str** | A valid CPU family name. | [optional] 
**max_cores** | **int** | The maximum number of cores available. | [optional] 
**max_ram** | **int** | The maximum RAM size in MB. | [optional] 
**vendor** | **str** | A valid CPU vendor name. | [optional] 

## Example

```python
from openapi_client.models.cpu_architecture_properties import CpuArchitectureProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CpuArchitectureProperties from a JSON string
cpu_architecture_properties_instance = CpuArchitectureProperties.from_json(json)
# print the JSON string representation of the object
print(CpuArchitectureProperties.to_json())

# convert the object into a dict
cpu_architecture_properties_dict = cpu_architecture_properties_instance.to_dict()
# create an instance of CpuArchitectureProperties from a dict
cpu_architecture_properties_from_dict = CpuArchitectureProperties.from_dict(cpu_architecture_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


