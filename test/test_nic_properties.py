# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.nic_properties import NicProperties

class TestNicProperties(unittest.TestCase):
    """NicProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NicProperties:
        """Test NicProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NicProperties`
        """
        model = NicProperties()
        if include_optional:
            return NicProperties(
                name = 'My resource',
                mac = '00:0a:95:9d:68:16',
                ips = ["10.160.12.12"],
                dhcp = True,
                ipv6_ips = ["2001:db8:b06d:8f5a:0609::1"],
                ipv6_cidr_block = '2001:db8:b06d:8f5a:0609::/80',
                dhcpv6 = True,
                lan = 2,
                firewall_active = False,
                firewall_type = 'INGRESS',
                device_number = 3,
                pci_slot = 7,
                vnet = ''
            )
        else:
            return NicProperties(
                lan = 2,
        )
        """

    def testNicProperties(self):
        """Test NicProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
