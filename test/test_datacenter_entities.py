# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.datacenter_entities import DatacenterEntities

class TestDatacenterEntities(unittest.TestCase):
    """DatacenterEntities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatacenterEntities:
        """Test DatacenterEntities
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatacenterEntities`
        """
        model = DatacenterEntities()
        if include_optional:
            return DatacenterEntities(
                servers = ionos_cloud_api_v6_client.models.servers.Servers(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.server.Server(
                            id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            type = 'server', 
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
                            properties = ionos_cloud_api_v6_client.models.server_properties.ServerProperties(
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
                                nic_multi_queue = True, ), 
                            entities = ionos_cloud_api_v6_client.models.server_entities.ServerEntities(
                                cdroms = ionos_cloud_api_v6_client.models.cdroms.Cdroms(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
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
                                    offset = 0, 
                                    limit = 1000, ), 
                                nics = ionos_cloud_api_v6_client.models.nics.Nics(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, ), 
                                securitygroups = ionos_cloud_api_v6_client.models.security_groups.SecurityGroups(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', ), ), )
                        ], 
                    offset = 0, 
                    limit = 1000, 
                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                        prev = '<PREVIOUS-PAGE-URI>', 
                        self = '<THIS-PAGE-URI>', 
                        next = '<NEXT-PAGE-URI>', ), ),
                volumes = ionos_cloud_api_v6_client.models.volumes.Volumes(
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
                loadbalancers = ionos_cloud_api_v6_client.models.loadbalancers.Loadbalancers(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.loadbalancer.Loadbalancer(
                            id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            type = 'loadbalancer', 
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
                            properties = ionos_cloud_api_v6_client.models.loadbalancer_properties.LoadbalancerProperties(
                                name = 'My resource', 
                                ip = '22.231.113.64', 
                                dhcp = True, ), 
                            entities = ionos_cloud_api_v6_client.models.loadbalancer_entities.LoadbalancerEntities(
                                balancednics = ionos_cloud_api_v6_client.models.balanced_nics.BalancedNics(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, 
                                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                                        prev = '<PREVIOUS-PAGE-URI>', 
                                        self = '<THIS-PAGE-URI>', 
                                        next = '<NEXT-PAGE-URI>', ), ), ), )
                        ], 
                    offset = 0, 
                    limit = 1000, 
                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                        prev = '<PREVIOUS-PAGE-URI>', 
                        self = '<THIS-PAGE-URI>', 
                        next = '<NEXT-PAGE-URI>', ), ),
                lans = ionos_cloud_api_v6_client.models.lans.Lans(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.lan.Lan(
                            id = '5', 
                            type = 'lan', 
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
                            properties = ionos_cloud_api_v6_client.models.lan_properties.LanProperties(
                                name = 'My resource', 
                                ip_failover = [
                                    ionos_cloud_api_v6_client.models.ip_failover.IPFailover(
                                        ip = '192.18.2.231', 
                                        nic_uuid = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec', )
                                    ], 
                                ipv4_cidr_block = '10.8.130.0/23', 
                                ipv6_cidr_block = '2001:db8:b06d:8f5a::/64', 
                                pcc = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec', 
                                public = True, 
                                vni = 123, ), 
                            entities = ionos_cloud_api_v6_client.models.lan_entities.LanEntities(
                                nics = ionos_cloud_api_v6_client.models.lan_nics.LanNics(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, 
                                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                                        prev = '<PREVIOUS-PAGE-URI>', 
                                        self = '<THIS-PAGE-URI>', 
                                        next = '<NEXT-PAGE-URI>', ), ), ), )
                        ], 
                    offset = 0, 
                    limit = 1000, 
                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                        prev = '<PREVIOUS-PAGE-URI>', 
                        self = '<THIS-PAGE-URI>', 
                        next = '<NEXT-PAGE-URI>', ), ),
                networkloadbalancers = ionos_cloud_api_v6_client.models.network_load_balancers.NetworkLoadBalancers(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.network_load_balancer.NetworkLoadBalancer(
                            id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            type = 'networkloadbalancer', 
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
                            properties = ionos_cloud_api_v6_client.models.network_load_balancer_properties.NetworkLoadBalancerProperties(
                                name = 'My Network Load Balancer', 
                                listener_lan = 1, 
                                ips = ["81.173.1.2","22.231.2.2","22.231.2.3"], 
                                target_lan = 2, 
                                lb_private_ips = ["81.173.1.5/24","22.231.2.5/24"], 
                                central_logging = True, 
                                logging_format = '%{+Q}o %{-Q}ci - - [%trg] %r %ST %B "" "" %cp %ms %ft %b %s %TR %Tw %Tc %Tr %Ta %tsc %ac %fc %bc %sc %rc %sq %bq %CC %CS %hrl %hsl', ), 
                            entities = ionos_cloud_api_v6_client.models.network_load_balancer_entities.NetworkLoadBalancerEntities(
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
                                forwardingrules = ionos_cloud_api_v6_client.models.network_load_balancer_forwarding_rules.NetworkLoadBalancerForwardingRules(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', ), ), )
                        ], 
                    offset = 0, 
                    limit = 1000, 
                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                        prev = '<PREVIOUS-PAGE-URI>', 
                        self = '<THIS-PAGE-URI>', 
                        next = '<NEXT-PAGE-URI>', ), ),
                natgateways = ionos_cloud_api_v6_client.models.nat_gateways.NatGateways(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = 'collection', 
                    href = '<RESOURCE-URI>', 
                    items = [
                        ionos_cloud_api_v6_client.models.nat_gateway.NatGateway(
                            id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            type = 'natgateway', 
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
                            properties = ionos_cloud_api_v6_client.models.nat_gateway_properties.NatGatewayProperties(
                                name = 'My NAT Gateway', 
                                public_ips = ["81.173.1.2","82.231.2.5","92.221.2.4"], 
                                lans = [
                                    ionos_cloud_api_v6_client.models.nat_gateway_lan_properties.NatGatewayLanProperties(
                                        id = 3, 
                                        gateway_ips = ["10.12.1.2/24","10.11.2.5/24","10.11.2.4"], )
                                    ], ), 
                            entities = ionos_cloud_api_v6_client.models.nat_gateway_entities.NatGatewayEntities(
                                rules = ionos_cloud_api_v6_client.models.nat_gateway_rules.NatGatewayRules(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', ), 
                                flowlogs = ionos_cloud_api_v6_client.models.flow_logs.FlowLogs(
                                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    type = 'collection', 
                                    href = '<RESOURCE-URI>', 
                                    offset = 0, 
                                    limit = 1000, 
                                    _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                                        prev = '<PREVIOUS-PAGE-URI>', 
                                        self = '<THIS-PAGE-URI>', 
                                        next = '<NEXT-PAGE-URI>', ), ), ), )
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
                                    href = '<RESOURCE-URI>', ), 
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
            return DatacenterEntities(
        )
        """

    def testDatacenterEntities(self):
        """Test DatacenterEntities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
