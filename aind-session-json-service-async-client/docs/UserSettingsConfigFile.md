# UserSettingsConfigFile

Optionally pull settings from a local config file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from aind_session_json_service_async_client.models.user_settings_config_file import UserSettingsConfigFile

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsConfigFile from a JSON string
user_settings_config_file_instance = UserSettingsConfigFile.from_json(json)
# print the JSON string representation of the object
print(UserSettingsConfigFile.to_json())

# convert the object into a dict
user_settings_config_file_dict = user_settings_config_file_instance.to_dict()
# create an instance of UserSettingsConfigFile from a dict
user_settings_config_file_from_dict = UserSettingsConfigFile.from_dict(user_settings_config_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


