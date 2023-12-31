# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.79
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ComplianceJobType(str, Enum):
    """
    Type of compliance job to list.
    """

    """
    allowed enum values
    """
    TWEETS = 'tweets'
    USERS = 'users'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ComplianceJobType from a JSON string"""
        return cls(json.loads(json_str))


