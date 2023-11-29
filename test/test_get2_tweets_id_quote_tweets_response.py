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

from openapi_client.models.get2_tweets_id_quote_tweets_response import Get2TweetsIdQuoteTweetsResponse

class TestGet2TweetsIdQuoteTweetsResponse(unittest.TestCase):
    """Get2TweetsIdQuoteTweetsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Get2TweetsIdQuoteTweetsResponse:
        """Test Get2TweetsIdQuoteTweetsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Get2TweetsIdQuoteTweetsResponse`
        """
        model = Get2TweetsIdQuoteTweetsResponse()
        if include_optional:
            return Get2TweetsIdQuoteTweetsResponse(
                data = [
                    {"author_id":"2244994945","created_at":"Wed Jan 06 18:40:40 +0000 2021","id":"1346889436626259968","text":"Learn how to use the user Tweet timeline and user mention timeline endpoints in the Twitter API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i"}
                    ],
                errors = [
                    openapi_client.models.problem.Problem(
                        detail = '', 
                        status = 56, 
                        title = '', 
                        type = '', )
                    ],
                includes = openapi_client.models.expansions.Expansions(
                    media = [
                        openapi_client.models.media.Media(
                            height = 0, 
                            media_key = '4_072888001528021798096225500850762068629', 
                            type = '', 
                            width = 0, )
                        ], 
                    places = [
                        openapi_client.models.place.Place(
                            contained_within = [
                                'f7eb2fa2fea288b1'
                                ], 
                            country = 'United States', 
                            country_code = 'US', 
                            full_name = 'Lakewood, CO', 
                            geo = openapi_client.models.geo.Geo(
                                bbox = [-105.193475,39.60973,-105.053164,39.761974], 
                                geometry = openapi_client.models.point.Point(
                                    coordinates = [-105.18816086351444,40.247749999999996], 
                                    type = 'Point', ), 
                                properties = openapi_client.models.properties.properties(), 
                                type = 'Feature', ), 
                            id = 'f7eb2fa2fea288b1', 
                            name = 'Lakewood', 
                            place_type = 'city', )
                        ], 
                    polls = [
                        openapi_client.models.poll.Poll(
                            duration_minutes = 5, 
                            end_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '1365059861688410112', 
                            options = [
                                openapi_client.models.poll_option.PollOption(
                                    label = '0', 
                                    position = 56, 
                                    votes = 56, )
                                ], 
                            voting_status = 'open', )
                        ], 
                    topics = [
                        openapi_client.models.topic.Topic(
                            description = 'All about technology', 
                            id = '', 
                            name = 'Technology', )
                        ], 
                    tweets = [
                        {"author_id":"2244994945","created_at":"Wed Jan 06 18:40:40 +0000 2021","id":"1346889436626259968","text":"Learn how to use the user Tweet timeline and user mention timeline endpoints in the Twitter API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i"}
                        ], 
                    users = [
                        {"created_at":"2013-12-14T04:35:55Z","id":"2244994945","name":"Twitter Dev","protected":false,"username":"TwitterDev"}
                        ], ),
                meta = openapi_client.models.get2_tweets_id_quote_tweets_response_meta.Get2TweetsIdQuoteTweetsResponse_meta(
                    next_token = '0', 
                    result_count = 56, )
            )
        else:
            return Get2TweetsIdQuoteTweetsResponse(
        )
        """

    def testGet2TweetsIdQuoteTweetsResponse(self):
        """Test Get2TweetsIdQuoteTweetsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
