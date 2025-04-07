# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.server_properties import ServerProperties

class TestServerProperties(unittest.TestCase):
    """ServerProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerProperties:
        """Test ServerProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerProperties`
        """
        model = ServerProperties()
        if include_optional:
            return ServerProperties(
                template_uuid = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                name = 'My resource',
                hostname = 'myHostname',
                cores = 4,
                ram = 4096,
                availability_zone = 'AUTO',
                vm_state = 'RUNNING',
                boot_cdrom = ionos_cloud_api_v6_client.models.resource_reference.ResourceReference(
                    id = '', 
                    type = 'resource', 
                    href = '<RESOURCE-URI>', ),
                boot_volume = ionos_cloud_api_v6_client.models.resource_reference.ResourceReference(
                    id = '', 
                    type = 'resource', 
                    href = '<RESOURCE-URI>', ),
                cpu_family = 'INTEL_ICELAKE',
                type = 'CUBE',
                placement_group_id = '',
                nic_multi_queue = True
            )
        else:
            return ServerProperties(
        )
        """

    def testServerProperties(self):
        """Test ServerProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
