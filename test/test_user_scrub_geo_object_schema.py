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

from openapi_client.models.user_scrub_geo_object_schema import UserScrubGeoObjectSchema

class TestUserScrubGeoObjectSchema(unittest.TestCase):
    """UserScrubGeoObjectSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserScrubGeoObjectSchema:
        """Test UserScrubGeoObjectSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserScrubGeoObjectSchema`
        """
        model = UserScrubGeoObjectSchema()
        if include_optional:
            return UserScrubGeoObjectSchema(
                event_at = '2021-07-06T18:40:40Z',
                up_to_tweet_id = '1346889436626259968',
                user = openapi_client.models.user_compliance_schema_user.UserComplianceSchema_user(
                    id = '2244994945', )
            )
        else:
            return UserScrubGeoObjectSchema(
                event_at = '2021-07-06T18:40:40Z',
                up_to_tweet_id = '1346889436626259968',
                user = openapi_client.models.user_compliance_schema_user.UserComplianceSchema_user(
                    id = '2244994945', ),
        )
        """

    def testUserScrubGeoObjectSchema(self):
        """Test UserScrubGeoObjectSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()