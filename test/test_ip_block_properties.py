# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.ip_block_properties import IpBlockProperties

class TestIpBlockProperties(unittest.TestCase):
    """IpBlockProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IpBlockProperties:
        """Test IpBlockProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IpBlockProperties`
        """
        model = IpBlockProperties()
        if include_optional:
            return IpBlockProperties(
                ips = ["22.231.113.64","22.231.113.65","22.231.113.66"],
                location = 'us/las',
                size = 5,
                name = 'My resource',
                ip_consumers = [{"ip":"192.18.2.11","mac":"02:01:3f:52:6e:57","nicId":"0e8ee463-1174-46f2-87ba-a5c79c14d8e5","serverId":"e6a3466f-8d6e-4cb6-8001-f4e245f222b7","serverName":"Unnamed Server","datacenterId":"6e54a9ec-aace-4176-8ee4-1c3a704fccfc","datacenterName":"IpConsumerDC","k8sNodePoolUuid":"6e54a9ec-aace-4176-8ee4-1c3a704fcc12","k8sClusterUuid":"6e54a9ec-aace-4176-8ee4-1c3a704fcc23"}]
            )
        else:
            return IpBlockProperties(
                location = 'us/las',
                size = 5,
        )
        """

    def testIpBlockProperties(self):
        """Test IpBlockProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
