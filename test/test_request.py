# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.request import Request

class TestRequest(unittest.TestCase):
    """Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Request:
        """Test Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Request`
        """
        model = Request()
        if include_optional:
            return Request(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = 'datacenter',
                href = '<RESOURCE-URI>',
                metadata = openapi_client.models.request_metadata.RequestMetadata(
                    created_date = '2015-12-04T14:34:09.809Z', 
                    created_by = 'user@example.com', 
                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                    request_status = openapi_client.models.request_status.RequestStatus(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = 'request-status', 
                        href = '<RESOURCE-URI>', 
                        metadata = openapi_client.models.request_status_metadata.RequestStatusMetadata(
                            status = 'QUEUED', 
                            message = '', 
                            etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                            targets = [
                                openapi_client.models.request_target.RequestTarget(
                                    target = openapi_client.models.resource_reference.ResourceReference(
                                        id = '', 
                                        type = 'resource', 
                                        href = '<RESOURCE-URI>', ), 
                                    status = 'QUEUED', )
                                ], ), ), ),
                properties = openapi_client.models.request_properties.RequestProperties(
                    method = '', 
                    headers = {
                        'key' : ''
                        }, 
                    body = '', 
                    url = '', )
            )
        else:
            return Request(
                properties = openapi_client.models.request_properties.RequestProperties(
                    method = '', 
                    headers = {
                        'key' : ''
                        }, 
                    body = '', 
                    url = '', ),
        )
        """

    def testRequest(self):
        """Test Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
