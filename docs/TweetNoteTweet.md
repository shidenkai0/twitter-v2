# TweetNoteTweet

The full-content of the Tweet, including text beyond 280 characters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**TweetNoteTweetEntities**](TweetNoteTweetEntities.md) |  | [optional] 
**text** | **str** | The note content of the Tweet. | [optional] 

## Example

```python
from openapi_client.models.tweet_note_tweet import TweetNoteTweet

# TODO update the JSON string below
json = "{}"
# create an instance of TweetNoteTweet from a JSON string
tweet_note_tweet_instance = TweetNoteTweet.from_json(json)
# print the JSON string representation of the object
print TweetNoteTweet.to_json()

# convert the object into a dict
tweet_note_tweet_dict = tweet_note_tweet_instance.to_dict()
# create an instance of TweetNoteTweet from a dict
tweet_note_tweet_form_dict = tweet_note_tweet.from_dict(tweet_note_tweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


