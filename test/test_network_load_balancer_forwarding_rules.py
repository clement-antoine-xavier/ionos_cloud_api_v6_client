# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.network_load_balancer_forwarding_rules import NetworkLoadBalancerForwardingRules

class TestNetworkLoadBalancerForwardingRules(unittest.TestCase):
    """NetworkLoadBalancerForwardingRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkLoadBalancerForwardingRules:
        """Test NetworkLoadBalancerForwardingRules
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkLoadBalancerForwardingRules`
        """
        model = NetworkLoadBalancerForwardingRules()
        if include_optional:
            return NetworkLoadBalancerForwardingRules(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = 'datacenter',
                href = '<RESOURCE-URI>',
                items = [
                    openapi_client.models.network_load_balancer_forwarding_rule.NetworkLoadBalancerForwardingRule(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'forwarding-rule', 
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
                        properties = openapi_client.models.network_load_balancer_forwarding_rule_properties.NetworkLoadBalancerForwardingRuleProperties(
                            name = 'My Network Load Balancer forwarding rule', 
                            algorithm = 'ROUND_ROBIN', 
                            protocol = 'HTTP', 
                            listener_ip = '81.173.1.2', 
                            listener_port = 8080, 
                            health_check = openapi_client.models.network_load_balancer_forwarding_rule_health_check.NetworkLoadBalancerForwardingRuleHealthCheck(
                                client_timeout = 50, 
                                connect_timeout = 5000, 
                                target_timeout = 50000, 
                                retries = 3, ), 
                            targets = [
                                openapi_client.models.network_load_balancer_forwarding_rule_target.NetworkLoadBalancerForwardingRuleTarget(
                                    ip = '22.231.2.2', 
                                    port = 8080, 
                                    weight = 123, 
                                    proxy_protocol = 'none', )
                                ], ), )
                    ],
                offset = 0,
                limit = 1000,
                links = openapi_client.models.pagination_links.PaginationLinks(
                    prev = '<PREVIOUS-PAGE-URI>', 
                    self = '<THIS-PAGE-URI>', 
                    next = '<NEXT-PAGE-URI>', )
            )
        else:
            return NetworkLoadBalancerForwardingRules(
        )
        """

    def testNetworkLoadBalancerForwardingRules(self):
        """Test NetworkLoadBalancerForwardingRules"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
