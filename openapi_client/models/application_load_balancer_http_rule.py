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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.application_load_balancer_http_rule_condition import ApplicationLoadBalancerHttpRuleCondition
from typing import Optional, Set
from typing_extensions import Self

class ApplicationLoadBalancerHttpRule(BaseModel):
    """
    ApplicationLoadBalancerHttpRule
    """ # noqa: E501
    name: StrictStr = Field(description="The unique name of the Application Load Balancer HTTP rule.")
    type: StrictStr = Field(description="The HTTP rule type.")
    target_group: Optional[StrictStr] = Field(default=None, description="The ID of the target group; this parameter is mandatory and is valid only for 'FORWARD' actions.", alias="targetGroup")
    drop_query: Optional[StrictBool] = Field(default=None, description="Indicates whether the query part of the URI should be dropped and is valid only for 'REDIRECT' actions. Default value is 'FALSE', the redirect URI does not contain any query parameters.", alias="dropQuery")
    location: Optional[StrictStr] = Field(default=None, description="The location for the redirection; this parameter is mandatory and valid only for 'REDIRECT' actions.")
    status_code: Optional[StrictInt] = Field(default=None, description="The status code is for 'REDIRECT' and 'STATIC' actions only.   If the HTTP rule is 'REDIRECT' the valid values are: 301, 302, 303, 307, 308; default value is '301'.  If the HTTP rule is 'STATIC' the valid values are from the range 200-599; default value is '503'.", alias="statusCode")
    response_message: Optional[StrictStr] = Field(default=None, description="The response message of the request; this parameter is mandatory for 'STATIC' actions.", alias="responseMessage")
    content_type: Optional[StrictStr] = Field(default=None, description="Specifies the content type and is valid only for 'STATIC' actions.", alias="contentType")
    conditions: Optional[List[ApplicationLoadBalancerHttpRuleCondition]] = Field(default=None, description="An array of items in the collection. The action will be executed only if each condition is met; the rule will always be applied if no conditions are set.")
    __properties: ClassVar[List[str]] = ["name", "type", "targetGroup", "dropQuery", "location", "statusCode", "responseMessage", "contentType", "conditions"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['FORWARD', 'STATIC', 'REDIRECT']):
            raise ValueError("must be one of enum values ('FORWARD', 'STATIC', 'REDIRECT')")
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
        """Create an instance of ApplicationLoadBalancerHttpRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationLoadBalancerHttpRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "targetGroup": obj.get("targetGroup"),
            "dropQuery": obj.get("dropQuery"),
            "location": obj.get("location"),
            "statusCode": obj.get("statusCode"),
            "responseMessage": obj.get("responseMessage"),
            "contentType": obj.get("contentType"),
            "conditions": [ApplicationLoadBalancerHttpRuleCondition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None
        })
        return _obj


