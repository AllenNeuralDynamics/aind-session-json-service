# aind_session_json_service_async_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_session**](DefaultApi.md#get_session) | **POST** /bergamo | Get Session


# **get_session**
> JobResponse get_session(job_settings)

Get Session

## Get Session JSON metadata file.

### Example


```python
import aind_session_json_service_async_client
from aind_session_json_service_async_client.models.job_response import JobResponse
from aind_session_json_service_async_client.models.job_settings import JobSettings
from aind_session_json_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_session_json_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with aind_session_json_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_session_json_service_async_client.DefaultApi(api_client)
    job_settings = aind_session_json_service_async_client.JobSettings() # JobSettings | 

    try:
        # Get Session
        api_response = await api_instance.get_session(job_settings)
        print("The response of DefaultApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_settings** | [**JobSettings**](JobSettings.md)|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

