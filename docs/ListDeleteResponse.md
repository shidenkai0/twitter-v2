# ListDeleteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListDeleteResponseData**](ListDeleteResponseData.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.list_delete_response import ListDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeleteResponse from a JSON string
list_delete_response_instance = ListDeleteResponse.from_json(json)
# print the JSON string representation of the object
print ListDeleteResponse.to_json()

# convert the object into a dict
list_delete_response_dict = list_delete_response_instance.to_dict()
# create an instance of ListDeleteResponse from a dict
list_delete_response_form_dict = list_delete_response.from_dict(list_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


