# CreateFiling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** |  | 
**cik** | **str** |  | [optional] [default to '']
**quarter** | **str** |  | [optional] [default to '']
**date_filed** | **str** |  | 
**url** | **str** |  | [optional] [default to '']
**form_type** | **str** |  | 
**table** | [**FilingTable**](FilingTable.md) |  | 
**parsed** | **str** |  | 

## Example

```python
from sec_agent_sdk.models.create_filing import CreateFiling

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFiling from a JSON string
create_filing_instance = CreateFiling.from_json(json)
# print the JSON string representation of the object
print(CreateFiling.to_json())

# convert the object into a dict
create_filing_dict = create_filing_instance.to_dict()
# create an instance of CreateFiling from a dict
create_filing_from_dict = CreateFiling.from_dict(create_filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


