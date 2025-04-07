# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.network_load_balancer import NetworkLoadBalancer

class TestNetworkLoadBalancer(unittest.TestCase):
    """NetworkLoadBalancer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkLoadBalancer:
        """Test NetworkLoadBalancer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkLoadBalancer`
        """
        model = NetworkLoadBalancer()
        if include_optional:
            return NetworkLoadBalancer(
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
                        items = [
                            ionos_cloud_api_v6_client.models.flow_log.FlowLog(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = 'flow-log', 
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
                                properties = ionos_cloud_api_v6_client.models.flow_log_properties.FlowLogProperties(
                                    name = 'My resource', 
                                    action = 'ACCEPTED', 
                                    direction = 'INGRESS', 
                                    bucket = 'bucketName/key', ), )
                            ], 
                        offset = 0, 
                        limit = 1000, 
                        _links = ionos_cloud_api_v6_client.models.pagination_links.PaginationLinks(
                            prev = '<PREVIOUS-PAGE-URI>', 
                            self = '<THIS-PAGE-URI>', 
                            next = '<NEXT-PAGE-URI>', ), ), 
                    forwardingrules = ionos_cloud_api_v6_client.models.network_load_balancer_forwarding_rules.NetworkLoadBalancerForwardingRules(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = '<RESOURCE-URI>', 
                        offset = 0, 
                        limit = 1000, ), )
            )
        else:
            return NetworkLoadBalancer(
                properties = ionos_cloud_api_v6_client.models.network_load_balancer_properties.NetworkLoadBalancerProperties(
                    name = 'My Network Load Balancer', 
                    listener_lan = 1, 
                    ips = ["81.173.1.2","22.231.2.2","22.231.2.3"], 
                    target_lan = 2, 
                    lb_private_ips = ["81.173.1.5/24","22.231.2.5/24"], 
                    central_logging = True, 
                    logging_format = '%{+Q}o %{-Q}ci - - [%trg] %r %ST %B "" "" %cp %ms %ft %b %s %TR %Tw %Tc %Tr %Ta %tsc %ac %fc %bc %sc %rc %sq %bq %CC %CS %hrl %hsl', ),
        )
        """

    def testNetworkLoadBalancer(self):
        """Test NetworkLoadBalancer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
