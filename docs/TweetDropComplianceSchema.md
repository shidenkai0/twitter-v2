# TweetDropComplianceSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop** | [**TweetComplianceSchema**](TweetComplianceSchema.md) |  | 

## Example

```python
from twitter_api_v2.models.tweet_drop_compliance_schema import TweetDropComplianceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TweetDropComplianceSchema from a JSON string
tweet_drop_compliance_schema_instance = TweetDropComplianceSchema.from_json(json)
# print the JSON string representation of the object
print TweetDropComplianceSchema.to_json()

# convert the object into a dict
tweet_drop_compliance_schema_dict = tweet_drop_compliance_schema_instance.to_dict()
# create an instance of TweetDropComplianceSchema from a dict
tweet_drop_compliance_schema_form_dict = tweet_drop_compliance_schema.from_dict(tweet_drop_compliance_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


