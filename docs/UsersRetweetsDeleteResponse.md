# UsersRetweetsDeleteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsersRetweetsCreateResponseData**](UsersRetweetsCreateResponseData.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.users_retweets_delete_response import UsersRetweetsDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersRetweetsDeleteResponse from a JSON string
users_retweets_delete_response_instance = UsersRetweetsDeleteResponse.from_json(json)
# print the JSON string representation of the object
print UsersRetweetsDeleteResponse.to_json()

# convert the object into a dict
users_retweets_delete_response_dict = users_retweets_delete_response_instance.to_dict()
# create an instance of UsersRetweetsDeleteResponse from a dict
users_retweets_delete_response_form_dict = users_retweets_delete_response.from_dict(users_retweets_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


