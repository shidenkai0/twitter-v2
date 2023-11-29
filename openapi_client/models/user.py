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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from openapi_client.models.user_entities import UserEntities
from openapi_client.models.user_public_metrics import UserPublicMetrics
from openapi_client.models.user_withheld import UserWithheld
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class User(BaseModel):
    """
    The Twitter User object.
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, description="Creation time of this User.")
    description: Optional[StrictStr] = Field(default=None, description="The text of this User's profile description (also known as bio), if the User provided one.")
    entities: Optional[UserEntities] = None
    id: Annotated[str, Field(strict=True)] = Field(description="Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.")
    location: Optional[StrictStr] = Field(default=None, description="The location specified in the User's profile, if the User provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.")
    most_recent_tweet_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.")
    name: StrictStr = Field(description="The friendly name of this User, as shown on their profile.")
    pinned_tweet_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.")
    profile_image_url: Optional[StrictStr] = Field(default=None, description="The URL to the profile image for this User.")
    protected: Optional[StrictBool] = Field(default=None, description="Indicates if this User has chosen to protect their Tweets (in other words, if this User's Tweets are private).")
    public_metrics: Optional[UserPublicMetrics] = None
    url: Optional[StrictStr] = Field(default=None, description="The URL specified in the User's profile.")
    username: Annotated[str, Field(strict=True)] = Field(description="The Twitter handle (screen name) of this user.")
    verified: Optional[StrictBool] = Field(default=None, description="Indicate if this User is a verified Twitter User.")
    verified_type: Optional[StrictStr] = Field(default=None, description="The Twitter Blue verified type of the user, eg: blue, government, business or none.")
    withheld: Optional[UserWithheld] = None
    __properties: ClassVar[List[str]] = ["created_at", "description", "entities", "id", "location", "most_recent_tweet_id", "name", "pinned_tweet_id", "profile_image_url", "protected", "public_metrics", "url", "username", "verified", "verified_type", "withheld"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{1,19}$/")
        return value

    @field_validator('most_recent_tweet_id')
    def most_recent_tweet_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{1,19}$/")
        return value

    @field_validator('pinned_tweet_id')
    def pinned_tweet_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{1,19}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{1,19}$/")
        return value

    @field_validator('username')
    def username_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[A-Za-z0-9_]{1,15}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9_]{1,15}$/")
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
        """Create an instance of User from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entities
        if self.entities:
            _dict['entities'] = self.entities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_metrics
        if self.public_metrics:
            _dict['public_metrics'] = self.public_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of withheld
        if self.withheld:
            _dict['withheld'] = self.withheld.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "entities": UserEntities.from_dict(obj.get("entities")) if obj.get("entities") is not None else None,
            "id": obj.get("id"),
            "location": obj.get("location"),
            "most_recent_tweet_id": obj.get("most_recent_tweet_id"),
            "name": obj.get("name"),
            "pinned_tweet_id": obj.get("pinned_tweet_id"),
            "profile_image_url": obj.get("profile_image_url"),
            "protected": obj.get("protected"),
            "public_metrics": UserPublicMetrics.from_dict(obj.get("public_metrics")) if obj.get("public_metrics") is not None else None,
            "url": obj.get("url"),
            "username": obj.get("username"),
            "verified": obj.get("verified"),
            "verified_type": obj.get("verified_type"),
            "withheld": UserWithheld.from_dict(obj.get("withheld")) if obj.get("withheld") is not None else None
        })
        return _obj


