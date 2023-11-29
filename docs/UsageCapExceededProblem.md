# UsageCapExceededProblem

A problem that indicates that a usage cap has been exceeded.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from twitter_v2.models.usage_cap_exceeded_problem import UsageCapExceededProblem

# TODO update the JSON string below
json = "{}"
# create an instance of UsageCapExceededProblem from a JSON string
usage_cap_exceeded_problem_instance = UsageCapExceededProblem.from_json(json)
# print the JSON string representation of the object
print UsageCapExceededProblem.to_json()

# convert the object into a dict
usage_cap_exceeded_problem_dict = usage_cap_exceeded_problem_instance.to_dict()
# create an instance of UsageCapExceededProblem from a dict
usage_cap_exceeded_problem_form_dict = usage_cap_exceeded_problem.from_dict(usage_cap_exceeded_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


