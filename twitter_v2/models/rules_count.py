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
from twitter_v2.models.app_rules_count import AppRulesCount
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RulesCount(BaseModel):
    """
    A count of user-provided stream filtering rules at the application and project levels.
    """ # noqa: E501
    all_project_client_apps: Optional[List[AppRulesCount]] = Field(default=None, description="Client App Rule Counts for all applications in the project")
    cap_per_client_app: Optional[StrictInt] = Field(default=None, description="Cap of number of rules allowed per client application")
    cap_per_project: Optional[StrictInt] = Field(default=None, description="Cap of number of rules allowed per project")
    client_app_rules_count: Optional[AppRulesCount] = None
    project_rules_count: Optional[StrictInt] = Field(default=None, description="Number of rules for project")
    __properties: ClassVar[List[str]] = ["all_project_client_apps", "cap_per_client_app", "cap_per_project", "client_app_rules_count", "project_rules_count"]

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
        """Create an instance of RulesCount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in all_project_client_apps (list)
        _items = []
        if self.all_project_client_apps:
            for _item in self.all_project_client_apps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['all_project_client_apps'] = _items
        # override the default output from pydantic by calling `to_dict()` of client_app_rules_count
        if self.client_app_rules_count:
            _dict['client_app_rules_count'] = self.client_app_rules_count.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RulesCount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "all_project_client_apps": [AppRulesCount.from_dict(_item) for _item in obj.get("all_project_client_apps")] if obj.get("all_project_client_apps") is not None else None,
            "cap_per_client_app": obj.get("cap_per_client_app"),
            "cap_per_project": obj.get("cap_per_project"),
            "client_app_rules_count": AppRulesCount.from_dict(obj.get("client_app_rules_count")) if obj.get("client_app_rules_count") is not None else None,
            "project_rules_count": obj.get("project_rules_count")
        })
        return _obj

