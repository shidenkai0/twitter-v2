# Get2SpacesByCreatorIdsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Space]**](Space.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 
**includes** | [**Expansions**](Expansions.md) |  | [optional] 
**meta** | [**Get2ComplianceJobsResponseMeta**](Get2ComplianceJobsResponseMeta.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.get2_spaces_by_creator_ids_response import Get2SpacesByCreatorIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2SpacesByCreatorIdsResponse from a JSON string
get2_spaces_by_creator_ids_response_instance = Get2SpacesByCreatorIdsResponse.from_json(json)
# print the JSON string representation of the object
print Get2SpacesByCreatorIdsResponse.to_json()

# convert the object into a dict
get2_spaces_by_creator_ids_response_dict = get2_spaces_by_creator_ids_response_instance.to_dict()
# create an instance of Get2SpacesByCreatorIdsResponse from a dict
get2_spaces_by_creator_ids_response_form_dict = get2_spaces_by_creator_ids_response.from_dict(get2_spaces_by_creator_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


