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

from openapi_client.models.rule import Rule

class TestRule(unittest.TestCase):
    """Rule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Rule:
        """Test Rule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Rule`
        """
        model = Rule()
        if include_optional:
            return Rule(
                id = '120897978112909812',
                tag = 'Non-retweeted coffee Tweets',
                value = 'coffee -is:retweet'
            )
        else:
            return Rule(
                value = 'coffee -is:retweet',
        )
        """

    def testRule(self):
        """Test Rule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
