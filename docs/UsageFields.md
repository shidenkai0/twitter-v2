# UsageFields

Represents the data for Usage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The time period for the usage | [optional] 
**usage** | **int** | The usage value | [optional] 

## Example

```python
from twitter_v2.models.usage_fields import UsageFields

# TODO update the JSON string below
json = "{}"
# create an instance of UsageFields from a JSON string
usage_fields_instance = UsageFields.from_json(json)
# print the JSON string representation of the object
print UsageFields.to_json()

# convert the object into a dict
usage_fields_dict = usage_fields_instance.to_dict()
# create an instance of UsageFields from a dict
usage_fields_form_dict = usage_fields.from_dict(usage_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


