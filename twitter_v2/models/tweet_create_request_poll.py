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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TweetCreateRequestPoll(BaseModel):
    """
    Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.
    """ # noqa: E501
    duration_minutes: Annotated[int, Field(le=10080, strict=True, ge=5)] = Field(description="Duration of the poll in minutes.")
    options: Annotated[List[Annotated[str, Field(min_length=1, strict=True, max_length=25)]], Field(min_length=2, max_length=4)]
    reply_settings: Optional[StrictStr] = Field(default=None, description="Settings to indicate who can reply to the Tweet.")
    __properties: ClassVar[List[str]] = ["duration_minutes", "options", "reply_settings"]

    @field_validator('reply_settings')
    def reply_settings_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('following', 'mentionedUsers'):
            raise ValueError("must be one of enum values ('following', 'mentionedUsers')")
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
        """Create an instance of TweetCreateRequestPoll from a JSON string"""
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
        """Create an instance of TweetCreateRequestPoll from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "duration_minutes": obj.get("duration_minutes"),
            "options": obj.get("options"),
            "reply_settings": obj.get("reply_settings")
        })
        return _obj


