# sec-agent-sdk
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Generator version: 7.6.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sec_agent_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sec_agent_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import sec_agent_sdk
from sec_agent_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sec_agent_sdk.Configuration(
    host = "http://localhost"
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
    except ApiException as e:
        print("Exception when calling DefaultApi->health_check_health_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

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




