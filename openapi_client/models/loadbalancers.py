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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.loadbalancer import Loadbalancer
from openapi_client.models.pagination_links import PaginationLinks
from openapi_client.models.type import Type
from typing import Optional, Set
from typing_extensions import Self

class Loadbalancers(BaseModel):
    """
    Loadbalancers
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The resource's unique identifier.")
    type: Optional[Type] = Field(default=None, description="The type of object that has been created.")
    href: Optional[StrictStr] = Field(default=None, description="URL to the object representation (absolute path).")
    items: Optional[List[Loadbalancer]] = Field(default=None, description="Array of items in the collection.")
    offset: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The offset (if specified in the request).")
    limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The limit (if specified in the request).")
    links: Optional[PaginationLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["id", "type", "href", "items", "offset", "limit", "_links"]

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
        """Create an instance of Loadbalancers from a JSON string"""
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
            "id",
            "href",
            "items",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Loadbalancers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "href": obj.get("href"),
            "items": [Loadbalancer.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "offset": obj.get("offset"),
            "limit": obj.get("limit"),
            "_links": PaginationLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


