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
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from twitter_v2.models.expansions import Expansions
from twitter_v2.models.problem import Problem
from twitter_v2.models.user import User
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Get2UsersByResponse(BaseModel):
    """
    Get2UsersByResponse
    """ # noqa: E501
    data: Optional[Annotated[List[User], Field(min_length=1)]] = None
    errors: Optional[Annotated[List[Problem], Field(min_length=1)]] = None
    includes: Optional[Expansions] = None
    __properties: ClassVar[List[str]] = ["data", "errors", "includes"]

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
        """Create an instance of Get2UsersByResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of includes
        if self.includes:
            _dict['includes'] = self.includes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Get2UsersByResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [User.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "errors": [Problem.from_dict(_item) for _item in obj.get("errors")] if obj.get("errors") is not None else None,
            "includes": Expansions.from_dict(obj.get("includes")) if obj.get("includes") is not None else None
        })
        return _obj


