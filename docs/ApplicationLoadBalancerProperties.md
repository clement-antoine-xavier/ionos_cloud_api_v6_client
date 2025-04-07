# ApplicationLoadBalancerProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Application Load Balancer name. | 
**listener_lan** | **int** | The ID of the listening (inbound) LAN. | 
**ips** | **List[str]** | Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the &#39;listenerLan&#39; are customer-reserved public IPs for the public load balancers, and private IPs for the private load balancers. | [optional] 
**target_lan** | **int** | The ID of the balanced private target LAN (outbound). | 
**lb_private_ips** | **List[str]** | Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet. | [optional] 
**central_logging** | **bool** | Turn logging on and off for this product. Default value is &#39;false&#39;. | [optional] 
**logging_format** | **str** | Specifies the format of the logs. | [optional] 

## Example

```python
from ionos_cloud_api_v6_client.models.application_load_balancer_properties import ApplicationLoadBalancerProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLoadBalancerProperties from a JSON string
application_load_balancer_properties_instance = ApplicationLoadBalancerProperties.from_json(json)
# print the JSON string representation of the object
print(ApplicationLoadBalancerProperties.to_json())

# convert the object into a dict
application_load_balancer_properties_dict = application_load_balancer_properties_instance.to_dict()
# create an instance of ApplicationLoadBalancerProperties from a dict
application_load_balancer_properties_from_dict = ApplicationLoadBalancerProperties.from_dict(application_load_balancer_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


