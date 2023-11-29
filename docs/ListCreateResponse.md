# ListCreateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListCreateResponseData**](ListCreateResponseData.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.list_create_response import ListCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCreateResponse from a JSON string
list_create_response_instance = ListCreateResponse.from_json(json)
# print the JSON string representation of the object
print ListCreateResponse.to_json()

# convert the object into a dict
list_create_response_dict = list_create_response_instance.to_dict()
# create an instance of ListCreateResponse from a dict
list_create_response_form_dict = list_create_response.from_dict(list_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


