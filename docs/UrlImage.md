# UrlImage

Represent the information for the URL image.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | The height of the media in pixels. | [optional] 
**url** | **str** | A validly formatted URL. | [optional] 
**width** | **int** | The width of the media in pixels. | [optional] 

## Example

```python
from twitter_v2.models.url_image import UrlImage

# TODO update the JSON string below
json = "{}"
# create an instance of UrlImage from a JSON string
url_image_instance = UrlImage.from_json(json)
# print the JSON string representation of the object
print UrlImage.to_json()

# convert the object into a dict
url_image_dict = url_image_instance.to_dict()
# create an instance of UrlImage from a dict
url_image_form_dict = url_image.from_dict(url_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


