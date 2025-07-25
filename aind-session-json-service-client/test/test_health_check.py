# coding: utf-8

"""
    aind-session-json-service

     ## aind-session-json-service  Run metadata mapper to create a session metadata  

    The version of the OpenAPI document: 0.1.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from aind_session_json_service_client.models.health_check import HealthCheck

class TestHealthCheck(unittest.TestCase):
    """HealthCheck unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HealthCheck:
        """Test HealthCheck
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HealthCheck`
        """
        model = HealthCheck()
        if include_optional:
            return HealthCheck(
                status = 'OK',
                service_version = '0.1.3'
            )
        else:
            return HealthCheck(
        )
        """

    def testHealthCheck(self):
        """Test HealthCheck"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
