# Filing

Filing(*, company: str, cik: str, quarter: str, form_type: str, date_filed: datetime.date, url: str, table: str, parsed: str | None, accession_number: str, html_s3_url: str | None, image_s3_url: str | None, id: int = None)

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
from sec_agent_sdk.models.filing import Filing

# TODO update the JSON string below
json = "{}"
# create an instance of Filing from a JSON string
filing_instance = Filing.from_json(json)
# print the JSON string representation of the object
print(Filing.to_json())

# convert the object into a dict
filing_dict = filing_instance.to_dict()
# create an instance of Filing from a dict
filing_from_dict = Filing.from_dict(filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


