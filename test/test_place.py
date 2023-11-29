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

from openapi_client.models.place import Place

class TestPlace(unittest.TestCase):
    """Place unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Place:
        """Test Place
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Place`
        """
        model = Place()
        if include_optional:
            return Place(
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
                place_type = 'city'
            )
        else:
            return Place(
                full_name = 'Lakewood, CO',
                id = 'f7eb2fa2fea288b1',
        )
        """

    def testPlace(self):
        """Test Place"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
