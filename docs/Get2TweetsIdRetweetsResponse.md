# Get2TweetsIdRetweetsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Tweet]**](Tweet.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 
**includes** | [**Expansions**](Expansions.md) |  | [optional] 
**meta** | [**Get2DmConversationsIdDmEventsResponseMeta**](Get2DmConversationsIdDmEventsResponseMeta.md) |  | [optional] 

## Example

```python
from twitter_v2.models.get2_tweets_id_retweets_response import Get2TweetsIdRetweetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2TweetsIdRetweetsResponse from a JSON string
get2_tweets_id_retweets_response_instance = Get2TweetsIdRetweetsResponse.from_json(json)
# print the JSON string representation of the object
print Get2TweetsIdRetweetsResponse.to_json()

# convert the object into a dict
get2_tweets_id_retweets_response_dict = get2_tweets_id_retweets_response_instance.to_dict()
# create an instance of Get2TweetsIdRetweetsResponse from a dict
get2_tweets_id_retweets_response_form_dict = get2_tweets_id_retweets_response.from_dict(get2_tweets_id_retweets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


