# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.application_load_balancers_api import ApplicationLoadBalancersApi


class TestApplicationLoadBalancersApi(unittest.TestCase):
    """ApplicationLoadBalancersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApplicationLoadBalancersApi()

    def tearDown(self) -> None:
        pass

    def test_datacenters_applicationloadbalancers_delete(self) -> None:
        """Test case for datacenters_applicationloadbalancers_delete

        Delete an Application Load Balancer by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_find_by_application_load_balancer_id(self) -> None:
        """Test case for datacenters_applicationloadbalancers_find_by_application_load_balancer_id

        Get an Application Load Balancer by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_flowlogs_delete(self) -> None:
        """Test case for datacenters_applicationloadbalancers_flowlogs_delete

        Delete an ALB Flow Log by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id(self) -> None:
        """Test case for datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id

        Get an ALB Flow Log by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_flowlogs_get(self) -> None:
        """Test case for datacenters_applicationloadbalancers_flowlogs_get

        Get ALB Flow Logs
        """
        pass

    def test_datacenters_applicationloadbalancers_flowlogs_patch(self) -> None:
        """Test case for datacenters_applicationloadbalancers_flowlogs_patch

        Partially Modify an ALB Flow Log by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_flowlogs_post(self) -> None:
        """Test case for datacenters_applicationloadbalancers_flowlogs_post

        Create an ALB Flow Log
        """
        pass

    def test_datacenters_applicationloadbalancers_flowlogs_put(self) -> None:
        """Test case for datacenters_applicationloadbalancers_flowlogs_put

        Modify an ALB Flow Log by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_forwardingrules_delete(self) -> None:
        """Test case for datacenters_applicationloadbalancers_forwardingrules_delete

        Delete an ALB Forwarding Rule by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id(self) -> None:
        """Test case for datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id

        Get an ALB Forwarding Rule by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_forwardingrules_get(self) -> None:
        """Test case for datacenters_applicationloadbalancers_forwardingrules_get

        Get ALB Forwarding Rules
        """
        pass

    def test_datacenters_applicationloadbalancers_forwardingrules_patch(self) -> None:
        """Test case for datacenters_applicationloadbalancers_forwardingrules_patch

        Partially modify an ALB Forwarding Rule by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_forwardingrules_post(self) -> None:
        """Test case for datacenters_applicationloadbalancers_forwardingrules_post

        Create an ALB Forwarding Rule
        """
        pass

    def test_datacenters_applicationloadbalancers_forwardingrules_put(self) -> None:
        """Test case for datacenters_applicationloadbalancers_forwardingrules_put

        Modify an ALB Forwarding Rule by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_get(self) -> None:
        """Test case for datacenters_applicationloadbalancers_get

        Get Application Load Balancers
        """
        pass

    def test_datacenters_applicationloadbalancers_patch(self) -> None:
        """Test case for datacenters_applicationloadbalancers_patch

        Partially Modify an Application Load Balancer by ID
        """
        pass

    def test_datacenters_applicationloadbalancers_post(self) -> None:
        """Test case for datacenters_applicationloadbalancers_post

        Create an Application Load Balancer
        """
        pass

    def test_datacenters_applicationloadbalancers_put(self) -> None:
        """Test case for datacenters_applicationloadbalancers_put

        Modify an Application Load Balancer by ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
