# RemoteConsoleUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The remote console url with the jwToken parameter for access | [optional] [readonly] 

## Example

```python
from openapi_client.models.remote_console_url import RemoteConsoleUrl

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteConsoleUrl from a JSON string
remote_console_url_instance = RemoteConsoleUrl.from_json(json)
# print the JSON string representation of the object
print(RemoteConsoleUrl.to_json())

# convert the object into a dict
remote_console_url_dict = remote_console_url_instance.to_dict()
# create an instance of RemoteConsoleUrl from a dict
remote_console_url_from_dict = RemoteConsoleUrl.from_dict(remote_console_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


