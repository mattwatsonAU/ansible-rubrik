# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class KmipConfigurationDetail(Model):
    """KmipConfigurationDetail.

    :param username:
    :type username: str
    :param server_address:
    :type server_address: str
    :param server_certificate:
    :type server_certificate: str
    :param server_port:
    :type server_port: int
    :param client_certificate:
    :type client_certificate: str
    """

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'server_address': {'key': 'serverAddress', 'type': 'str'},
        'server_certificate': {'key': 'serverCertificate', 'type': 'str'},
        'server_port': {'key': 'serverPort', 'type': 'int'},
        'client_certificate': {'key': 'clientCertificate', 'type': 'str'},
    }

    def __init__(self, username=None, server_address=None, server_certificate=None, server_port=None, client_certificate=None):
        self.username = username
        self.server_address = server_address
        self.server_certificate = server_certificate
        self.server_port = server_port
        self.client_certificate = client_certificate