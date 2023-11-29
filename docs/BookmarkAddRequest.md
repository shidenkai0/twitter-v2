# BookmarkAddRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tweet_id** | **str** | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. | 

## Example

```python
from twitter_api_v2.models.bookmark_add_request import BookmarkAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkAddRequest from a JSON string
bookmark_add_request_instance = BookmarkAddRequest.from_json(json)
# print the JSON string representation of the object
print BookmarkAddRequest.to_json()

# convert the object into a dict
bookmark_add_request_dict = bookmark_add_request_instance.to_dict()
# create an instance of BookmarkAddRequest from a dict
bookmark_add_request_form_dict = bookmark_add_request.from_dict(bookmark_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


