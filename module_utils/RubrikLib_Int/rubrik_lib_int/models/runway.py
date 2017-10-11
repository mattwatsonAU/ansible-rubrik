# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Runway(Model):
    """Runway.

    :param days:
    :type days: long
    """

    _validation = {
        'days': {'required': True},
    }

    _attribute_map = {
        'days': {'key': 'days', 'type': 'long'},
    }

    def __init__(self, days):
        self.days = days