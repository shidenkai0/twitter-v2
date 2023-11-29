# TweetDeleteResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | 

## Example

```python
from twitter_v2.models.tweet_delete_response_data import TweetDeleteResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TweetDeleteResponseData from a JSON string
tweet_delete_response_data_instance = TweetDeleteResponseData.from_json(json)
# print the JSON string representation of the object
print TweetDeleteResponseData.to_json()

# convert the object into a dict
tweet_delete_response_data_dict = tweet_delete_response_data_instance.to_dict()
# create an instance of TweetDeleteResponseData from a dict
tweet_delete_response_data_form_dict = tweet_delete_response_data.from_dict(tweet_delete_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


