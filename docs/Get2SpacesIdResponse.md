# Get2SpacesIdResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Space**](Space.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 
**includes** | [**Expansions**](Expansions.md) |  | [optional] 

## Example

```python
from openapi_client.models.get2_spaces_id_response import Get2SpacesIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2SpacesIdResponse from a JSON string
get2_spaces_id_response_instance = Get2SpacesIdResponse.from_json(json)
# print the JSON string representation of the object
print Get2SpacesIdResponse.to_json()

# convert the object into a dict
get2_spaces_id_response_dict = get2_spaces_id_response_instance.to_dict()
# create an instance of Get2SpacesIdResponse from a dict
get2_spaces_id_response_form_dict = get2_spaces_id_response.from_dict(get2_spaces_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

