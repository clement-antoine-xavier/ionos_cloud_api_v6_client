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
from ionos_cloud_api_v6_client.models.resource_reference import ResourceReference
from typing import Optional, Set
from typing_extensions import Self

class ServerProperties(BaseModel):
    """
    ServerProperties
    """ # noqa: E501
    template_uuid: Optional[StrictStr] = Field(default=None, description="The ID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource.", alias="templateUuid")
    name: Optional[StrictStr] = Field(default=None, description="The name of the  resource.")
    hostname: Optional[StrictStr] = Field(default=None, description="The hostname of the  resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters.")
    cores: Optional[StrictInt] = Field(default=None, description="The total number of cores for the enterprise server.")
    ram: Optional[StrictInt] = Field(default=None, description="The memory size for the enterprise server in MB, such as 2048. Size must be specified in multiples of 256 MB with a minimum of 256 MB; however, if you set ramHotPlug to TRUE then you must use a minimum of 1024 MB. If you set the RAM size more than 240GB, then ramHotPlug will be set to FALSE and can not be set to TRUE unless RAM size not set to less than 240GB.")
    availability_zone: Optional[StrictStr] = Field(default=None, description="The availability zone in which the server should be provisioned.", alias="availabilityZone")
    vm_state: Optional[StrictStr] = Field(default=None, description="Status of the virtual machine.", alias="vmState")
    boot_cdrom: Optional[ResourceReference] = Field(default=None, alias="bootCdrom")
    boot_volume: Optional[ResourceReference] = Field(default=None, alias="bootVolume")
    cpu_family: Optional[StrictStr] = Field(default=None, description="CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource; must not be provided for CUBE and VCPU servers.", alias="cpuFamily")
    type: Optional[StrictStr] = Field(default=None, description="Server type: CUBE, ENTERPRISE or VCPU.")
    placement_group_id: Optional[StrictStr] = Field(default=None, description="The placement group ID that belongs to this server; Requires system privileges, for internal usage only", alias="placementGroupId")
    nic_multi_queue: Optional[StrictBool] = Field(default=False, description="Activate or deactivate the Multi Queue feature on all NICs of this server. This feature is beneficial to  enable when the NICs are experiencing performance issues (e.g. low throughput). Toggling this feature will also initiate a restart of the server. If the specified value is `true`, the feature will  be activated; if it is not specified or set to `false`, the feature will be deactivated. It is not allowed for servers of type Cube.", alias="nicMultiQueue")
    __properties: ClassVar[List[str]] = ["templateUuid", "name", "hostname", "cores", "ram", "availabilityZone", "vmState", "bootCdrom", "bootVolume", "cpuFamily", "type", "placementGroupId", "nicMultiQueue"]

    @field_validator('availability_zone')
    def availability_zone_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AUTO', 'ZONE_1', 'ZONE_2']):
            raise ValueError("must be one of enum values ('AUTO', 'ZONE_1', 'ZONE_2')")
        return value

    @field_validator('vm_state')
    def vm_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NOSTATE', 'RUNNING', 'BLOCKED', 'PAUSED', 'SHUTDOWN', 'SHUTOFF', 'CRASHED', 'SUSPENDED']):
            raise ValueError("must be one of enum values ('NOSTATE', 'RUNNING', 'BLOCKED', 'PAUSED', 'SHUTDOWN', 'SHUTOFF', 'CRASHED', 'SUSPENDED')")
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
        """Create an instance of ServerProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "vm_state",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of boot_cdrom
        if self.boot_cdrom:
            _dict['bootCdrom'] = self.boot_cdrom.to_dict()
        # override the default output from pydantic by calling `to_dict()` of boot_volume
        if self.boot_volume:
            _dict['bootVolume'] = self.boot_volume.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServerProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "templateUuid": obj.get("templateUuid"),
            "name": obj.get("name"),
            "hostname": obj.get("hostname"),
            "cores": obj.get("cores"),
            "ram": obj.get("ram"),
            "availabilityZone": obj.get("availabilityZone"),
            "vmState": obj.get("vmState"),
            "bootCdrom": ResourceReference.from_dict(obj["bootCdrom"]) if obj.get("bootCdrom") is not None else None,
            "bootVolume": ResourceReference.from_dict(obj["bootVolume"]) if obj.get("bootVolume") is not None else None,
            "cpuFamily": obj.get("cpuFamily"),
            "type": obj.get("type"),
            "placementGroupId": obj.get("placementGroupId"),
            "nicMultiQueue": obj.get("nicMultiQueue") if obj.get("nicMultiQueue") is not None else False
        })
        return _obj


