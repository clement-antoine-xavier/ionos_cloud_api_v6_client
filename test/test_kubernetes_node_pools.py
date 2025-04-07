# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.kubernetes_node_pools import KubernetesNodePools

class TestKubernetesNodePools(unittest.TestCase):
    """KubernetesNodePools unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KubernetesNodePools:
        """Test KubernetesNodePools
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KubernetesNodePools`
        """
        model = KubernetesNodePools()
        if include_optional:
            return KubernetesNodePools(
                id = '1e072e52-2ed3-492f-b6b6-c6b116907527/nodepools',
                type = 'collection',
                href = 'https://api.ionos.com/cloudapi/v6/k8s/30f8a4f6-6515-4c34-b49d-dea807453b90/nodepools',
                items = [
                    ionos_cloud_api_v6_client.models.kubernetes_node_pool.KubernetesNodePool(
                        id = '1e072e52-2ed3-492f-b6b6-c6b116907527', 
                        type = 'nodepool', 
                        href = 'https://api.ionos.com/cloudapi/v6/k8s/30f8a4f6-6515-4c34-b49d-dea807453b90/nodepools/4735f530-4279-42f3-9562-386143098038', 
                        metadata = ionos_cloud_api_v6_client.models.datacenter_element_metadata.DatacenterElementMetadata(
                            etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                            created_date = '2015-12-04T14:34:09.809Z', 
                            created_by = 'user@example.com', 
                            created_by_user_id = 'user@example.com', 
                            last_modified_date = '2015-12-04T14:34:09.809Z', 
                            last_modified_by = 'user@example.com', 
                            last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                            state = 'AVAILABLE', ), 
                        properties = ionos_cloud_api_v6_client.models.kubernetes_node_pool_properties.KubernetesNodePoolProperties(
                            name = 'K8s-node-pool', 
                            datacenter_id = '1e072e52-2ed3-492f-b6b6-c6b116907521', 
                            node_count = 2, 
                            server_type = 'DedicatedCore', 
                            cpu_family = 'INTEL_ICELAKE', 
                            cores_count = 4, 
                            ram_size = 2048, 
                            availability_zone = 'AUTO', 
                            storage_type = 'HDD', 
                            storage_size = 100, 
                            k8s_version = '1.15.4', 
                            maintenance_window = ionos_cloud_api_v6_client.models.kubernetes_maintenance_window.KubernetesMaintenanceWindow(
                                day_of_the_week = 'Monday', 
                                time = '13:00:00', ), 
                            auto_scaling = ionos_cloud_api_v6_client.models.kubernetes_auto_scaling.KubernetesAutoScaling(
                                min_node_count = 1, 
                                max_node_count = 3, ), 
                            lans = [
                                ionos_cloud_api_v6_client.models.kubernetes_node_pool_lan.KubernetesNodePoolLan(
                                    datacenter_id = '00000000-0000-0000-0000-000000000000', 
                                    id = 3, 
                                    dhcp = True, 
                                    routes = [
                                        ionos_cloud_api_v6_client.models.kubernetes_node_pool_lan_routes.KubernetesNodePoolLanRoutes(
                                            network = '1.2.3.4/24', 
                                            gateway_ip = '10.1.5.16', )
                                        ], )
                                ], 
                            labels = {
                                'key' : ''
                                }, 
                            annotations = {
                                'key' : ''
                                }, 
                            public_ips = ["81.173.1.2","82.231.2.5","92.221.2.4"], 
                            available_upgrade_versions = ["1.16.4","1.17.7"], ), )
                    ]
            )
        else:
            return KubernetesNodePools(
        )
        """

    def testKubernetesNodePools(self):
        """Test KubernetesNodePools"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
