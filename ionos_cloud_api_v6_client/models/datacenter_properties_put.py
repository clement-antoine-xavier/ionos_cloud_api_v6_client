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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ionos_cloud_api_v6_client.models.cpu_architecture_properties import CpuArchitectureProperties
from typing import Optional, Set
from typing_extensions import Self

class DatacenterPropertiesPut(BaseModel):
    """
    DatacenterPropertiesPut
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the  resource.")
    description: Optional[StrictStr] = Field(default=None, description="A description for the datacenter, such as staging, production.")
    location: StrictStr = Field(description="The physical location where the datacenter will be created. This will be where all of your servers live. Property cannot be modified after datacenter creation (disallowed in update requests).")
    version: Optional[StrictInt] = Field(default=None, description="The version of the data center; incremented with every change.")
    features: Optional[List[StrictStr]] = Field(default=None, description="List of features supported by the location where this data center is provisioned.")
    sec_auth_protection: Optional[StrictBool] = Field(default=None, description="Boolean value representing if the data center requires extra protection, such as two-step verification.", alias="secAuthProtection")
    cpu_architecture: Optional[List[CpuArchitectureProperties]] = Field(default=None, description="Array of features and CPU families available in a location", alias="cpuArchitecture")
    ipv6_cidr_block: Optional[StrictStr] = Field(default=None, description="This value is either 'null' or contains an automatically-assigned /56 IPv6 CIDR block if IPv6 is enabled on this virtual data center. It can neither be changed nor removed.", alias="ipv6CidrBlock")
    default_security_group_id: Optional[StrictStr] = Field(default=None, description="This will become the default security group for the datacenter, replacing the old one if already exists.  This security group must already exists prior to this request. Provide this field only if the `createDefaultSecurityGroup` field is missing. You cannot provide both of them", alias="defaultSecurityGroupId")
    create_default_security_group: Optional[StrictBool] = Field(default=None, description="If this field is set on true and this datacenter has no default security group then a default security group, with predefined rules, will be created for this datacenter. Default value is false.  Provide this field only if the `defaultSecurityGroupId` field is missing. You cannot provide both of them", alias="createDefaultSecurityGroup")
    __properties: ClassVar[List[str]] = ["name", "description", "location", "version", "features", "secAuthProtection", "cpuArchitecture", "ipv6CidrBlock", "defaultSecurityGroupId", "createDefaultSecurityGroup"]

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
        """Create an instance of DatacenterPropertiesPut from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "version",
            "features",
            "cpu_architecture",
            "ipv6_cidr_block",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in cpu_architecture (list)
        _items = []
        if self.cpu_architecture:
            for _item_cpu_architecture in self.cpu_architecture:
                if _item_cpu_architecture:
                    _items.append(_item_cpu_architecture.to_dict())
            _dict['cpuArchitecture'] = _items
        # set to None if ipv6_cidr_block (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6_cidr_block is None and "ipv6_cidr_block" in self.model_fields_set:
            _dict['ipv6CidrBlock'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatacenterPropertiesPut from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "location": obj.get("location"),
            "version": obj.get("version"),
            "features": obj.get("features"),
            "secAuthProtection": obj.get("secAuthProtection"),
            "cpuArchitecture": [CpuArchitectureProperties.from_dict(_item) for _item in obj["cpuArchitecture"]] if obj.get("cpuArchitecture") is not None else None,
            "ipv6CidrBlock": obj.get("ipv6CidrBlock"),
            "defaultSecurityGroupId": obj.get("defaultSecurityGroupId"),
            "createDefaultSecurityGroup": obj.get("createDefaultSecurityGroup")
        })
        return _obj


