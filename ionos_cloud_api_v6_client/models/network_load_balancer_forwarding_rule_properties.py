# coding: utf-8

"""
    CLOUD API

     IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ionos_cloud_api_v6_client.models.network_load_balancer_forwarding_rule_health_check import NetworkLoadBalancerForwardingRuleHealthCheck
from ionos_cloud_api_v6_client.models.network_load_balancer_forwarding_rule_target import NetworkLoadBalancerForwardingRuleTarget
from typing import Optional, Set
from typing_extensions import Self

class NetworkLoadBalancerForwardingRuleProperties(BaseModel):
    """
    NetworkLoadBalancerForwardingRuleProperties
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the Network Load Balancer forwarding rule.")
    algorithm: StrictStr = Field(description="Balancing algorithm")
    protocol: StrictStr = Field(description="Balancing protocol")
    listener_ip: StrictStr = Field(description="Listening (inbound) IP.", alias="listenerIp")
    listener_port: StrictInt = Field(description="Listening (inbound) port number; valid range is 1 to 65535.", alias="listenerPort")
    health_check: Optional[NetworkLoadBalancerForwardingRuleHealthCheck] = Field(default=None, alias="healthCheck")
    targets: List[NetworkLoadBalancerForwardingRuleTarget] = Field(description="Array of items in the collection.")
    __properties: ClassVar[List[str]] = ["name", "algorithm", "protocol", "listenerIp", "listenerPort", "healthCheck", "targets"]

    @field_validator('algorithm')
    def algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ROUND_ROBIN', 'LEAST_CONNECTION', 'RANDOM', 'SOURCE_IP']):
            raise ValueError("must be one of enum values ('ROUND_ROBIN', 'LEAST_CONNECTION', 'RANDOM', 'SOURCE_IP')")
        return value

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['HTTP', 'TCP']):
            raise ValueError("must be one of enum values ('HTTP', 'TCP')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NetworkLoadBalancerForwardingRuleProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of health_check
        if self.health_check:
            _dict['healthCheck'] = self.health_check.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item_targets in self.targets:
                if _item_targets:
                    _items.append(_item_targets.to_dict())
            _dict['targets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkLoadBalancerForwardingRuleProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "algorithm": obj.get("algorithm"),
            "protocol": obj.get("protocol"),
            "listenerIp": obj.get("listenerIp"),
            "listenerPort": obj.get("listenerPort"),
            "healthCheck": NetworkLoadBalancerForwardingRuleHealthCheck.from_dict(obj["healthCheck"]) if obj.get("healthCheck") is not None else None,
            "targets": [NetworkLoadBalancerForwardingRuleTarget.from_dict(_item) for _item in obj["targets"]] if obj.get("targets") is not None else None
        })
        return _obj


