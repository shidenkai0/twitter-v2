# ClientAppUsage

Usage per client app

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_app_id** | **str** | The unique identifier for this project | [optional] 
**usage** | [**List[UsageFields]**](UsageFields.md) | The usage value | [optional] 
**usage_result_count** | **int** | The number of results returned | [optional] 

## Example

```python
from twitter_api_v2.models.client_app_usage import ClientAppUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAppUsage from a JSON string
client_app_usage_instance = ClientAppUsage.from_json(json)
# print the JSON string representation of the object
print ClientAppUsage.to_json()

# convert the object into a dict
client_app_usage_dict = client_app_usage_instance.to_dict()
# create an instance of ClientAppUsage from a dict
client_app_usage_form_dict = client_app_usage.from_dict(client_app_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


