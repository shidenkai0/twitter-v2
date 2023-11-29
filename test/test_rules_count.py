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

from openapi_client.models.rules_count import RulesCount

class TestRulesCount(unittest.TestCase):
    """RulesCount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RulesCount:
        """Test RulesCount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RulesCount`
        """
        model = RulesCount()
        if include_optional:
            return RulesCount(
                all_project_client_apps = [
                    openapi_client.models.app_rules_count.AppRulesCount(
                        client_app_id = '0', 
                        rule_count = 56, )
                    ],
                cap_per_client_app = 56,
                cap_per_project = 56,
                client_app_rules_count = openapi_client.models.app_rules_count.AppRulesCount(
                    client_app_id = '0', 
                    rule_count = 56, ),
                project_rules_count = 56
            )
        else:
            return RulesCount(
        )
        """

    def testRulesCount(self):
        """Test RulesCount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
