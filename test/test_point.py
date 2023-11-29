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

from openapi_client.models.point import Point

class TestPoint(unittest.TestCase):
    """Point unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Point:
        """Test Point
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Point`
        """
        model = Point()
        if include_optional:
            return Point(
                coordinates = [-105.18816086351444,40.247749999999996],
                type = 'Point'
            )
        else:
            return Point(
                coordinates = [-105.18816086351444,40.247749999999996],
                type = 'Point',
        )
        """

    def testPoint(self):
        """Test Point"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()