# sec_agent_sdk.DefaultApi

All URIs are relative to *https://c11yrich0c.execute-api.us-west-2.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_sec_filing**](DefaultApi.md#search_sec_filing) | **GET** /v1/sec-filing | Search sec filing


# **search_sec_filing**
> Filing search_sec_filing(form_type, company, date_filed, table)

Search sec filing

Search sec filing

### Example

* Api Key Authentication (APIKeyHeader):

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
    date_filed = 'date_filed_example' # str | 
    table = sec_agent_sdk.FilingTable() # FilingTable | 

    try:
        # Search sec filing
        api_response = api_instance.search_sec_filing(form_type, company, date_filed, table)
        print("The response of DefaultApi->search_sec_filing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_sec_filing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_type** | [**FormType**](.md)|  | 
 **company** | **str**|  | 
 **date_filed** | **str**|  | 
 **table** | [**FilingTable**](.md)|  | 

### Return type

[**Filing**](Filing.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

