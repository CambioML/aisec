# coding: utf-8

"""
    sec-agent-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sec_agent_sdk.models.filing import Filing

class TestFiling(unittest.TestCase):
    """Filing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Filing:
        """Test Filing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Filing`
        """
        model = Filing()
        if include_optional:
            return Filing(
                company = '',
                cik = '',
                quarter = '',
                form_type = '',
                date_filed = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                url = '',
                table = '',
                parsed = '',
                accession_number = '',
                html_s3_url = '',
                image_s3_url = '',
                id = 56
            )
        else:
            return Filing(
                company = '',
                cik = '',
                quarter = '',
                form_type = '',
                date_filed = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                url = '',
                table = '',
                parsed = '',
                accession_number = '',
                html_s3_url = '',
                image_s3_url = '',
        )
        """

    def testFiling(self):
        """Test Filing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
