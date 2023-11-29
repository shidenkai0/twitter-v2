# AppRulesCount

A count of user-provided stream filtering rules at the client application level.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_app_id** | **str** | The ID of the client application | [optional] 
**rule_count** | **int** | Number of rules for client application | [optional] 

## Example

```python
from openapi_client.models.app_rules_count import AppRulesCount

# TODO update the JSON string below
json = "{}"
# create an instance of AppRulesCount from a JSON string
app_rules_count_instance = AppRulesCount.from_json(json)
# print the JSON string representation of the object
print AppRulesCount.to_json()

# convert the object into a dict
app_rules_count_dict = app_rules_count_instance.to_dict()
# create an instance of AppRulesCount from a dict
app_rules_count_form_dict = app_rules_count.from_dict(app_rules_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


