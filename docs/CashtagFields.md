# CashtagFields

Represent the portion of text recognized as a Cashtag, and its start and end position within the text.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | 

## Example

```python
from twitter_api_v2.models.cashtag_fields import CashtagFields

# TODO update the JSON string below
json = "{}"
# create an instance of CashtagFields from a JSON string
cashtag_fields_instance = CashtagFields.from_json(json)
# print the JSON string representation of the object
print CashtagFields.to_json()

# convert the object into a dict
cashtag_fields_dict = cashtag_fields_instance.to_dict()
# create an instance of CashtagFields from a dict
cashtag_fields_form_dict = cashtag_fields.from_dict(cashtag_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


