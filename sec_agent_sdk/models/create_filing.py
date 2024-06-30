# coding: utf-8

"""
    sec-agent-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sec_agent_sdk.models.filing_table import FilingTable
from typing import Optional, Set
from typing_extensions import Self

class CreateFiling(BaseModel):
    """
    CreateFiling
    """ # noqa: E501
    company: StrictStr
    cik: Optional[StrictStr] = ''
    quarter: Optional[StrictStr] = ''
    date_filed: StrictStr
    url: Optional[StrictStr] = ''
    form_type: StrictStr
    table: FilingTable
    parsed: StrictStr
    __properties: ClassVar[List[str]] = ["company", "cik", "quarter", "date_filed", "url", "form_type", "table", "parsed"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateFiling from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateFiling from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "company": obj.get("company"),
            "cik": obj.get("cik") if obj.get("cik") is not None else '',
            "quarter": obj.get("quarter") if obj.get("quarter") is not None else '',
            "date_filed": obj.get("date_filed"),
            "url": obj.get("url") if obj.get("url") is not None else '',
            "form_type": obj.get("form_type"),
            "table": obj.get("table"),
            "parsed": obj.get("parsed")
        })
        return _obj

