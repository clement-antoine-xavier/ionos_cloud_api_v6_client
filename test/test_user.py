# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.user import User

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> User:
        """Test User
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = User()
        if include_optional:
            return User(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = 'datacenter',
                href = '<RESOURCE-URI>',
                metadata = ionos_cloud_api_v6_client.models.user_metadata.UserMetadata(
                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                    created_date = '2015-12-04T14:34:09.809Z', 
                    created_by = 'user@example.com', 
                    created_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                    last_modified_by = 'user@example.com', 
                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                    last_login = '2015-12-04T14:34:09.809Z', ),
                properties = ionos_cloud_api_v6_client.models.user_properties.UserProperties(
                    firstname = '', 
                    lastname = '', 
                    email = '', 
                    administrator = True, 
                    force_sec_auth = True, 
                    sec_auth_active = True, 
                    s3_canonical_user_id = '', 
                    active = True, ),
                entities = ionos_cloud_api_v6_client.models.users_entities.UsersEntities(
                    owns = ionos_cloud_api_v6_client.models.resources_users.ResourcesUsers(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'collection', 
                        href = 'https://<API_HOST>/cloudapi/v6/um/users/9b1b4c62-1466-11e7-87d3-d7bb7dac0087/owns', 
                        items = [
                            ionos_cloud_api_v6_client.models.resource.Resource(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = 'group', 
                                href = 'https://<API_HOST>/cloudapi/v6/um/resources/datacenter/15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                metadata = ionos_cloud_api_v6_client.models.datacenter_element_metadata.DatacenterElementMetadata(
                                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                    created_date = '2015-12-04T14:34:09.809Z', 
                                    created_by = 'user@example.com', 
                                    created_by_user_id = 'user@example.com', 
                                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                                    last_modified_by = 'user@example.com', 
                                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                                    state = 'AVAILABLE', ), 
                                properties = ionos_cloud_api_v6_client.models.resource_properties.ResourceProperties(
                                    name = '', 
                                    sec_auth_protection = True, ), )
                            ], ), 
                    groups = ionos_cloud_api_v6_client.models.group_users.GroupUsers(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'group', 
                        href = 'https://<API_HOST>/cloudapi/v6/um/users/9b1b4c62-1466-11e7-87d3-d7bb7dac0087/groups', ), )
            )
        else:
            return User(
                properties = ionos_cloud_api_v6_client.models.user_properties.UserProperties(
                    firstname = '', 
                    lastname = '', 
                    email = '', 
                    administrator = True, 
                    force_sec_auth = True, 
                    sec_auth_active = True, 
                    s3_canonical_user_id = '', 
                    active = True, ),
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
