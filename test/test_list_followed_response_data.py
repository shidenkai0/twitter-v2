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

from openapi_client.models.list_followed_response_data import ListFollowedResponseData

class TestListFollowedResponseData(unittest.TestCase):
    """ListFollowedResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListFollowedResponseData:
        """Test ListFollowedResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListFollowedResponseData`
        """
        model = ListFollowedResponseData()
        if include_optional:
            return ListFollowedResponseData(
                following = True
            )
        else:
            return ListFollowedResponseData(
        )
        """

    def testListFollowedResponseData(self):
        """Test ListFollowedResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
