# FilingV2

FilingV2(*, company: str, cik: str, quarter: str, form_type: str, date_filed: datetime.date, url: str, table: str, parsed: str | None, accession_number: str, html_s3_url: str | None, image_s3_url: str | None, id: int = None)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** |  | 
**cik** | **str** |  | 
**quarter** | **str** |  | 
**form_type** | **str** |  | 
**date_filed** | **date** |  | 
**url** | **str** |  | 
**table** | **str** |  | 
**parsed** | **str** |  | 
**accession_number** | **str** |  | 
**html_s3_url** | **str** |  | 
**image_s3_url** | **str** |  | 
**id** | **int** |  | [optional] 

## Example

```python
from sec_agent_sdk.models.filing_v2 import FilingV2

# TODO update the JSON string below
json = "{}"
# create an instance of FilingV2 from a JSON string
filing_v2_instance = FilingV2.from_json(json)
# print the JSON string representation of the object
print(FilingV2.to_json())

# convert the object into a dict
filing_v2_dict = filing_v2_instance.to_dict()
# create an instance of FilingV2 from a dict
filing_v2_from_dict = FilingV2.from_dict(filing_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


