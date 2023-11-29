# TweetNoteTweetEntities


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashtags** | [**List[CashtagEntity]**](CashtagEntity.md) |  | [optional] 
**hashtags** | [**List[HashtagEntity]**](HashtagEntity.md) |  | [optional] 
**mentions** | [**List[MentionEntity]**](MentionEntity.md) |  | [optional] 
**urls** | [**List[UrlEntity]**](UrlEntity.md) |  | [optional] 

## Example

```python
from twitter_v2.models.tweet_note_tweet_entities import TweetNoteTweetEntities

# TODO update the JSON string below
json = "{}"
# create an instance of TweetNoteTweetEntities from a JSON string
tweet_note_tweet_entities_instance = TweetNoteTweetEntities.from_json(json)
# print the JSON string representation of the object
print TweetNoteTweetEntities.to_json()

# convert the object into a dict
tweet_note_tweet_entities_dict = tweet_note_tweet_entities_instance.to_dict()
# create an instance of TweetNoteTweetEntities from a dict
tweet_note_tweet_entities_form_dict = tweet_note_tweet_entities.from_dict(tweet_note_tweet_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


