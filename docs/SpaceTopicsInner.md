# SpaceTopicsInner

The Twitter Topic object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the given topic. | [optional] 
**id** | **str** | An ID suitable for use in the REST API. | 
**name** | **str** | The name of the given topic. | 

## Example

```python
from twitter_v2.models.space_topics_inner import SpaceTopicsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceTopicsInner from a JSON string
space_topics_inner_instance = SpaceTopicsInner.from_json(json)
# print the JSON string representation of the object
print SpaceTopicsInner.to_json()

# convert the object into a dict
space_topics_inner_dict = space_topics_inner_instance.to_dict()
# create an instance of SpaceTopicsInner from a dict
space_topics_inner_form_dict = space_topics_inner.from_dict(space_topics_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


