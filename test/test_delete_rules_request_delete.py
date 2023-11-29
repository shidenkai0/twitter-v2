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

from openapi_client.models.delete_rules_request_delete import DeleteRulesRequestDelete

class TestDeleteRulesRequestDelete(unittest.TestCase):
    """DeleteRulesRequestDelete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteRulesRequestDelete:
        """Test DeleteRulesRequestDelete
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteRulesRequestDelete`
        """
        model = DeleteRulesRequestDelete()
        if include_optional:
            return DeleteRulesRequestDelete(
                ids = [
                    '120897978112909812'
                    ],
                values = [
                    'coffee -is:retweet'
                    ]
            )
        else:
            return DeleteRulesRequestDelete(
        )
        """

    def testDeleteRulesRequestDelete(self):
        """Test DeleteRulesRequestDelete"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
