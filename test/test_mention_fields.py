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

from openapi_client.models.mention_fields import MentionFields

class TestMentionFields(unittest.TestCase):
    """MentionFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MentionFields:
        """Test MentionFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MentionFields`
        """
        model = MentionFields()
        if include_optional:
            return MentionFields(
                id = '2244994945',
                username = 'HqXzyC'
            )
        else:
            return MentionFields(
                username = 'HqXzyC',
        )
        """

    def testMentionFields(self):
        """Test MentionFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
