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
from twitter_v2.models.poll_option import PollOption
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Poll(BaseModel):
    """
    Represent a Poll attached to a Tweet.
    """ # noqa: E501
    duration_minutes: Optional[Annotated[int, Field(le=10080, strict=True, ge=5)]] = None
    end_datetime: Optional[datetime] = None
    id: Annotated[str, Field(strict=True)] = Field(description="Unique identifier of this poll.")
    options: Annotated[List[PollOption], Field(min_length=2, max_length=4)]
    voting_status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["duration_minutes", "end_datetime", "id", "options", "voting_status"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{1,19}$/")
        return value

    @field_validator('voting_status')
    def voting_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('open', 'closed'):
            raise ValueError("must be one of enum values ('open', 'closed')")
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
        """Create an instance of Poll from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item in self.options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Poll from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "duration_minutes": obj.get("duration_minutes"),
            "end_datetime": obj.get("end_datetime"),
            "id": obj.get("id"),
            "options": [PollOption.from_dict(_item) for _item in obj.get("options")] if obj.get("options") is not None else None,
            "voting_status": obj.get("voting_status")
        })
        return _obj

