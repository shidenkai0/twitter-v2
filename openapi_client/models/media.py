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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Media(BaseModel):
    """
    Media
    """ # noqa: E501
    height: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The height of the media in pixels.")
    media_key: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The Media Key identifier for this attachment.")
    type: StrictStr
    width: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The width of the media in pixels.")
    __properties: ClassVar[List[str]] = ["height", "media_key", "type", "width"]

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


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'animated_gif': 'AnimatedGif','photo': 'Photo','video': 'Video'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union[Self, Self, Self]:
        """Create an instance of Media from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self]:
        """Create an instance of Media from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("Media failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.animated_gif import AnimatedGif
from openapi_client.models.photo import Photo
from openapi_client.models.video import Video
# TODO: Rewrite to not use raise_errors
Media.model_rebuild(raise_errors=False)

