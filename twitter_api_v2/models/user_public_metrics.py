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

class UserPublicMetrics(BaseModel):
    """
    A list of metrics for this User.
    """ # noqa: E501
    followers_count: StrictInt = Field(description="Number of Users who are following this User.")
    following_count: StrictInt = Field(description="Number of Users this User is following.")
    like_count: Optional[StrictInt] = Field(default=None, description="The number of likes created by this User.")
    listed_count: StrictInt = Field(description="The number of lists that include this User.")
    tweet_count: StrictInt = Field(description="The number of Tweets (including Retweets) posted by this User.")
    __properties: ClassVar[List[str]] = ["followers_count", "following_count", "like_count", "listed_count", "tweet_count"]

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
        """Create an instance of UserPublicMetrics from a JSON string"""
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
        """Create an instance of UserPublicMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "followers_count": obj.get("followers_count"),
            "following_count": obj.get("following_count"),
            "like_count": obj.get("like_count"),
            "listed_count": obj.get("listed_count"),
            "tweet_count": obj.get("tweet_count")
        })
        return _obj


