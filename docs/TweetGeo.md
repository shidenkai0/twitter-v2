# TweetGeo

The location tagged on the Tweet, if the user provided one.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**Point**](Point.md) |  | [optional] 
**place_id** | **str** | The identifier for this place. | [optional] 

## Example

```python
from twitter_api_v2.models.tweet_geo import TweetGeo

# TODO update the JSON string below
json = "{}"
# create an instance of TweetGeo from a JSON string
tweet_geo_instance = TweetGeo.from_json(json)
# print the JSON string representation of the object
print TweetGeo.to_json()

# convert the object into a dict
tweet_geo_dict = tweet_geo_instance.to_dict()
# create an instance of TweetGeo from a dict
tweet_geo_form_dict = tweet_geo.from_dict(tweet_geo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


