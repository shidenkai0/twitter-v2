# Get2TweetsCountsAllResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SearchCount]**](SearchCount.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 
**meta** | [**Get2TweetsCountsAllResponseMeta**](Get2TweetsCountsAllResponseMeta.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.get2_tweets_counts_all_response import Get2TweetsCountsAllResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2TweetsCountsAllResponse from a JSON string
get2_tweets_counts_all_response_instance = Get2TweetsCountsAllResponse.from_json(json)
# print the JSON string representation of the object
print Get2TweetsCountsAllResponse.to_json()

# convert the object into a dict
get2_tweets_counts_all_response_dict = get2_tweets_counts_all_response_instance.to_dict()
# create an instance of Get2TweetsCountsAllResponse from a dict
get2_tweets_counts_all_response_form_dict = get2_tweets_counts_all_response.from_dict(get2_tweets_counts_all_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


