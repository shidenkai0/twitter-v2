# Get2TweetsSearchAllResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Tweet]**](Tweet.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 
**includes** | [**Expansions**](Expansions.md) |  | [optional] 
**meta** | [**Get2TweetsSearchAllResponseMeta**](Get2TweetsSearchAllResponseMeta.md) |  | [optional] 

## Example

```python
from twitter_v2.models.get2_tweets_search_all_response import Get2TweetsSearchAllResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2TweetsSearchAllResponse from a JSON string
get2_tweets_search_all_response_instance = Get2TweetsSearchAllResponse.from_json(json)
# print the JSON string representation of the object
print Get2TweetsSearchAllResponse.to_json()

# convert the object into a dict
get2_tweets_search_all_response_dict = get2_tweets_search_all_response_instance.to_dict()
# create an instance of Get2TweetsSearchAllResponse from a dict
get2_tweets_search_all_response_form_dict = get2_tweets_search_all_response.from_dict(get2_tweets_search_all_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


