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
from openapi_client.models.url_image import UrlImage
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UrlFields(BaseModel):
    """
    Represent the portion of text recognized as a URL.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description of the URL landing page.")
    display_url: Optional[StrictStr] = Field(default=None, description="The URL as displayed in the Twitter client.")
    expanded_url: Optional[StrictStr] = Field(default=None, description="A validly formatted URL.")
    images: Optional[Annotated[List[UrlImage], Field(min_length=1)]] = None
    media_key: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The Media Key identifier for this attachment.")
    status: Optional[Annotated[int, Field(le=599, strict=True, ge=100)]] = Field(default=None, description="HTTP Status Code.")
    title: Optional[StrictStr] = Field(default=None, description="Title of the page the URL points to.")
    unwound_url: Optional[StrictStr] = Field(default=None, description="Fully resolved url.")
    url: StrictStr = Field(description="A validly formatted URL.")
    __properties: ClassVar[List[str]] = ["description", "display_url", "expanded_url", "images", "media_key", "status", "title", "unwound_url", "url"]

    @field_validator('media_key')
    def media_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+)_([0-9]+)$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+)_([0-9]+)$/")
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
        """Create an instance of UrlFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UrlFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "display_url": obj.get("display_url"),
            "expanded_url": obj.get("expanded_url"),
            "images": [UrlImage.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "media_key": obj.get("media_key"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "unwound_url": obj.get("unwound_url"),
            "url": obj.get("url")
        })
        return _obj


