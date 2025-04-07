# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.application_load_balancer_http_rule import ApplicationLoadBalancerHttpRule

class TestApplicationLoadBalancerHttpRule(unittest.TestCase):
    """ApplicationLoadBalancerHttpRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationLoadBalancerHttpRule:
        """Test ApplicationLoadBalancerHttpRule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationLoadBalancerHttpRule`
        """
        model = ApplicationLoadBalancerHttpRule()
        if include_optional:
            return ApplicationLoadBalancerHttpRule(
                name = 'My Application Load Balancer HTTP rule',
                type = 'FORWARD',
                target_group = '96e514d0-73e4-4abd-8fbc-c0f53b79bfae',
                drop_query = True,
                location = 'www.ionos.com',
                status_code = 301,
                response_message = 'Application Down',
                content_type = 'text/html',
                conditions = [
                    openapi_client.models.application_load_balancer_http_rule_condition.ApplicationLoadBalancerHttpRuleCondition(
                        type = 'HEADER', 
                        condition = 'STARTS_WITH', 
                        negate = False, 
                        key = 'forward-at', 
                        value = 'Friday', )
                    ]
            )
        else:
            return ApplicationLoadBalancerHttpRule(
                name = 'My Application Load Balancer HTTP rule',
                type = 'FORWARD',
        )
        """

    def testApplicationLoadBalancerHttpRule(self):
        """Test ApplicationLoadBalancerHttpRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
