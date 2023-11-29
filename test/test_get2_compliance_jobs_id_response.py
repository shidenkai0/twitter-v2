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

from openapi_client.models.get2_compliance_jobs_id_response import Get2ComplianceJobsIdResponse

class TestGet2ComplianceJobsIdResponse(unittest.TestCase):
    """Get2ComplianceJobsIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Get2ComplianceJobsIdResponse:
        """Test Get2ComplianceJobsIdResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Get2ComplianceJobsIdResponse`
        """
        model = Get2ComplianceJobsIdResponse()
        if include_optional:
            return Get2ComplianceJobsIdResponse(
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
            return Get2ComplianceJobsIdResponse(
        )
        """

    def testGet2ComplianceJobsIdResponse(self):
        """Test Get2ComplianceJobsIdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()