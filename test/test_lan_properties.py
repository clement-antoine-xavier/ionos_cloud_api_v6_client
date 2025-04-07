# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.lan_properties import LanProperties

class TestLanProperties(unittest.TestCase):
    """LanProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LanProperties:
        """Test LanProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LanProperties`
        """
        model = LanProperties()
        if include_optional:
            return LanProperties(
                name = 'My resource',
                ip_failover = [
                    openapi_client.models.ip_failover.IPFailover(
                        ip = '192.18.2.231', 
                        nic_uuid = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec', )
                    ],
                ipv4_cidr_block = '10.8.130.0/23',
                ipv6_cidr_block = '2001:db8:b06d:8f5a::/64',
                pcc = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec',
                public = True,
                vni = 123
            )
        else:
            return LanProperties(
        )
        """

    def testLanProperties(self):
        """Test LanProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
