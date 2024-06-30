# sec_agent_sdk.DefaultApi

All URIs are relative to *https://c11yrich0c.execute-api.us-west-2.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_health_get**](DefaultApi.md#health_check_health_get) | **GET** /health | Health Check
[**search_filing_v1_sec_filing_get**](DefaultApi.md#search_filing_v1_sec_filing_get) | **GET** /v1/sec-filing | Search Filing
[**search_filing_v2_v1_sec_filing_v2_get**](DefaultApi.md#search_filing_v2_v1_sec_filing_v2_get) | **GET** /v1/sec-filing-v2 | Search Filing V2


# **health_check_health_get**
> str health_check_health_get()

Health Check

### Example


```python
import sec_agent_sdk
from sec_agent_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://c11yrich0c.execute-api.us-west-2.amazonaws.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sec_agent_sdk.Configuration(
    host = "https://c11yrich0c.execute-api.us-west-2.amazonaws.com"
)


# Enter a context with an instance of the API client
with sec_agent_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sec_agent_sdk.DefaultApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_health_get()
        print("The response of DefaultApi->health_check_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_filing_v1_sec_filing_get**
> Filing search_filing_v1_sec_filing_get(form_type, company, table, date_filed=date_filed)

Search Filing

Search sec filings

### Example


```python
import sec_agent_sdk
from sec_agent_sdk.models.filing import Filing
from sec_agent_sdk.models.filing_table import FilingTable
from sec_agent_sdk.models.form_type import FormType
from sec_agent_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://c11yrich0c.execute-api.us-west-2.amazonaws.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sec_agent_sdk.Configuration(
    host = "https://c11yrich0c.execute-api.us-west-2.amazonaws.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with sec_agent_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sec_agent_sdk.DefaultApi(api_client)
    form_type = sec_agent_sdk.FormType() # FormType | 
    company = 'company_example' # str | 
    table = sec_agent_sdk.FilingTable() # FilingTable | 
    date_filed = 'date_filed_example' # str |  (optional)

    try:
        # Search Filing
        api_response = api_instance.search_filing_v1_sec_filing_get(form_type, company, table, date_filed=date_filed)
        print("The response of DefaultApi->search_filing_v1_sec_filing_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_filing_v1_sec_filing_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_type** | [**FormType**](.md)|  | 
 **company** | **str**|  | 
 **table** | [**FilingTable**](.md)|  | 
 **date_filed** | **str**|  | [optional] 

### Return type

[**Filing**](Filing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_filing_v2_v1_sec_filing_v2_get**
> FilingV2 search_filing_v2_v1_sec_filing_v2_get(form_type, company, table, date_filed=date_filed)

Search Filing V2

Search sec filings

### Example


```python
import sec_agent_sdk
from sec_agent_sdk.models.filing_table import FilingTable
from sec_agent_sdk.models.filing_v2 import FilingV2
from sec_agent_sdk.models.form_type import FormType
from sec_agent_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://c11yrich0c.execute-api.us-west-2.amazonaws.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sec_agent_sdk.Configuration(
    host = "https://c11yrich0c.execute-api.us-west-2.amazonaws.com"
)


# Enter a context with an instance of the API client
with sec_agent_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sec_agent_sdk.DefaultApi(api_client)
    form_type = sec_agent_sdk.FormType() # FormType | 
    company = 'company_example' # str | 
    table = sec_agent_sdk.FilingTable() # FilingTable | 
    date_filed = 'date_filed_example' # str |  (optional)

    try:
        # Search Filing V2
        api_response = api_instance.search_filing_v2_v1_sec_filing_v2_get(form_type, company, table, date_filed=date_filed)
        print("The response of DefaultApi->search_filing_v2_v1_sec_filing_v2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_filing_v2_v1_sec_filing_v2_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_type** | [**FormType**](.md)|  | 
 **company** | **str**|  | 
 **table** | [**FilingTable**](.md)|  | 
 **date_filed** | **str**|  | [optional] 

### Return type

[**FilingV2**](FilingV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

