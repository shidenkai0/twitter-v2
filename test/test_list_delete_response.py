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

from openapi_client.models.list_delete_response import ListDeleteResponse

class TestListDeleteResponse(unittest.TestCase):
    """ListDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDeleteResponse:
        """Test ListDeleteResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDeleteResponse`
        """
        model = ListDeleteResponse()
        if include_optional:
            return ListDeleteResponse(
                data = openapi_client.models.list_delete_response_data.ListDeleteResponse_data(
                    deleted = True, ),
                errors = [
                    openapi_client.models.problem.Problem(
                        detail = '', 
                        status = 56, 
                        title = '', 
                        type = '', )
                    ]
            )
        else:
            return ListDeleteResponse(
        )
        """

    def testListDeleteResponse(self):
        """Test ListDeleteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
