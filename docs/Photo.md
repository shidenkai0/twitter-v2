# Photo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from twitter_api_v2.models.photo import Photo

# TODO update the JSON string below
json = "{}"
# create an instance of Photo from a JSON string
photo_instance = Photo.from_json(json)
# print the JSON string representation of the object
print Photo.to_json()

# convert the object into a dict
photo_dict = photo_instance.to_dict()
# create an instance of Photo from a dict
photo_form_dict = photo.from_dict(photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


