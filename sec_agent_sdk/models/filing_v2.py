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

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FilingV2(BaseModel):
    """
    FilingV2(*, company: str, cik: str, quarter: str, form_type: str, date_filed: datetime.date, url: str, table: str, parsed: str | None, accession_number: str, html_s3_url: str | None, image_s3_url: str | None, id: int = None)
    """ # noqa: E501
    company: StrictStr
    cik: StrictStr
    quarter: StrictStr
    form_type: StrictStr
    date_filed: date
    url: StrictStr
    table: StrictStr
    parsed: Optional[StrictStr]
    accession_number: StrictStr
    html_s3_url: Optional[StrictStr]
    image_s3_url: Optional[StrictStr]
    id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["company", "cik", "quarter", "form_type", "date_filed", "url", "table", "parsed", "accession_number", "html_s3_url", "image_s3_url", "id"]

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
        """Create an instance of FilingV2 from a JSON string"""
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
        # set to None if parsed (nullable) is None
        # and model_fields_set contains the field
        if self.parsed is None and "parsed" in self.model_fields_set:
            _dict['parsed'] = None

        # set to None if html_s3_url (nullable) is None
        # and model_fields_set contains the field
        if self.html_s3_url is None and "html_s3_url" in self.model_fields_set:
            _dict['html_s3_url'] = None

        # set to None if image_s3_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_s3_url is None and "image_s3_url" in self.model_fields_set:
            _dict['image_s3_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FilingV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "company": obj.get("company"),
            "cik": obj.get("cik"),
            "quarter": obj.get("quarter"),
            "form_type": obj.get("form_type"),
            "date_filed": obj.get("date_filed"),
            "url": obj.get("url"),
            "table": obj.get("table"),
            "parsed": obj.get("parsed"),
            "accession_number": obj.get("accession_number"),
            "html_s3_url": obj.get("html_s3_url"),
            "image_s3_url": obj.get("image_s3_url"),
            "id": obj.get("id")
        })
        return _obj


