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

from openapi_client.models.tweet_delete_compliance_schema import TweetDeleteComplianceSchema

class TestTweetDeleteComplianceSchema(unittest.TestCase):
    """TweetDeleteComplianceSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TweetDeleteComplianceSchema:
        """Test TweetDeleteComplianceSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetDeleteComplianceSchema`
        """
        model = TweetDeleteComplianceSchema()
        if include_optional:
            return TweetDeleteComplianceSchema(
                delete = openapi_client.models.tweet_compliance_schema.TweetComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), )
            )
        else:
            return TweetDeleteComplianceSchema(
                delete = openapi_client.models.tweet_compliance_schema.TweetComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), ),
        )
        """

    def testTweetDeleteComplianceSchema(self):
        """Test TweetDeleteComplianceSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
