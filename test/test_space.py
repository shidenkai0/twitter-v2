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

from openapi_client.models.space import Space

class TestSpace(unittest.TestCase):
    """Space unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Space:
        """Test Space
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Space`
        """
        model = Space()
        if include_optional:
            return Space(
                created_at = '2021-07-06T18:40:40Z',
                creator_id = '2244994945',
                ended_at = '2021-07-06T18:40:40Z',
                host_ids = [
                    '2244994945'
                    ],
                id = '1SLjjRYNejbKM',
                invited_user_ids = [
                    '2244994945'
                    ],
                is_ticketed = False,
                lang = 'en',
                participant_count = 10,
                scheduled_start = '2021-07-06T18:40:40Z',
                speaker_ids = [
                    '2244994945'
                    ],
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                state = 'live',
                subscriber_count = 10,
                title = 'Spaces are Awesome',
                topics = [
                    {"description":"All about technology","id":"848920371311001600","name":"Technology"}
                    ],
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Space(
                id = '1SLjjRYNejbKM',
                state = 'live',
        )
        """

    def testSpace(self):
        """Test Space"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()