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

from openapi_client.models.get2_users_id_mentions_response_meta import Get2UsersIdMentionsResponseMeta

class TestGet2UsersIdMentionsResponseMeta(unittest.TestCase):
    """Get2UsersIdMentionsResponseMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Get2UsersIdMentionsResponseMeta:
        """Test Get2UsersIdMentionsResponseMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Get2UsersIdMentionsResponseMeta`
        """
        model = Get2UsersIdMentionsResponseMeta()
        if include_optional:
            return Get2UsersIdMentionsResponseMeta(
                newest_id = '',
                next_token = '0',
                oldest_id = '',
                previous_token = '0',
                result_count = 56
            )
        else:
            return Get2UsersIdMentionsResponseMeta(
        )
        """

    def testGet2UsersIdMentionsResponseMeta(self):
        """Test Get2UsersIdMentionsResponseMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
