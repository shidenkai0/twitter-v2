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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from twitter_v2.models.tweet_create_request_geo import TweetCreateRequestGeo
from twitter_v2.models.tweet_create_request_media import TweetCreateRequestMedia
from twitter_v2.models.tweet_create_request_poll import TweetCreateRequestPoll
from twitter_v2.models.tweet_create_request_reply import TweetCreateRequestReply
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TweetCreateRequest(BaseModel):
    """
    TweetCreateRequest
    """ # noqa: E501
    card_uri: Optional[StrictStr] = Field(default=None, description="Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link.")
    direct_message_deep_link: Optional[StrictStr] = Field(default=None, description="Link to take the conversation from the public timeline to a private Direct Message.")
    for_super_followers_only: Optional[StrictBool] = Field(default=False, description="Exclusive Tweet for super followers.")
    geo: Optional[TweetCreateRequestGeo] = None
    media: Optional[TweetCreateRequestMedia] = None
    nullcast: Optional[StrictBool] = Field(default=False, description="Nullcasted (promoted-only) Tweets do not appear in the public timeline and are not served to followers.")
    poll: Optional[TweetCreateRequestPoll] = None
    quote_tweet_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.")
    reply: Optional[TweetCreateRequestReply] = None
    reply_settings: Optional[StrictStr] = Field(default=None, description="Settings to indicate who can reply to the Tweet.")
    text: Optional[StrictStr] = Field(default=None, description="The content of the Tweet.")
    __properties: ClassVar[List[str]] = ["card_uri", "direct_message_deep_link", "for_super_followers_only", "geo", "media", "nullcast", "poll", "quote_tweet_id", "reply", "reply_settings", "text"]

    @field_validator('quote_tweet_id')
    def quote_tweet_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{1,19}$/")
        return value

    @field_validator('reply_settings')
    def reply_settings_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('following', 'mentionedUsers', 'subscribers'):
            raise ValueError("must be one of enum values ('following', 'mentionedUsers', 'subscribers')")
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
        """Create an instance of TweetCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of geo
        if self.geo:
            _dict['geo'] = self.geo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media
        if self.media:
            _dict['media'] = self.media.to_dict()
        # override the default output from pydantic by calling `to_dict()` of poll
        if self.poll:
            _dict['poll'] = self.poll.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reply
        if self.reply:
            _dict['reply'] = self.reply.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TweetCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "card_uri": obj.get("card_uri"),
            "direct_message_deep_link": obj.get("direct_message_deep_link"),
            "for_super_followers_only": obj.get("for_super_followers_only") if obj.get("for_super_followers_only") is not None else False,
            "geo": TweetCreateRequestGeo.from_dict(obj.get("geo")) if obj.get("geo") is not None else None,
            "media": TweetCreateRequestMedia.from_dict(obj.get("media")) if obj.get("media") is not None else None,
            "nullcast": obj.get("nullcast") if obj.get("nullcast") is not None else False,
            "poll": TweetCreateRequestPoll.from_dict(obj.get("poll")) if obj.get("poll") is not None else None,
            "quote_tweet_id": obj.get("quote_tweet_id"),
            "reply": TweetCreateRequestReply.from_dict(obj.get("reply")) if obj.get("reply") is not None else None,
            "reply_settings": obj.get("reply_settings"),
            "text": obj.get("text")
        })
        return _obj

