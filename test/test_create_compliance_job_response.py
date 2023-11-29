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

from openapi_client.models.create_compliance_job_response import CreateComplianceJobResponse

class TestCreateComplianceJobResponse(unittest.TestCase):
    """CreateComplianceJobResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateComplianceJobResponse:
        """Test CreateComplianceJobResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateComplianceJobResponse`
        """
        model = CreateComplianceJobResponse()
        if include_optional:
            return CreateComplianceJobResponse(
                data = openapi_client.models.compliance_job.ComplianceJob(
                    created_at = '2021-01-06T18:40:40Z', 
                    download_expires_at = '2021-01-06T18:40:40Z', 
                    download_url = '', 
                    id = '1372966999991541762', 
                    name = 'my-job', 
                    status = 'created', 
                    type = 'tweets', 
                    upload_expires_at = '2021-01-06T18:40:40Z', 
                    upload_url = '', ),
                errors = [
                    openapi_client.models.problem.Problem(
                        detail = '', 
                        status = 56, 
                        title = '', 
                        type = '', )
                    ]
            )
        else:
            return CreateComplianceJobResponse(
        )
        """

    def testCreateComplianceJobResponse(self):
        """Test CreateComplianceJobResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()