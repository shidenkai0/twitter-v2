# RulesCount

A count of user-provided stream filtering rules at the application and project levels.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_project_client_apps** | [**List[AppRulesCount]**](AppRulesCount.md) | Client App Rule Counts for all applications in the project | [optional] 
**cap_per_client_app** | **int** | Cap of number of rules allowed per client application | [optional] 
**cap_per_project** | **int** | Cap of number of rules allowed per project | [optional] 
**client_app_rules_count** | [**AppRulesCount**](AppRulesCount.md) |  | [optional] 
**project_rules_count** | **int** | Number of rules for project | [optional] 

## Example

```python
from twitter_api_v2.models.rules_count import RulesCount

# TODO update the JSON string below
json = "{}"
# create an instance of RulesCount from a JSON string
rules_count_instance = RulesCount.from_json(json)
# print the JSON string representation of the object
print RulesCount.to_json()

# convert the object into a dict
rules_count_dict = rules_count_instance.to_dict()
# create an instance of RulesCount from a dict
rules_count_form_dict = rules_count.from_dict(rules_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


