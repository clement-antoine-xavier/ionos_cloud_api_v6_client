# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.image_properties import ImageProperties

class TestImageProperties(unittest.TestCase):
    """ImageProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageProperties:
        """Test ImageProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageProperties`
        """
        model = ImageProperties()
        if include_optional:
            return ImageProperties(
                name = 'My resource',
                description = 'The image/snapshot of Ubuntu ',
                location = 'us/las',
                size = 100,
                cpu_hot_plug = True,
                cpu_hot_unplug = True,
                ram_hot_plug = True,
                ram_hot_unplug = True,
                nic_hot_plug = True,
                nic_hot_unplug = True,
                disc_virtio_hot_plug = True,
                disc_virtio_hot_unplug = True,
                disc_scsi_hot_plug = True,
                disc_scsi_hot_unplug = True,
                expose_serial = True,
                require_legacy_bios = True,
                licence_type = 'LINUX',
                application_type = 'UNKNOWN',
                image_type = 'HDD',
                public = True,
                image_aliases = [
                    ''
                    ],
                cloud_init = 'V1'
            )
        else:
            return ImageProperties(
                licence_type = 'LINUX',
        )
        """

    def testImageProperties(self):
        """Test ImageProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
