# Get2UsageTweetsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Usage**](Usage.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 

## Example

```python
from openapi_client.models.get2_usage_tweets_response import Get2UsageTweetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2UsageTweetsResponse from a JSON string
get2_usage_tweets_response_instance = Get2UsageTweetsResponse.from_json(json)
# print the JSON string representation of the object
print Get2UsageTweetsResponse.to_json()

# convert the object into a dict
get2_usage_tweets_response_dict = get2_usage_tweets_response_instance.to_dict()
# create an instance of Get2UsageTweetsResponse from a dict
get2_usage_tweets_response_form_dict = get2_usage_tweets_response.from_dict(get2_usage_tweets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


