import sys

sys.path.append(".")
sys.path.append("..")
sys.path.append("../..")

from pprint import pprint

import sec_agent_sdk
from sec_agent_sdk import ApiClient, DefaultApi, FilingTable, FormType
from sec_agent_sdk.rest import ApiException

configuration = sec_agent_sdk.Configuration()

# Configure API key authorization: APIKeyHeader
configuration.api_key["APIKeyHeader"] = "YOUR-API-KEY"

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = DefaultApi(api_client)
    form_type = FormType.EIGHT_K  # FormType | 10-K | 10-Q | 8-K | 6-K
    company = "AAPL"  # ticker
    # date_filed = '2024-04-17' # str | date string in YYYY-mm-dd
    table = (
        FilingTable.BALANCE_SHEET
    )  # FilingTable | 'cash-flow-statement' | 'income-statement' | 'balance-sheet'

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
