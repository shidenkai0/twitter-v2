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

from openapi_client.models.oauth1_permissions_problem import Oauth1PermissionsProblem

class TestOauth1PermissionsProblem(unittest.TestCase):
    """Oauth1PermissionsProblem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Oauth1PermissionsProblem:
        """Test Oauth1PermissionsProblem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Oauth1PermissionsProblem`
        """
        model = Oauth1PermissionsProblem()
        if include_optional:
            return Oauth1PermissionsProblem(
            )
        else:
            return Oauth1PermissionsProblem(
        )
        """

    def testOauth1PermissionsProblem(self):
        """Test Oauth1PermissionsProblem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()