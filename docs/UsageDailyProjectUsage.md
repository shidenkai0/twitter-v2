# UsageDailyProjectUsage

The daily usage breakdown for a project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The unique identifier for this project | [optional] 
**usage** | [**List[UsageFields]**](UsageFields.md) | The usage value | [optional] 

## Example

```python
from twitter_api_v2.models.usage_daily_project_usage import UsageDailyProjectUsage

# TODO update the JSON string below
json = "{}"
# create an instance of UsageDailyProjectUsage from a JSON string
usage_daily_project_usage_instance = UsageDailyProjectUsage.from_json(json)
# print the JSON string representation of the object
print UsageDailyProjectUsage.to_json()

# convert the object into a dict
usage_daily_project_usage_dict = usage_daily_project_usage_instance.to_dict()
# create an instance of UsageDailyProjectUsage from a dict
usage_daily_project_usage_form_dict = usage_daily_project_usage.from_dict(usage_daily_project_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


