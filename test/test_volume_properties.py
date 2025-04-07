# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.volume_properties import VolumeProperties

class TestVolumeProperties(unittest.TestCase):
    """VolumeProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VolumeProperties:
        """Test VolumeProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VolumeProperties`
        """
        model = VolumeProperties()
        if include_optional:
            return VolumeProperties(
                name = 'My resource',
                type = 'HDD',
                size = 100,
                availability_zone = 'AUTO',
                image = 'd6ad1576-fde9-4696-aa41-1ebd75bdaf49',
                image_password = 'mypass123',
                image_alias = '',
                ssh_keys = ["ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyWh6LZ7f2wxnupVgtK2096bc69Vv9uT2A58lwN3ol0A6mxqlT0f4M1NbarVUxa+MVdxBLud5PvlkbYc9mY91OyzLGZMfVWvhAYz/tJSsDtsgRUl0GFVv332zDWk0i+mAVy0N408OORm5XqV6zvIDaiB/jopyjemUp2rnP7pXU4+98ilZw6ef9DF9y4YZ64mchL5//rcrGm1Lff3pC75X/polGONHeG6m4Vs8eIu+0epJ4PJBxO+rwRYp1zMnn90UCk21KvTcYops2cte7ouXQwkGUq3vmXxnSdvuivK/4JNoFQBsaGV974hDmloS5LOvSJjKpXs8Ed437ln712345","ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyWh6LZ7f2wxnupVgtK2096bc69Vv9uT2A58lwN3ol0A6mxqlT0f4M1NbarVUxa+MVdxBLud5PvlkbYc9mY91OyzLGZMfVWvhAYz/tJSsDtsgRUl0GFVv332zDWk0i+mAVy0N408OORm5XqV6zvIDaiB/jopyjemUp2rnP7pXU4+98ilZw6ef9DF9y4YZ64mchL5//rcrGm1Lff3pC75X/polGONHeG6m4Vs8eIu+0epJ4PJBxO+rwRYp1zMnn90UCk21KvTcYops2cte7ouXQwkGUq3vmXxnSdvuivK/asdfghjkjhyutry545tgvbn76e4rf43"],
                bus = 'VIRTIO',
                licence_type = 'LINUX',
                application_type = 'UNKNOWN',
                cpu_hot_plug = True,
                ram_hot_plug = True,
                nic_hot_plug = True,
                nic_hot_unplug = True,
                disc_virtio_hot_plug = True,
                disc_virtio_hot_unplug = True,
                expose_serial = True,
                require_legacy_bios = True,
                device_number = 3,
                pci_slot = 7,
                backupunit_id = '25f67991-0f51-4efc-a8ad-ef1fb31a481c',
                user_data = '',
                boot_server = '25f67991-0f51-4efc-a8ad-ef1fb31a481c',
                boot_order = 'AUTO'
            )
        else:
            return VolumeProperties(
                size = 100,
        )
        """

    def testVolumeProperties(self):
        """Test VolumeProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
