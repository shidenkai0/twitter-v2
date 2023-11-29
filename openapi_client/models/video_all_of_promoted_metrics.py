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
from pydantic import BaseModel, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VideoAllOfPromotedMetrics(BaseModel):
    """
    Promoted nonpublic engagement metrics for the Media at the time of the request.
    """ # noqa: E501
    playback_0_count: Optional[StrictInt] = Field(default=None, description="Number of users who made it through 0% of the video.")
    playback_100_count: Optional[StrictInt] = Field(default=None, description="Number of users who made it through 100% of the video.")
    playback_25_count: Optional[StrictInt] = Field(default=None, description="Number of users who made it through 25% of the video.")
    playback_50_count: Optional[StrictInt] = Field(default=None, description="Number of users who made it through 50% of the video.")
    playback_75_count: Optional[StrictInt] = Field(default=None, description="Number of users who made it through 75% of the video.")
    view_count: Optional[StrictInt] = Field(default=None, description="Number of times this video has been viewed.")
    __properties: ClassVar[List[str]] = ["playback_0_count", "playback_100_count", "playback_25_count", "playback_50_count", "playback_75_count", "view_count"]

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
        """Create an instance of VideoAllOfPromotedMetrics from a JSON string"""
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
        """Create an instance of VideoAllOfPromotedMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "playback_0_count": obj.get("playback_0_count"),
            "playback_100_count": obj.get("playback_100_count"),
            "playback_25_count": obj.get("playback_25_count"),
            "playback_50_count": obj.get("playback_50_count"),
            "playback_75_count": obj.get("playback_75_count"),
            "view_count": obj.get("view_count")
        })
        return _obj


