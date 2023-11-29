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
from pydantic import BaseModel, field_validator
from pydantic import Field
from typing_extensions import Annotated
from twitter_api_v2.models.tweet_compliance_schema_tweet import TweetComplianceSchemaTweet
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TweetTakedownComplianceSchema(BaseModel):
    """
    TweetTakedownComplianceSchema
    """ # noqa: E501
    event_at: datetime = Field(description="Event time.")
    quote_tweet_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.")
    tweet: TweetComplianceSchemaTweet
    withheld_in_countries: Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1)]
    __properties: ClassVar[List[str]] = ["event_at", "quote_tweet_id", "tweet", "withheld_in_countries"]

    @field_validator('quote_tweet_id')
    def quote_tweet_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{1,19}$/")
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
        """Create an instance of TweetTakedownComplianceSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tweet
        if self.tweet:
            _dict['tweet'] = self.tweet.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TweetTakedownComplianceSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_at": obj.get("event_at"),
            "quote_tweet_id": obj.get("quote_tweet_id"),
            "tweet": TweetComplianceSchemaTweet.from_dict(obj.get("tweet")) if obj.get("tweet") is not None else None,
            "withheld_in_countries": obj.get("withheld_in_countries")
        })
        return _obj


