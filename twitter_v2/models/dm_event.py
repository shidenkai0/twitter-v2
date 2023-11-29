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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from twitter_v2.models.dm_event_attachments import DmEventAttachments
from twitter_v2.models.dm_event_referenced_tweets_inner import DmEventReferencedTweetsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DmEvent(BaseModel):
    """
    DmEvent
    """ # noqa: E501
    attachments: Optional[DmEventAttachments] = None
    created_at: Optional[datetime] = None
    dm_conversation_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Unique identifier of a DM conversation. This can either be a numeric string, or a pair of numeric strings separated by a '-' character in the case of one-on-one DM Conversations.")
    event_type: StrictStr
    id: Annotated[str, Field(strict=True)] = Field(description="Unique identifier of a DM Event.")
    participant_ids: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1)]] = Field(default=None, description="A list of participants for a ParticipantsJoin or ParticipantsLeave event_type.")
    referenced_tweets: Optional[Annotated[List[DmEventReferencedTweetsInner], Field(min_length=1)]] = Field(default=None, description="A list of Tweets this DM refers to.")
    sender_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.")
    text: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["attachments", "created_at", "dm_conversation_id", "event_type", "id", "participant_ids", "referenced_tweets", "sender_id", "text"]

    @field_validator('dm_conversation_id')
    def dm_conversation_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,19}-[0-9]{1,19}|[0-9]{15,19})$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,19}-[0-9]{1,19}|[0-9]{15,19})$/")
        return value

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{1,19}$/")
        return value

    @field_validator('sender_id')
    def sender_id_validate_regular_expression(cls, value):
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
        """Create an instance of DmEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attachments
        if self.attachments:
            _dict['attachments'] = self.attachments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in referenced_tweets (list)
        _items = []
        if self.referenced_tweets:
            for _item in self.referenced_tweets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['referenced_tweets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DmEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attachments": DmEventAttachments.from_dict(obj.get("attachments")) if obj.get("attachments") is not None else None,
            "created_at": obj.get("created_at"),
            "dm_conversation_id": obj.get("dm_conversation_id"),
            "event_type": obj.get("event_type"),
            "id": obj.get("id"),
            "participant_ids": obj.get("participant_ids"),
            "referenced_tweets": [DmEventReferencedTweetsInner.from_dict(_item) for _item in obj.get("referenced_tweets")] if obj.get("referenced_tweets") is not None else None,
            "sender_id": obj.get("sender_id"),
            "text": obj.get("text")
        })
        return _obj


