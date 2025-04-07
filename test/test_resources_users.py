# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_cloud_api_v6_client.models.resources_users import ResourcesUsers

class TestResourcesUsers(unittest.TestCase):
    """ResourcesUsers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourcesUsers:
        """Test ResourcesUsers
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourcesUsers`
        """
        model = ResourcesUsers()
        if include_optional:
            return ResourcesUsers(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = 'datacenter',
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
                            sec_auth_protection = True, ), 
                        entities = ionos_cloud_api_v6_client.models.resource_entities.ResourceEntities(
                            groups = ionos_cloud_api_v6_client.models.resource_groups.ResourceGroups(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = 'collection', 
                                href = 'https://<API_HOST>/cloudapi/v6/um/groups/30740c22-1def-11e7-aac9-d7a3646ca7fd/resources', 
                                items = [
                                    ionos_cloud_api_v6_client.models.resource.Resource(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = 'group', 
                                        href = 'https://<API_HOST>/cloudapi/v6/um/resources/datacenter/15f67991-0f51-4efc-a8ad-ef1fb31a480c', )
                                    ], ), ), )
                    ]
            )
        else:
            return ResourcesUsers(
        )
        """

    def testResourcesUsers(self):
        """Test ResourcesUsers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
