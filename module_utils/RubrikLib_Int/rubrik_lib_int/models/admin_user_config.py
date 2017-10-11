# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdminUserConfig(Model):
    """AdminUserConfig.

    :param id:
    :type id: str
    :param password:
    :type password: str
    :param email_address:
    :type email_address: str
    """

    _validation = {
        'id': {'required': True},
        'password': {'required': True},
        'email_address': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
    }

    def __init__(self, id, password, email_address):
        self.id = id
        self.password = password
        self.email_address = email_address