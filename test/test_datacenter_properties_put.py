# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.datacenter_properties_put import DatacenterPropertiesPut

class TestDatacenterPropertiesPut(unittest.TestCase):
    """DatacenterPropertiesPut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatacenterPropertiesPut:
        """Test DatacenterPropertiesPut
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatacenterPropertiesPut`
        """
        model = DatacenterPropertiesPut()
        if include_optional:
            return DatacenterPropertiesPut(
                name = 'Production Datacenter',
                description = 'My Production Datacenter',
                location = 'us/las',
                version = 8,
                features = ["SSD"],
                sec_auth_protection = True,
                cpu_architecture = [
                    ionos_cloud_api_v6_client.models.cpu_architecture_properties.CpuArchitectureProperties(
                        cpu_family = 'INTEL_ICELAKE', 
                        max_cores = 62, 
                        max_ram = 245760, 
                        vendor = 'AuthenticAMD', )
                    ],
                ipv6_cidr_block = '2001:db8:b06d:8f00::/56',
                default_security_group_id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                create_default_security_group = True
            )
        else:
            return DatacenterPropertiesPut(
                location = 'us/las',
        )
        """

    def testDatacenterPropertiesPut(self):
        """Test DatacenterPropertiesPut"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
