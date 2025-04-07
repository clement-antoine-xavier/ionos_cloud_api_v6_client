# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.nat_gateway_rule_properties import NatGatewayRuleProperties

class TestNatGatewayRuleProperties(unittest.TestCase):
    """NatGatewayRuleProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NatGatewayRuleProperties:
        """Test NatGatewayRuleProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NatGatewayRuleProperties`
        """
        model = NatGatewayRuleProperties()
        if include_optional:
            return NatGatewayRuleProperties(
                name = 'My NAT Gateway rule',
                type = 'SNAT',
                protocol = 'TCP',
                source_subnet = '10.0.1.0/24',
                public_ip = '192.18.7.17',
                target_subnet = '10.0.1.0/24',
                target_port_range = openapi_client.models.target_port_range.TargetPortRange(
                    start = 10000, 
                    end = 20000, )
            )
        else:
            return NatGatewayRuleProperties(
                name = 'My NAT Gateway rule',
                source_subnet = '10.0.1.0/24',
                public_ip = '192.18.7.17',
        )
        """

    def testNatGatewayRuleProperties(self):
        """Test NatGatewayRuleProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
