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

from openapi_client.models.bookmark_mutation_response_data import BookmarkMutationResponseData

class TestBookmarkMutationResponseData(unittest.TestCase):
    """BookmarkMutationResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BookmarkMutationResponseData:
        """Test BookmarkMutationResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BookmarkMutationResponseData`
        """
        model = BookmarkMutationResponseData()
        if include_optional:
            return BookmarkMutationResponseData(
                bookmarked = True
            )
        else:
            return BookmarkMutationResponseData(
        )
        """

    def testBookmarkMutationResponseData(self):
        """Test BookmarkMutationResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
