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

from openapi_client.models.tweet_compliance_stream_response_one_of import TweetComplianceStreamResponseOneOf

class TestTweetComplianceStreamResponseOneOf(unittest.TestCase):
    """TweetComplianceStreamResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TweetComplianceStreamResponseOneOf:
        """Test TweetComplianceStreamResponseOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetComplianceStreamResponseOneOf`
        """
        model = TweetComplianceStreamResponseOneOf()
        if include_optional:
            return TweetComplianceStreamResponseOneOf(
                data = None
            )
        else:
            return TweetComplianceStreamResponseOneOf(
                data = None,
        )
        """

    def testTweetComplianceStreamResponseOneOf(self):
        """Test TweetComplianceStreamResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()