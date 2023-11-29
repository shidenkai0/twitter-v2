# TweetComplianceStreamResponse

Tweet compliance stream events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TweetComplianceData**](TweetComplianceData.md) |  | 
**errors** | [**List[Problem]**](Problem.md) |  | 

## Example

```python
from twitter_v2.models.tweet_compliance_stream_response import TweetComplianceStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TweetComplianceStreamResponse from a JSON string
tweet_compliance_stream_response_instance = TweetComplianceStreamResponse.from_json(json)
# print the JSON string representation of the object
print TweetComplianceStreamResponse.to_json()

# convert the object into a dict
tweet_compliance_stream_response_dict = tweet_compliance_stream_response_instance.to_dict()
# create an instance of TweetComplianceStreamResponse from a dict
tweet_compliance_stream_response_form_dict = tweet_compliance_stream_response.from_dict(tweet_compliance_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


