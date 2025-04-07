# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.datacenter_element_metadata import DatacenterElementMetadata

class TestDatacenterElementMetadata(unittest.TestCase):
    """DatacenterElementMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatacenterElementMetadata:
        """Test DatacenterElementMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatacenterElementMetadata`
        """
        model = DatacenterElementMetadata()
        if include_optional:
            return DatacenterElementMetadata(
                etag = '45480eb3fbfc31f1d916c1eaa4abdcc3',
                created_date = '2015-12-04T14:34:09.809Z',
                created_by = 'user@example.com',
                created_by_user_id = 'user@example.com',
                last_modified_date = '2015-12-04T14:34:09.809Z',
                last_modified_by = 'user@example.com',
                last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90',
                state = 'AVAILABLE'
            )
        else:
            return DatacenterElementMetadata(
        )
        """

    def testDatacenterElementMetadata(self):
        """Test DatacenterElementMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
