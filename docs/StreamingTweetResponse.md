# StreamingTweetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Tweet**](Tweet.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 
**includes** | [**Expansions**](Expansions.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.streaming_tweet_response import StreamingTweetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingTweetResponse from a JSON string
streaming_tweet_response_instance = StreamingTweetResponse.from_json(json)
# print the JSON string representation of the object
print StreamingTweetResponse.to_json()

# convert the object into a dict
streaming_tweet_response_dict = streaming_tweet_response_instance.to_dict()
# create an instance of StreamingTweetResponse from a dict
streaming_tweet_response_form_dict = streaming_tweet_response.from_dict(streaming_tweet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


