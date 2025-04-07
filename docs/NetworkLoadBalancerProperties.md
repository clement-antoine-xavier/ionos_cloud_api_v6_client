# NetworkLoadBalancerProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Network Load Balancer. | 
**listener_lan** | **int** | ID of the listening LAN (inbound). | 
**ips** | **List[str]** | Collection of the Network Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan must be customer-reserved IPs for public Load Balancers, and private IPs for private Load Balancers. | [optional] 
**target_lan** | **int** | ID of the balanced private target LAN (outbound). | 
**lb_private_ips** | **List[str]** | Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain a valid subnet mask. If no IP is provided, the system will generate an IP with /24 subnet. | [optional] 
**central_logging** | **bool** | Turn logging on and off for this product. Default value is &#39;false&#39;. | [optional] 
**logging_format** | **str** | Specifies the format of the logs. | [optional] 

## Example

```python
from openapi_client.models.network_load_balancer_properties import NetworkLoadBalancerProperties

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerProperties from a JSON string
network_load_balancer_properties_instance = NetworkLoadBalancerProperties.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerProperties.to_json())

# convert the object into a dict
network_load_balancer_properties_dict = network_load_balancer_properties_instance.to_dict()
# create an instance of NetworkLoadBalancerProperties from a dict
network_load_balancer_properties_from_dict = NetworkLoadBalancerProperties.from_dict(network_load_balancer_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


