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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class VolumeProperties(BaseModel):
    """
    VolumeProperties
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the  resource.")
    type: Optional[StrictStr] = Field(default=None, description="Hardware type of the volume. DAS (Direct Attached Storage) could be used only in a composite call with a Cube server.")
    size: Union[StrictFloat, StrictInt] = Field(description="The size of the volume in GB.")
    availability_zone: Optional[StrictStr] = Field(default=None, description="The availability zone in which the volume should be provisioned. The storage volume will be provisioned on as few physical storage devices as possible, but this cannot be guaranteed upfront. This is uavailable for DAS (Direct Attached Storage), and subject to availability for SSD.", alias="availabilityZone")
    image: Optional[StrictStr] = Field(default=None, description="Image or snapshot ID to be used as template for this volume. MSSQL Enterprise Images can be used only if the feature toggle for MSSQL Enterprise is enabled on the contract.")
    image_password: Optional[StrictStr] = Field(default=None, description="Initial password to be set for installed OS. Works with public images only. Not modifiable, forbidden in update requests. Password rules allows all characters from a-z, A-Z, 0-9.", alias="imagePassword")
    image_alias: Optional[StrictStr] = Field(default=None, description="Image alias of an image to be used as template for this volume. MSSQL Enterprise Images can be used only if the feature toggle for MSSQL Enterprise is enabled on the contract.", alias="imageAlias")
    ssh_keys: Optional[List[StrictStr]] = Field(default=None, description="Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation.", alias="sshKeys")
    bus: Optional[StrictStr] = Field(default=None, description="The bus type for this volume; default is VIRTIO.")
    licence_type: Optional[StrictStr] = Field(default=None, description="OS type for this volume.", alias="licenceType")
    application_type: Optional[StrictStr] = Field(default='UNKNOWN', description="The type of application that is hosted on this resource.  Only public images can have an Application type different than UNKNOWN.", alias="applicationType")
    cpu_hot_plug: Optional[StrictBool] = Field(default=None, description="Hot-plug capable CPU (no reboot required).", alias="cpuHotPlug")
    ram_hot_plug: Optional[StrictBool] = Field(default=None, description="Hot-plug capable RAM (no reboot required).", alias="ramHotPlug")
    nic_hot_plug: Optional[StrictBool] = Field(default=None, description="Hot-plug capable NIC (no reboot required).", alias="nicHotPlug")
    nic_hot_unplug: Optional[StrictBool] = Field(default=None, description="Hot-unplug capable NIC (no reboot required).", alias="nicHotUnplug")
    disc_virtio_hot_plug: Optional[StrictBool] = Field(default=None, description="Hot-plug capable Virt-IO drive (no reboot required).", alias="discVirtioHotPlug")
    disc_virtio_hot_unplug: Optional[StrictBool] = Field(default=None, description="Hot-unplug capable Virt-IO drive (no reboot required). Not supported with Windows VMs.", alias="discVirtioHotUnplug")
    expose_serial: Optional[StrictBool] = Field(default=False, description="If set to `true` will expose the serial id of the disk attached to the server. If set to `false` will not expose the serial id. Some operating systems or software solutions require the serial id to be exposed to work properly. Exposing the serial  can influence licensed software (e.g. Windows) behavior", alias="exposeSerial")
    require_legacy_bios: Optional[StrictBool] = Field(default=True, description="Indicates if the image requires the legacy BIOS for compatibility or specific needs.", alias="requireLegacyBios")
    device_number: Optional[StrictInt] = Field(default=None, description="The Logical Unit Number of the storage volume. Null for volumes, not mounted to a VM.", alias="deviceNumber")
    pci_slot: Optional[StrictInt] = Field(default=None, description="The PCI slot number of the storage volume. Null for volumes, not mounted to a VM.", alias="pciSlot")
    backupunit_id: Optional[StrictStr] = Field(default=None, description="The ID of the backup unit that the user has access to. The property is immutable and is only allowed to be set on creation of a new a volume. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.", alias="backupunitId")
    user_data: Optional[StrictStr] = Field(default=None, description="The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on creation of a new a volume. It is mandatory to provide either 'public image' or 'imageAlias' that has cloud-init compatibility in conjunction with this property.", alias="userData")
    boot_server: Optional[StrictStr] = Field(default=None, description="The UUID of the attached server.", alias="bootServer")
    boot_order: Optional[StrictStr] = Field(default='AUTO', description="Determines whether the volume will be used as a boot volume. Set to `NONE`, the volume will not be used as boot volume. Set to `PRIMARY`, the volume will be used as boot volume and all other volumes must be set to `NONE`. Set to `AUTO` or `null` requires all volumes to be set to `AUTO` or `null`; this will use the legacy behavior, which is to use the volume as a boot volume only if there are no other volumes or cdrom devices.", alias="bootOrder")
    __properties: ClassVar[List[str]] = ["name", "type", "size", "availabilityZone", "image", "imagePassword", "imageAlias", "sshKeys", "bus", "licenceType", "applicationType", "cpuHotPlug", "ramHotPlug", "nicHotPlug", "nicHotUnplug", "discVirtioHotPlug", "discVirtioHotUnplug", "exposeSerial", "requireLegacyBios", "deviceNumber", "pciSlot", "backupunitId", "userData", "bootServer", "bootOrder"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['HDD', 'SSD', 'SSD Standard', 'SSD Premium', 'DAS', 'ISO']):
            raise ValueError("must be one of enum values ('HDD', 'SSD', 'SSD Standard', 'SSD Premium', 'DAS', 'ISO')")
        return value

    @field_validator('availability_zone')
    def availability_zone_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AUTO', 'ZONE_1', 'ZONE_2', 'ZONE_3']):
            raise ValueError("must be one of enum values ('AUTO', 'ZONE_1', 'ZONE_2', 'ZONE_3')")
        return value

    @field_validator('bus')
    def bus_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['VIRTIO', 'IDE', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('VIRTIO', 'IDE', 'UNKNOWN')")
        return value

    @field_validator('boot_order')
    def boot_order_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AUTO', 'NONE', 'PRIMARY']):
            raise ValueError("must be one of enum values ('AUTO', 'NONE', 'PRIMARY')")
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
        """Create an instance of VolumeProperties from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "device_number",
            "pci_slot",
            "boot_server",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if boot_order (nullable) is None
        # and model_fields_set contains the field
        if self.boot_order is None and "boot_order" in self.model_fields_set:
            _dict['bootOrder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VolumeProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "size": obj.get("size"),
            "availabilityZone": obj.get("availabilityZone"),
            "image": obj.get("image"),
            "imagePassword": obj.get("imagePassword"),
            "imageAlias": obj.get("imageAlias"),
            "sshKeys": obj.get("sshKeys"),
            "bus": obj.get("bus"),
            "licenceType": obj.get("licenceType"),
            "applicationType": obj.get("applicationType") if obj.get("applicationType") is not None else 'UNKNOWN',
            "cpuHotPlug": obj.get("cpuHotPlug"),
            "ramHotPlug": obj.get("ramHotPlug"),
            "nicHotPlug": obj.get("nicHotPlug"),
            "nicHotUnplug": obj.get("nicHotUnplug"),
            "discVirtioHotPlug": obj.get("discVirtioHotPlug"),
            "discVirtioHotUnplug": obj.get("discVirtioHotUnplug"),
            "exposeSerial": obj.get("exposeSerial") if obj.get("exposeSerial") is not None else False,
            "requireLegacyBios": obj.get("requireLegacyBios") if obj.get("requireLegacyBios") is not None else True,
            "deviceNumber": obj.get("deviceNumber"),
            "pciSlot": obj.get("pciSlot"),
            "backupunitId": obj.get("backupunitId"),
            "userData": obj.get("userData"),
            "bootServer": obj.get("bootServer"),
            "bootOrder": obj.get("bootOrder") if obj.get("bootOrder") is not None else 'AUTO'
        })
        return _obj


