# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_group_post import UserGroupPost

class TestUserGroupPost(unittest.TestCase):
    """UserGroupPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGroupPost:
        """Test UserGroupPost
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGroupPost`
        """
        model = UserGroupPost()
        if include_optional:
            return UserGroupPost(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c'
            )
        else:
            return UserGroupPost(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
        )
        """

    def testUserGroupPost(self):
        """Test UserGroupPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
