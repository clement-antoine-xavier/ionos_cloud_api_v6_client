# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.location_properties import LocationProperties

class TestLocationProperties(unittest.TestCase):
    """LocationProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocationProperties:
        """Test LocationProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocationProperties`
        """
        model = LocationProperties()
        if include_optional:
            return LocationProperties(
                name = 'berlin',
                features = ["cloud-init-private-image","ssd","vnf-nat"],
                image_aliases = ["windows:2012r2_iso","windows:2019_iso","ubuntu:18.04_iso"],
                cpu_architecture = [
                    openapi_client.models.cpu_architecture_properties.CpuArchitectureProperties(
                        cpu_family = 'INTEL_ICELAKE', 
                        max_cores = 62, 
                        max_ram = 245760, 
                        vendor = 'AuthenticAMD', )
                    ]
            )
        else:
            return LocationProperties(
        )
        """

    def testLocationProperties(self):
        """Test LocationProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
