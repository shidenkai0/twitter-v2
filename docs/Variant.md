# Variant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bit_rate** | **int** | The bit rate of the media. | [optional] 
**content_type** | **str** | The content type of the media. | [optional] 
**url** | **str** | The url to the media. | [optional] 

## Example

```python
from twitter_api_v2.models.variant import Variant

# TODO update the JSON string below
json = "{}"
# create an instance of Variant from a JSON string
variant_instance = Variant.from_json(json)
# print the JSON string representation of the object
print Variant.to_json()

# convert the object into a dict
variant_dict = variant_instance.to_dict()
# create an instance of Variant from a dict
variant_form_dict = variant.from_dict(variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


