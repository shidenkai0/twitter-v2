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

from openapi_client.models.add_rules_request import AddRulesRequest

class TestAddRulesRequest(unittest.TestCase):
    """AddRulesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddRulesRequest:
        """Test AddRulesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddRulesRequest`
        """
        model = AddRulesRequest()
        if include_optional:
            return AddRulesRequest(
                add = [
                    openapi_client.models.rule_no_id.RuleNoId(
                        tag = 'Non-retweeted coffee Tweets', 
                        value = 'coffee -is:retweet', )
                    ]
            )
        else:
            return AddRulesRequest(
                add = [
                    openapi_client.models.rule_no_id.RuleNoId(
                        tag = 'Non-retweeted coffee Tweets', 
                        value = 'coffee -is:retweet', )
                    ],
        )
        """

    def testAddRulesRequest(self):
        """Test AddRulesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
