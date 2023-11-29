# Get2TweetsSearchStreamRulesCountsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RulesCount**](RulesCount.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.get2_tweets_search_stream_rules_counts_response import Get2TweetsSearchStreamRulesCountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2TweetsSearchStreamRulesCountsResponse from a JSON string
get2_tweets_search_stream_rules_counts_response_instance = Get2TweetsSearchStreamRulesCountsResponse.from_json(json)
# print the JSON string representation of the object
print Get2TweetsSearchStreamRulesCountsResponse.to_json()

# convert the object into a dict
get2_tweets_search_stream_rules_counts_response_dict = get2_tweets_search_stream_rules_counts_response_instance.to_dict()
# create an instance of Get2TweetsSearchStreamRulesCountsResponse from a dict
get2_tweets_search_stream_rules_counts_response_form_dict = get2_tweets_search_stream_rules_counts_response.from_dict(get2_tweets_search_stream_rules_counts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


