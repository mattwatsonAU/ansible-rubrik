# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ArchivalLocationSummary(Model):
    """ArchivalLocationSummary.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param location_type:
    :type location_type: str
    :param is_active:
    :type is_active: bool
    :param ip_address:
    :type ip_address: str
    :param bucket: Bucket name cannot contain whitespace or _\\\\/*?%.:|<> For
     AWS, bucket name also cannot contain capital letters or underscore.
    :type bucket: str
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
        'location_type': {'required': True},
        'is_active': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location_type': {'key': 'locationType', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'bucket': {'key': 'bucket', 'type': 'str'},
    }

    def __init__(self, id, name, location_type, is_active, ip_address=None, bucket=None):
        self.id = id
        self.name = name
        self.location_type = location_type
        self.is_active = is_active
        self.ip_address = ip_address
        self.bucket = bucket