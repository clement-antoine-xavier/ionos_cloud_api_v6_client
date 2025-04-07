# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.datacenter import Datacenter

class TestDatacenter(unittest.TestCase):
    """Datacenter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Datacenter:
        """Test Datacenter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Datacenter`
        """
        model = Datacenter()
        if include_optional:
            return Datacenter(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = 'datacenter',
                href = '<RESOURCE-URI>',
                metadata = openapi_client.models.datacenter_element_metadata.DatacenterElementMetadata(
                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                    created_date = '2015-12-04T14:34:09.809Z', 
                    created_by = 'user@example.com', 
                    created_by_user_id = 'user@example.com', 
                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                    last_modified_by = 'user@example.com', 
                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                    state = 'AVAILABLE', ),
                properties = openapi_client.models.datacenter_properties.DatacenterProperties(
                    name = 'Production datacenter', 
                    description = 'My Production Datacenter', 
                    location = 'us/las', 
                    version = 8, 
                    features = ["SSD"], 
                    sec_auth_protection = True, 
                    cpu_architecture = [
                        openapi_client.models.cpu_architecture_properties.CpuArchitectureProperties(
                            cpu_family = 'INTEL_ICELAKE', 
                            max_cores = 62, 
                            max_ram = 245760, 
                            vendor = 'AuthenticAMD', )
                        ], 
                    ipv6_cidr_block = '2001:db8:b06d:8f00::/56', 
                    default_security_group_id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', ),
                entities = openapi_client.models.datacenter_entities.DatacenterEntities(
                    servers = openapi_client.models.servers.Servers(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', 
                        items = [
                            openapi_client.models.server.Server(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = 'server', 
                                href = '<RESOURCE-URI>', 
                                metadata = openapi_client.models.datacenter_element_metadata.DatacenterElementMetadata(
                                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                    created_date = '2015-12-04T14:34:09.809Z', 
                                    created_by = 'user@example.com', 
                                    created_by_user_id = 'user@example.com', 
                                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                                    last_modified_by = 'user@example.com', 
                                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                                    state = 'AVAILABLE', ), 
                                properties = openapi_client.models.server_properties.ServerProperties(
                                    template_uuid = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                    name = 'My resource', 
                                    hostname = 'myHostname', 
                                    cores = 4, 
                                    ram = 4096, 
                                    availability_zone = 'AUTO', 
                                    vm_state = 'RUNNING', 
                                    boot_cdrom = openapi_client.models.resource_reference.ResourceReference(
                                        id = '', 
                                        type = 'resource', 
                                        href = '<RESOURCE-URI>', ), 
                                    boot_volume = openapi_client.models.resource_reference.ResourceReference(
                                        id = '', 
                                        type = 'resource', 
                                        href = '<RESOURCE-URI>', ), 
                                    cpu_family = 'INTEL_ICELAKE', 
                                    type = 'CUBE', 
                                    placement_group_id = '', 
                                    nic_multi_queue = True, ), 
                                entities = openapi_client.models.server_entities.ServerEntities(
                                    cdroms = openapi_client.models.cdroms.Cdroms(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = 'collection', 
                                        href = '<RESOURCE-URI>', 
                                        offset = 0, 
                                        limit = 1000, 
                                        _links = openapi_client.models.pagination_links.PaginationLinks(
                                            prev = '<PREVIOUS-PAGE-URI>', 
                                            self = '<THIS-PAGE-URI>', 
                                            next = '<NEXT-PAGE-URI>', ), ), 
                                    volumes = openapi_client.models.attached_volumes.AttachedVolumes(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = 'collection', 
                                        href = '<RESOURCE-URI>', 
                                        offset = 0, 
                                        limit = 1000, ), 
                                    nics = openapi_client.models.nics.Nics(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = 'collection', 
                                        href = '<RESOURCE-URI>', 
                                        offset = 0, 
                                        limit = 1000, ), 
                                    securitygroups = openapi_client.models.security_groups.SecurityGroups(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = 'collection', 
                                        href = '<RESOURCE-URI>', ), ), )
                            ], 
                        offset = 0, 
                        limit = 1000, 
                        _links = openapi_client.models.pagination_links.PaginationLinks(
                            prev = '<PREVIOUS-PAGE-URI>', 
                            self = '<THIS-PAGE-URI>', 
                            next = '<NEXT-PAGE-URI>', ), ), 
                    volumes = openapi_client.models.volumes.Volumes(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', ), 
                    loadbalancers = openapi_client.models.loadbalancers.Loadbalancers(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', ), 
                    lans = openapi_client.models.lans.Lans(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', ), 
                    networkloadbalancers = openapi_client.models.network_load_balancers.NetworkLoadBalancers(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', ), 
                    natgateways = openapi_client.models.nat_gateways.NatGateways(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', ), 
                    securitygroups = openapi_client.models.security_groups.SecurityGroups(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', ), )
            )
        else:
            return Datacenter(
                properties = openapi_client.models.datacenter_properties.DatacenterProperties(
                    name = 'Production datacenter', 
                    description = 'My Production Datacenter', 
                    location = 'us/las', 
                    version = 8, 
                    features = ["SSD"], 
                    sec_auth_protection = True, 
                    cpu_architecture = [
                        openapi_client.models.cpu_architecture_properties.CpuArchitectureProperties(
                            cpu_family = 'INTEL_ICELAKE', 
                            max_cores = 62, 
                            max_ram = 245760, 
                            vendor = 'AuthenticAMD', )
                        ], 
                    ipv6_cidr_block = '2001:db8:b06d:8f00::/56', 
                    default_security_group_id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', ),
        )
        """

    def testDatacenter(self):
        """Test Datacenter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
