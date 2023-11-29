# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.79
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from twitter_api_v2.models.compliance_job_status import ComplianceJobStatus
from twitter_api_v2.models.compliance_job_type import ComplianceJobType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ComplianceJob(BaseModel):
    """
    ComplianceJob
    """ # noqa: E501
    created_at: datetime = Field(description="Creation time of the compliance job.")
    download_expires_at: datetime = Field(description="Expiration time of the download URL.")
    download_url: StrictStr = Field(description="URL from which the user will retrieve their compliance results.")
    id: Annotated[str, Field(strict=True)] = Field(description="Compliance Job ID.")
    name: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="User-provided name for a compliance job.")
    status: ComplianceJobStatus
    type: ComplianceJobType
    upload_expires_at: datetime = Field(description="Expiration time of the upload URL.")
    upload_url: StrictStr = Field(description="URL to which the user will upload their Tweet or user IDs.")
    __properties: ClassVar[List[str]] = ["created_at", "download_expires_at", "download_url", "id", "name", "status", "type", "upload_expires_at", "upload_url"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{1,19}$/")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ComplianceJob from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ComplianceJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "download_expires_at": obj.get("download_expires_at"),
            "download_url": obj.get("download_url"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "upload_expires_at": obj.get("upload_expires_at"),
            "upload_url": obj.get("upload_url")
        })
        return _obj


