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
from pydantic import StrictInt, StrictStr
from pydantic import Field
from twitter_v2.models.media import Media
from twitter_v2.models.variant import Variant
from twitter_v2.models.video_all_of_non_public_metrics import VideoAllOfNonPublicMetrics
from twitter_v2.models.video_all_of_organic_metrics import VideoAllOfOrganicMetrics
from twitter_v2.models.video_all_of_promoted_metrics import VideoAllOfPromotedMetrics
from twitter_v2.models.video_all_of_public_metrics import VideoAllOfPublicMetrics
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Video(Media):
    """
    Video
    """ # noqa: E501
    duration_ms: Optional[StrictInt] = None
    non_public_metrics: Optional[VideoAllOfNonPublicMetrics] = None
    organic_metrics: Optional[VideoAllOfOrganicMetrics] = None
    preview_image_url: Optional[StrictStr] = None
    promoted_metrics: Optional[VideoAllOfPromotedMetrics] = None
    public_metrics: Optional[VideoAllOfPublicMetrics] = None
    variants: Optional[List[Variant]] = Field(default=None, description="An array of all available variants of the media.")
    __properties: ClassVar[List[str]] = ["height", "media_key", "type", "width", "duration_ms", "non_public_metrics", "organic_metrics", "preview_image_url", "promoted_metrics", "public_metrics", "variants"]

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
        """Create an instance of Video from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of non_public_metrics
        if self.non_public_metrics:
            _dict['non_public_metrics'] = self.non_public_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organic_metrics
        if self.organic_metrics:
            _dict['organic_metrics'] = self.organic_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promoted_metrics
        if self.promoted_metrics:
            _dict['promoted_metrics'] = self.promoted_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_metrics
        if self.public_metrics:
            _dict['public_metrics'] = self.public_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in variants (list)
        _items = []
        if self.variants:
            for _item in self.variants:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Video from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "height": obj.get("height"),
            "media_key": obj.get("media_key"),
            "type": obj.get("type"),
            "width": obj.get("width"),
            "duration_ms": obj.get("duration_ms"),
            "non_public_metrics": VideoAllOfNonPublicMetrics.from_dict(obj.get("non_public_metrics")) if obj.get("non_public_metrics") is not None else None,
            "organic_metrics": VideoAllOfOrganicMetrics.from_dict(obj.get("organic_metrics")) if obj.get("organic_metrics") is not None else None,
            "preview_image_url": obj.get("preview_image_url"),
            "promoted_metrics": VideoAllOfPromotedMetrics.from_dict(obj.get("promoted_metrics")) if obj.get("promoted_metrics") is not None else None,
            "public_metrics": VideoAllOfPublicMetrics.from_dict(obj.get("public_metrics")) if obj.get("public_metrics") is not None else None,
            "variants": [Variant.from_dict(_item) for _item in obj.get("variants")] if obj.get("variants") is not None else None
        })
        return _obj

