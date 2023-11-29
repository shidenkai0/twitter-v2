# openapi_client.GeneralApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api_spec**](GeneralApi.md#get_open_api_spec) | **GET** /2/openapi.json | Returns the OpenAPI Specification document.
[**get_rule_count**](GeneralApi.md#get_rule_count) | **GET** /2/tweets/search/stream/rules/counts | Rules Count


# **get_open_api_spec**
> object get_open_api_spec()

Returns the OpenAPI Specification document.

Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.twitter.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.twitter.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GeneralApi(api_client)

    try:
        # Returns the OpenAPI Specification document.
        api_response = api_instance.get_open_api_spec()
        print("The response of GeneralApi->get_open_api_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_open_api_spec: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_count**
> Get2TweetsSearchStreamRulesCountsResponse get_rule_count(rules_count_fields=rules_count_fields)

Rules Count

Returns the counts of rules from a User's active rule set, to reflect usage by project and application.

### Example

* Bearer Authentication (BearerToken):
```python
import time
import os
import openapi_client
from openapi_client.models.get2_tweets_search_stream_rules_counts_response import Get2TweetsSearchStreamRulesCountsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.twitter.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.twitter.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerToken
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GeneralApi(api_client)
    rules_count_fields = ['[\"all_project_client_apps\",\"cap_per_client_app\",\"cap_per_project\",\"client_app_rules_count\",\"project_rules_count\"]'] # List[str] | A comma separated list of RulesCount fields to display. (optional)

    try:
        # Rules Count
        api_response = api_instance.get_rule_count(rules_count_fields=rules_count_fields)
        print("The response of GeneralApi->get_rule_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralApi->get_rule_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_count_fields** | [**List[str]**](str.md)| A comma separated list of RulesCount fields to display. | [optional] 

### Return type

[**Get2TweetsSearchStreamRulesCountsResponse**](Get2TweetsSearchStreamRulesCountsResponse.md)

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

