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

from openapi_client.models.tweet_compliance_data import TweetComplianceData

class TestTweetComplianceData(unittest.TestCase):
    """TweetComplianceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TweetComplianceData:
        """Test TweetComplianceData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetComplianceData`
        """
        model = TweetComplianceData()
        if include_optional:
            return TweetComplianceData(
                delete = openapi_client.models.tweet_compliance_schema.TweetComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), ),
                withheld = openapi_client.models.tweet_takedown_compliance_schema.TweetTakedownComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), 
                    withheld_in_countries = [
                        'US'
                        ], ),
                drop = openapi_client.models.tweet_compliance_schema.TweetComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), ),
                undrop = openapi_client.models.tweet_compliance_schema.TweetComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), ),
                tweet_edit = openapi_client.models.tweet_edit_compliance_object_schema.TweetEditComplianceObjectSchema(
                    edit_tweet_ids = [
                        '1346889436626259968'
                        ], 
                    event_at = '2021-07-06T18:40:40Z', 
                    initial_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.dm_event_referenced_tweets_inner.DmEvent_referenced_tweets_inner(
                        id = '1346889436626259968', ), )
            )
        else:
            return TweetComplianceData(
                delete = openapi_client.models.tweet_compliance_schema.TweetComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), ),
                withheld = openapi_client.models.tweet_takedown_compliance_schema.TweetTakedownComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), 
                    withheld_in_countries = [
                        'US'
                        ], ),
                drop = openapi_client.models.tweet_compliance_schema.TweetComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), ),
                undrop = openapi_client.models.tweet_compliance_schema.TweetComplianceSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    quote_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.tweet_compliance_schema_tweet.TweetComplianceSchema_tweet(
                        author_id = '2244994945', 
                        id = '1346889436626259968', ), ),
                tweet_edit = openapi_client.models.tweet_edit_compliance_object_schema.TweetEditComplianceObjectSchema(
                    edit_tweet_ids = [
                        '1346889436626259968'
                        ], 
                    event_at = '2021-07-06T18:40:40Z', 
                    initial_tweet_id = '1346889436626259968', 
                    tweet = openapi_client.models.dm_event_referenced_tweets_inner.DmEvent_referenced_tweets_inner(
                        id = '1346889436626259968', ), ),
        )
        """

    def testTweetComplianceData(self):
        """Test TweetComplianceData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
