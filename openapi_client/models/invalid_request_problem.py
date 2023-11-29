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

from pydantic import Field
from typing_extensions import Annotated
from openapi_client.models.invalid_request_problem_all_of_errors import InvalidRequestProblemAllOfErrors
from openapi_client.models.problem import Problem
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InvalidRequestProblem(Problem):
    """
    A problem that indicates this request is invalid.
    """ # noqa: E501
    errors: Optional[Annotated[List[InvalidRequestProblemAllOfErrors], Field(min_length=1)]] = None
    __properties: ClassVar[List[str]] = ["detail", "status", "title", "type", "errors"]

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
        """Create an instance of InvalidRequestProblem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of InvalidRequestProblem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "detail": obj.get("detail"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "errors": [InvalidRequestProblemAllOfErrors.from_dict(_item) for _item in obj.get("errors")] if obj.get("errors") is not None else None
        })
        return _obj


