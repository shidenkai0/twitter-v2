# TweetDeleteComplianceSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete** | [**TweetComplianceSchema**](TweetComplianceSchema.md) |  | 

## Example

```python
from twitter_api_v2.models.tweet_delete_compliance_schema import TweetDeleteComplianceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TweetDeleteComplianceSchema from a JSON string
tweet_delete_compliance_schema_instance = TweetDeleteComplianceSchema.from_json(json)
# print the JSON string representation of the object
print TweetDeleteComplianceSchema.to_json()

# convert the object into a dict
tweet_delete_compliance_schema_dict = tweet_delete_compliance_schema_instance.to_dict()
# create an instance of TweetDeleteComplianceSchema from a dict
tweet_delete_compliance_schema_form_dict = tweet_delete_compliance_schema.from_dict(tweet_delete_compliance_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


