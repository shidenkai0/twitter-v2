# Get2SpacesIdTweetsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Tweet]**](Tweet.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 
**includes** | [**Expansions**](Expansions.md) |  | [optional] 
**meta** | [**Get2DmConversationsIdDmEventsResponseMeta**](Get2DmConversationsIdDmEventsResponseMeta.md) |  | [optional] 

## Example

```python
from openapi_client.models.get2_spaces_id_tweets_response import Get2SpacesIdTweetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2SpacesIdTweetsResponse from a JSON string
get2_spaces_id_tweets_response_instance = Get2SpacesIdTweetsResponse.from_json(json)
# print the JSON string representation of the object
print Get2SpacesIdTweetsResponse.to_json()

# convert the object into a dict
get2_spaces_id_tweets_response_dict = get2_spaces_id_tweets_response_instance.to_dict()
# create an instance of Get2SpacesIdTweetsResponse from a dict
get2_spaces_id_tweets_response_form_dict = get2_spaces_id_tweets_response.from_dict(get2_spaces_id_tweets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

