# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.server_entities import ServerEntities

class TestServerEntities(unittest.TestCase):
    """ServerEntities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerEntities:
        """Test ServerEntities
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerEntities`
        """
        model = ServerEntities()
        if include_optional:
            return ServerEntities(
                cdroms = ionos_cloud_api_v6_client.models.cdroms.Cdroms(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.image.Image(
                            id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            type = 'image', 
                            href = '<RESOURCE-URI>', 
                            metadata = ionos_cloud_api_v6_client.models.datacenter_element_metadata.DatacenterElementMetadata(
                                etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                created_date = '2015-12-04T14:34:09.809Z', 
                                created_by = 'user@example.com', 
                                created_by_user_id = 'user@example.com', 
                                last_modified_date = '2015-12-04T14:34:09.809Z', 
                                last_modified_by = 'user@example.com', 
                                last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                                state = 'AVAILABLE', ), 
                            properties = ionos_cloud_api_v6_client.models.image_properties.ImageProperties(
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
                                cloud_init = 'V1', ), )
                        ], 
                    offset = 0, 
                    limit = 1000, 
                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                        prev = '<PREVIOUS-PAGE-URI>', 
                        self = '<THIS-PAGE-URI>', 
                        next = '<NEXT-PAGE-URI>', ), ),
                volumes = ionos_cloud_api_v6_client.models.attached_volumes.AttachedVolumes(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.volume.Volume(
                            id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            type = 'volume', 
                            href = '<RESOURCE-URI>', 
                            metadata = ionos_cloud_api_v6_client.models.datacenter_element_metadata.DatacenterElementMetadata(
                                etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                created_date = '2015-12-04T14:34:09.809Z', 
                                created_by = 'user@example.com', 
                                created_by_user_id = 'user@example.com', 
                                last_modified_date = '2015-12-04T14:34:09.809Z', 
                                last_modified_by = 'user@example.com', 
                                last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                                state = 'AVAILABLE', ), 
                            properties = ionos_cloud_api_v6_client.models.volume_properties.VolumeProperties(
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
                                boot_order = 'AUTO', ), )
                        ], 
                    offset = 0, 
                    limit = 1000, 
                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                        prev = '<PREVIOUS-PAGE-URI>', 
                        self = '<THIS-PAGE-URI>', 
                        next = '<NEXT-PAGE-URI>', ), ),
                nics = ionos_cloud_api_v6_client.models.nics.Nics(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.nic.Nic(
                            id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            type = 'nic', 
                            href = '<RESOURCE-URI>', 
                            metadata = ionos_cloud_api_v6_client.models.datacenter_element_metadata.DatacenterElementMetadata(
                                etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                created_date = '2015-12-04T14:34:09.809Z', 
                                created_by = 'user@example.com', 
                                created_by_user_id = 'user@example.com', 
                                last_modified_date = '2015-12-04T14:34:09.809Z', 
                                last_modified_by = 'user@example.com', 
                                last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                                state = 'AVAILABLE', ), 
                            properties = ionos_cloud_api_v6_client.models.nic_properties.NicProperties(
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
                                vnet = '', ), 
                            entities = ionos_cloud_api_v6_client.models.nic_entities.NicEntities(
                                flowlogs = ionos_cloud_api_v6_client.models.flow_logs.FlowLogs(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, 
                                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                                        prev = '<PREVIOUS-PAGE-URI>', 
                                        self = '<THIS-PAGE-URI>', 
                                        next = '<NEXT-PAGE-URI>', ), ), 
                                firewallrules = ionos_cloud_api_v6_client.models.firewall_rules.FirewallRules(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, ), 
                                securitygroups = ionos_cloud_api_v6_client.models.security_groups.SecurityGroups(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, ), ), )
                        ], 
                    offset = 0, 
                    limit = 1000, 
                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                        prev = '<PREVIOUS-PAGE-URI>', 
                        self = '<THIS-PAGE-URI>', 
                        next = '<NEXT-PAGE-URI>', ), ),
                securitygroups = ionos_cloud_api_v6_client.models.security_groups.SecurityGroups(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.security_group.SecurityGroup(
                            id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            type = 'security-group', 
                            href = '<RESOURCE-URI>', 
                            metadata = ionos_cloud_api_v6_client.models.datacenter_element_metadata.DatacenterElementMetadata(
                                etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                created_date = '2015-12-04T14:34:09.809Z', 
                                created_by = 'user@example.com', 
                                created_by_user_id = 'user@example.com', 
                                last_modified_date = '2015-12-04T14:34:09.809Z', 
                                last_modified_by = 'user@example.com', 
                                last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                                state = 'AVAILABLE', ), 
                            properties = ionos_cloud_api_v6_client.models.security_group_properties.SecurityGroupProperties(
                                name = 'My security group', 
                                description = 'My security group description', ), 
                            entities = ionos_cloud_api_v6_client.models.security_group_entities.SecurityGroupEntities(
                                rules = ionos_cloud_api_v6_client.models.firewall_rules.FirewallRules(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, 
                                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                                        prev = '<PREVIOUS-PAGE-URI>', 
                                        self = '<THIS-PAGE-URI>', 
                                        next = '<NEXT-PAGE-URI>', ), ), 
                                nics = ionos_cloud_api_v6_client.models.nics.Nics(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, ), 
                                servers = ionos_cloud_api_v6_client.models.servers.Servers(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', ), ), )
                        ], 
                    offset = 0, 
                    limit = 1000, 
                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                        prev = '<PREVIOUS-PAGE-URI>', 
                        self = '<THIS-PAGE-URI>', 
                        next = '<NEXT-PAGE-URI>', ), )
            )
        else:
            return ServerEntities(
        )
        """

    def testServerEntities(self):
        """Test ServerEntities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
