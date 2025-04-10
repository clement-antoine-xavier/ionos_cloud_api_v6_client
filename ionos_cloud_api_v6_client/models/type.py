# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Type(str, Enum):
    """
    Type
    """

    """
    allowed enum values
    """
    DATACENTER = 'datacenter'
    SERVER = 'server'
    VOLUME = 'volume'
    NIC = 'nic'
    LOADBALANCER = 'loadbalancer'
    LOCATION = 'location'
    FIREWALL_MINUS_RULE = 'firewall-rule'
    FLOW_MINUS_LOG = 'flow-log'
    IMAGE = 'image'
    SNAPSHOT = 'snapshot'
    LAN = 'lan'
    IPBLOCK = 'ipblock'
    PCC = 'pcc'
    CONTRACT = 'contract'
    USER = 'user'
    GROUP = 'group'
    COLLECTION = 'collection'
    RESOURCE = 'resource'
    REQUEST = 'request'
    REQUEST_MINUS_STATUS = 'request-status'
    S3KEY = 's3key'
    BACKUPUNIT = 'backupunit'
    LABEL = 'label'
    K8S = 'k8s'
    NODEPOOL = 'nodepool'
    TEMPLATE = 'template'
    NETWORKLOADBALANCER = 'networkloadbalancer'
    FORWARDING_MINUS_RULE = 'forwarding-rule'
    NATGATEWAY = 'natgateway'
    NATGATEWAY_MINUS_RULE = 'natgateway-rule'
    NODE = 'node'
    APPLICATIONLOADBALANCER = 'applicationloadbalancer'
    TARGET_MINUS_GROUP = 'target-group'
    SECURITY_MINUS_GROUP = 'security-group'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Type from a JSON string"""
        return cls(json.loads(json_str))


