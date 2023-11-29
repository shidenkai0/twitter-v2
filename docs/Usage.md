# Usage

Usage per client app

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cap_reset_day** | **int** | Number of days left for the Tweet cap to reset | [optional] 
**daily_client_app_usage** | [**List[ClientAppUsage]**](ClientAppUsage.md) | The daily usage breakdown for each Client Application a project | [optional] 
**daily_project_usage** | [**UsageDailyProjectUsage**](UsageDailyProjectUsage.md) |  | [optional] 
**project_cap** | **int** | Total number of Tweets that can be read in this project per month | [optional] 
**project_id** | **str** | The unique identifier for this project | [optional] 
**project_usage** | **int** | The number of Tweets read in this project | [optional] 

## Example

```python
from twitter_v2.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print Usage.to_json()

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_form_dict = usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


