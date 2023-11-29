# Get2TweetsSample10StreamResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Tweet**](Tweet.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 
**includes** | [**Expansions**](Expansions.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.get2_tweets_sample10_stream_response import Get2TweetsSample10StreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2TweetsSample10StreamResponse from a JSON string
get2_tweets_sample10_stream_response_instance = Get2TweetsSample10StreamResponse.from_json(json)
# print the JSON string representation of the object
print Get2TweetsSample10StreamResponse.to_json()

# convert the object into a dict
get2_tweets_sample10_stream_response_dict = get2_tweets_sample10_stream_response_instance.to_dict()
# create an instance of Get2TweetsSample10StreamResponse from a dict
get2_tweets_sample10_stream_response_form_dict = get2_tweets_sample10_stream_response.from_dict(get2_tweets_sample10_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


