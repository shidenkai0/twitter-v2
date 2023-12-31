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
from pydantic import BaseModel, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Problem(BaseModel):
    """
    An HTTP Problem Details object, as defined in IETF RFC 7807 (https://tools.ietf.org/html/rfc7807).
    """ # noqa: E501
    detail: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    title: StrictStr
    type: StrictStr
    __properties: ClassVar[List[str]] = ["detail", "status", "title", "type"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'about:blank': 'GenericProblem','https://api.twitter.com/2/problems/client-disconnected': 'ClientDisconnectedProblem','https://api.twitter.com/2/problems/client-forbidden': 'ClientForbiddenProblem','https://api.twitter.com/2/problems/conflict': 'ConflictProblem','https://api.twitter.com/2/problems/disallowed-resource': 'DisallowedResourceProblem','https://api.twitter.com/2/problems/duplicate-rules': 'DuplicateRuleProblem','https://api.twitter.com/2/problems/invalid-request': 'InvalidRequestProblem','https://api.twitter.com/2/problems/invalid-rules': 'InvalidRuleProblem','https://api.twitter.com/2/problems/noncompliant-rules': 'NonCompliantRulesProblem','https://api.twitter.com/2/problems/not-authorized-for-field': 'FieldUnauthorizedProblem','https://api.twitter.com/2/problems/not-authorized-for-resource': 'ResourceUnauthorizedProblem','https://api.twitter.com/2/problems/oauth1-permissions': 'Oauth1PermissionsProblem','https://api.twitter.com/2/problems/operational-disconnect': 'OperationalDisconnectProblem','https://api.twitter.com/2/problems/resource-not-found': 'ResourceNotFoundProblem','https://api.twitter.com/2/problems/resource-unavailable': 'ResourceUnavailableProblem','https://api.twitter.com/2/problems/rule-cap': 'RulesCapProblem','https://api.twitter.com/2/problems/streaming-connection': 'ConnectionExceptionProblem','https://api.twitter.com/2/problems/unsupported-authentication': 'UnsupportedAuthenticationProblem','https://api.twitter.com/2/problems/usage-capped': 'UsageCapExceededProblem'
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
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of Problem from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of Problem from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("Problem failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from twitter_v2.models.client_disconnected_problem import ClientDisconnectedProblem
from twitter_v2.models.client_forbidden_problem import ClientForbiddenProblem
from twitter_v2.models.conflict_problem import ConflictProblem
from twitter_v2.models.connection_exception_problem import ConnectionExceptionProblem
from twitter_v2.models.disallowed_resource_problem import DisallowedResourceProblem
from twitter_v2.models.duplicate_rule_problem import DuplicateRuleProblem
from twitter_v2.models.field_unauthorized_problem import FieldUnauthorizedProblem
from twitter_v2.models.generic_problem import GenericProblem
from twitter_v2.models.invalid_request_problem import InvalidRequestProblem
from twitter_v2.models.invalid_rule_problem import InvalidRuleProblem
from twitter_v2.models.non_compliant_rules_problem import NonCompliantRulesProblem
from twitter_v2.models.oauth1_permissions_problem import Oauth1PermissionsProblem
from twitter_v2.models.operational_disconnect_problem import OperationalDisconnectProblem
from twitter_v2.models.resource_not_found_problem import ResourceNotFoundProblem
from twitter_v2.models.resource_unauthorized_problem import ResourceUnauthorizedProblem
from twitter_v2.models.resource_unavailable_problem import ResourceUnavailableProblem
from twitter_v2.models.rules_cap_problem import RulesCapProblem
from twitter_v2.models.unsupported_authentication_problem import UnsupportedAuthenticationProblem
from twitter_v2.models.usage_cap_exceeded_problem import UsageCapExceededProblem
# TODO: Rewrite to not use raise_errors
Problem.model_rebuild(raise_errors=False)

