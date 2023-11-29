# UsersRetweetsCreateResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retweeted** | **bool** |  | [optional] 

## Example

```python
from twitter_api_v2.models.users_retweets_create_response_data import UsersRetweetsCreateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersRetweetsCreateResponseData from a JSON string
users_retweets_create_response_data_instance = UsersRetweetsCreateResponseData.from_json(json)
# print the JSON string representation of the object
print UsersRetweetsCreateResponseData.to_json()

# convert the object into a dict
users_retweets_create_response_data_dict = users_retweets_create_response_data_instance.to_dict()
# create an instance of UsersRetweetsCreateResponseData from a dict
users_retweets_create_response_data_form_dict = users_retweets_create_response_data.from_dict(users_retweets_create_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


