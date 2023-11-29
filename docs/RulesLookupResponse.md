# RulesLookupResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Rule]**](Rule.md) |  | [optional] 
**meta** | [**RulesResponseMetadata**](RulesResponseMetadata.md) |  | 

## Example

```python
from twitter_api_v2.models.rules_lookup_response import RulesLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RulesLookupResponse from a JSON string
rules_lookup_response_instance = RulesLookupResponse.from_json(json)
# print the JSON string representation of the object
print RulesLookupResponse.to_json()

# convert the object into a dict
rules_lookup_response_dict = rules_lookup_response_instance.to_dict()
# create an instance of RulesLookupResponse from a dict
rules_lookup_response_form_dict = rules_lookup_response.from_dict(rules_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


