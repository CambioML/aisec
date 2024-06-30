# AI Agent for SEC Fillings
The library is an experiment to extract SEC fillings data in real-time.

## Requirements.

Python 3.7+

💻 Installation

```sh
pip install git+ssh://git@github.com:CambioML/aisec.git#main

# Or

pip install git+https://github.com/CambioML/aisec.git

# Or

poetry add git+ssh://git@github.com:CambioML/aisec.git#main
```

🌱 Set up your CambioML API key for AI SEC
Please reach out at info@cambioml.com for an API key.

📜 Examples

```python
import os
import sec_agent_sdk
from sec_agent_sdk import ApiClient, DefaultApi, FilingTable, FormType
from sec_agent_sdk.rest import ApiException
from pprint import pprint

configuration = sec_agent_sdk.Configuration()

# Configure API key authorization: APIKeyHeader
configuration.api_key["APIKeyHeader"] = "YOUR-API-KEY"

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = DefaultApi(api_client)
    form_type = FormType.EIGHT_K  # FormType | 10-K | 10-Q | 8-K | 6-K
    company = "AAPL"  # ticker
    table = (
        FilingTable.BALANCE_SHEET
    )  # FilingTable | 'cash-flow-statement' | 'income-statement' | 'balance-sheet'
     # date_filed = '2024-04-17' # optional str (date string in YYYY-mm-dd) or None(the latest filing will be retrieved)

    try:
        # Search sec filing
        api_response = api_instance.search_sec_filing_get(form_type, company, table)
        print("The response of DefaultApi->search_sec_filing:\n")
        pprint(api_response)

        # Search sec filing v2
        api_response = api_instance.search_sec_filing_v2_get(form_type, company, table)
        print("The response of DefaultApi->search_sec_filing_v2:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->search_sec_filing: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://c11yrich0c.execute-api.us-west-2.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**health_check_health_get**](docs/DefaultApi.md#health_check_health_get) | **GET** /health | Health Check
*DefaultApi* | [**search_filing_v1_sec_filing_get**](docs/DefaultApi.md#search_filing_v1_sec_filing_get) | **GET** /v1/sec-filing | Search Filing
*DefaultApi* | [**search_filing_v2_v1_sec_filing_v2_get**](docs/DefaultApi.md#search_filing_v2_v1_sec_filing_v2_get) | **GET** /v1/sec-filing-v2 | Search Filing V2


## Documentation For Models

 - [CreateFiling](docs/CreateFiling.md)
 - [Filing](docs/Filing.md)
 - [FilingTable](docs/FilingTable.md)
 - [FilingV2](docs/FilingV2.md)
 - [FormType](docs/FormType.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [PatchFiling](docs/PatchFiling.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




