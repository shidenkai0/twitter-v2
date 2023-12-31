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

from openapi_client.models.tweet_withheld_compliance_schema import TweetWithheldComplianceSchema

class TestTweetWithheldComplianceSchema(unittest.TestCase):
    """TweetWithheldComplianceSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TweetWithheldComplianceSchema:
        """Test TweetWithheldComplianceSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetWithheldComplianceSchema`
        """
        model = TweetWithheldComplianceSchema()
        if include_optional:
            return TweetWithheldComplianceSchema(
                withheld = openapi_client.models.tweet_takedown_compliance_schema.TweetTakedownComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), 
                    withheld_in_countries = [
                        'US'
                        ], )
            )
        else:
            return TweetWithheldComplianceSchema(
                withheld = openapi_client.models.tweet_takedown_compliance_schema.TweetTakedownComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), 
                    withheld_in_countries = [
                        'US'
                        ], ),
        )
        """

    def testTweetWithheldComplianceSchema(self):
        """Test TweetWithheldComplianceSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
