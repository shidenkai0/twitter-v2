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

from openapi_client.models.create_dm_event_response_data import CreateDmEventResponseData

class TestCreateDmEventResponseData(unittest.TestCase):
    """CreateDmEventResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateDmEventResponseData:
        """Test CreateDmEventResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDmEventResponseData`
        """
        model = CreateDmEventResponseData()
        if include_optional:
            return CreateDmEventResponseData(
                dm_conversation_id = '123123123-456456456',
                dm_event_id = '1146654567674912769'
            )
        else:
            return CreateDmEventResponseData(
                dm_conversation_id = '123123123-456456456',
                dm_event_id = '1146654567674912769',
        )
        """

    def testCreateDmEventResponseData(self):
        """Test CreateDmEventResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()