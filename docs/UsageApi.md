# twitter_api_v2.UsageApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_tweets**](UsageApi.md#get_usage_tweets) | **GET** /2/usage/tweets | Tweet Usage


# **get_usage_tweets**
> Get2UsageTweetsResponse get_usage_tweets(days=days, usage_fields=usage_fields)

Tweet Usage

Returns the Tweet Usage.

### Example

* Bearer Authentication (BearerToken):
```python
import time
import os
import twitter_api_v2
from twitter_api_v2.models.get2_usage_tweets_response import Get2UsageTweetsResponse
from twitter_api_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.twitter.com
# See configuration.py for a list of all supported configuration parameters.
configuration = twitter_api_v2.Configuration(
    host = "https://api.twitter.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerToken
configuration = twitter_api_v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with twitter_api_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = twitter_api_v2.UsageApi(api_client)
    days = 7 # int | The number of days for which you need usage for. (optional) (default to 7)
    usage_fields = ['[\"cap_reset_day\",\"daily_client_app_usage\",\"daily_project_usage\",\"project_cap\",\"project_id\",\"project_usage\"]'] # List[str] | A comma separated list of Usage fields to display. (optional)

    try:
        # Tweet Usage
        api_response = api_instance.get_usage_tweets(days=days, usage_fields=usage_fields)
        print("The response of UsageApi->get_usage_tweets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_tweets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| The number of days for which you need usage for. | [optional] [default to 7]
 **usage_fields** | [**List[str]**](str.md)| A comma separated list of Usage fields to display. | [optional] 

### Return type

[**Get2UsageTweetsResponse**](Get2UsageTweetsResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**0** | The request has failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

