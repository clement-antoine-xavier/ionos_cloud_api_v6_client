# KubernetesMaintenanceWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_the_week** | **str** | The weekday for a maintenance window. | 
**time** | **str** | The time to use for a maintenance window. Accepted formats are: HH:mm:ss; HH:mm:ss\&quot;Z\&quot;; HH:mm:ssZ. This time may vary by 15 minutes. | 

## Example

```python
from openapi_client.models.kubernetes_maintenance_window import KubernetesMaintenanceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesMaintenanceWindow from a JSON string
kubernetes_maintenance_window_instance = KubernetesMaintenanceWindow.from_json(json)
# print the JSON string representation of the object
print(KubernetesMaintenanceWindow.to_json())

# convert the object into a dict
kubernetes_maintenance_window_dict = kubernetes_maintenance_window_instance.to_dict()
# create an instance of KubernetesMaintenanceWindow from a dict
kubernetes_maintenance_window_from_dict = KubernetesMaintenanceWindow.from_dict(kubernetes_maintenance_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


