# FirewallRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly] 
**type** | [**Type**](Type.md) | The type of object that has been created. | [optional] 
**href** | **str** | URL to the object representation (absolute path). | [optional] [readonly] 
**items** | [**List[FirewallRule]**](FirewallRule.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.firewall_rules import FirewallRules

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRules from a JSON string
firewall_rules_instance = FirewallRules.from_json(json)
# print the JSON string representation of the object
print(FirewallRules.to_json())

# convert the object into a dict
firewall_rules_dict = firewall_rules_instance.to_dict()
# create an instance of FirewallRules from a dict
firewall_rules_from_dict = FirewallRules.from_dict(firewall_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


