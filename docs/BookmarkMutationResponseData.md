# BookmarkMutationResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmarked** | **bool** |  | [optional] 

## Example

```python
from twitter_api_v2.models.bookmark_mutation_response_data import BookmarkMutationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkMutationResponseData from a JSON string
bookmark_mutation_response_data_instance = BookmarkMutationResponseData.from_json(json)
# print the JSON string representation of the object
print BookmarkMutationResponseData.to_json()

# convert the object into a dict
bookmark_mutation_response_data_dict = bookmark_mutation_response_data_instance.to_dict()
# create an instance of BookmarkMutationResponseData from a dict
bookmark_mutation_response_data_form_dict = bookmark_mutation_response_data.from_dict(bookmark_mutation_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


