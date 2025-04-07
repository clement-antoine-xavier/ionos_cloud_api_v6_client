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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class S3KeyMetadata(BaseModel):
    """
    S3KeyMetadata
    """ # noqa: E501
    etag: Optional[StrictStr] = Field(default=None, description="Resource's Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an 'ETag response header to requests which don't use 'depth' parameter.")
    created_date: Optional[datetime] = Field(default=None, description="The time when the Object storage key was created.", alias="createdDate")
    created_by: Optional[StrictStr] = Field(default=None, description="Unique name of the identity that created the resource.", alias="createdBy")
    created_by_user_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the user who created the Object storage key.", alias="createdByUserId")
    last_modified_date: Optional[datetime] = Field(default=None, description="The last time the Object storage key was modified.", alias="lastModifiedDate")
    last_modified_by: Optional[StrictStr] = Field(default=None, description="Unique name of the identity that last modified the Object storage key.", alias="lastModifiedBy")
    last_modified_by_user_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the user who last modified the Object storage key.", alias="lastModifiedByUserId")
    __properties: ClassVar[List[str]] = ["etag", "createdDate", "createdBy", "createdByUserId", "lastModifiedDate", "lastModifiedBy", "lastModifiedByUserId"]

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
        """Create an instance of S3KeyMetadata from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "etag",
            "created_date",
            "created_by",
            "created_by_user_id",
            "last_modified_date",
            "last_modified_by",
            "last_modified_by_user_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of S3KeyMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "etag": obj.get("etag"),
            "createdDate": obj.get("createdDate"),
            "createdBy": obj.get("createdBy"),
            "createdByUserId": obj.get("createdByUserId"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "lastModifiedBy": obj.get("lastModifiedBy"),
            "lastModifiedByUserId": obj.get("lastModifiedByUserId")
        })
        return _obj


