# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.security_group import SecurityGroup

class TestSecurityGroup(unittest.TestCase):
    """SecurityGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityGroup:
        """Test SecurityGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityGroup`
        """
        model = SecurityGroup()
        if include_optional:
            return SecurityGroup(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = 'datacenter',
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
                        items = [
                            ionos_cloud_api_v6_client.models.firewall_rule.FirewallRule(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = 'firewall-rule', 
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
                                properties = ionos_cloud_api_v6_client.models.firewallrule_properties.FirewallruleProperties(
                                    name = 'My resource', 
                                    protocol = 'TCP', 
                                    source_mac = '00:0a:95:9d:68:16', 
                                    ip_version = 'IPv4', 
                                    source_ip = '22.231.113.64', 
                                    target_ip = '22.231.113.64', 
                                    icmp_code = 0, 
                                    icmp_type = 8, 
                                    port_range_start = 8, 
                                    port_range_end = 8, 
                                    type = 'INGRESS', ), )
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
                        offset = 0, 
                        limit = 1000, ), 
                    servers = ionos_cloud_api_v6_client.models.servers.Servers(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', 
                        offset = 0, 
                        limit = 1000, ), )
            )
        else:
            return SecurityGroup(
                properties = ionos_cloud_api_v6_client.models.security_group_properties.SecurityGroupProperties(
                    name = 'My security group', 
                    description = 'My security group description', ),
        )
        """

    def testSecurityGroup(self):
        """Test SecurityGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
