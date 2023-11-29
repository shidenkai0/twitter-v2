# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.79
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.user_withheld_compliance_schema import UserWithheldComplianceSchema

class TestUserWithheldComplianceSchema(unittest.TestCase):
    """UserWithheldComplianceSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserWithheldComplianceSchema:
        """Test UserWithheldComplianceSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserWithheldComplianceSchema`
        """
        model = UserWithheldComplianceSchema()
        if include_optional:
            return UserWithheldComplianceSchema(
                user_withheld = openapi_client.models.user_takedown_compliance_schema.UserTakedownComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    user = openapi_client.models.user_compliance_schema_user.UserComplianceSchema_user(
                        id = '2244994945', ), 
                    withheld_in_countries = [
                        'US'
                        ], )
            )
        else:
            return UserWithheldComplianceSchema(
                user_withheld = openapi_client.models.user_takedown_compliance_schema.UserTakedownComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    user = openapi_client.models.user_compliance_schema_user.UserComplianceSchema_user(
                        id = '2244994945', ), 
                    withheld_in_countries = [
                        'US'
                        ], ),
        )
        """

    def testUserWithheldComplianceSchema(self):
        """Test UserWithheldComplianceSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
