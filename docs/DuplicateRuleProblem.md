# DuplicateRuleProblem

The rule you have submitted is a duplicate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from twitter_v2.models.duplicate_rule_problem import DuplicateRuleProblem

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateRuleProblem from a JSON string
duplicate_rule_problem_instance = DuplicateRuleProblem.from_json(json)
# print the JSON string representation of the object
print DuplicateRuleProblem.to_json()

# convert the object into a dict
duplicate_rule_problem_dict = duplicate_rule_problem_instance.to_dict()
# create an instance of DuplicateRuleProblem from a dict
duplicate_rule_problem_form_dict = duplicate_rule_problem.from_dict(duplicate_rule_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


