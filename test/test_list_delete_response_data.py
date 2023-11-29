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

from openapi_client.models.list_delete_response_data import ListDeleteResponseData

class TestListDeleteResponseData(unittest.TestCase):
    """ListDeleteResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDeleteResponseData:
        """Test ListDeleteResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDeleteResponseData`
        """
        model = ListDeleteResponseData()
        if include_optional:
            return ListDeleteResponseData(
                deleted = True
            )
        else:
            return ListDeleteResponseData(
        )
        """

    def testListDeleteResponseData(self):
        """Test ListDeleteResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
