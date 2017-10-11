# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MssqlDbSlaConflictCheck(Model):
    """MssqlDbSlaConflictCheck.

    :param database_ids: A list of the IDs of the databases being assigned to
     the SLA Domain.
    :type database_ids: list of str
    """

    _validation = {
        'database_ids': {'required': True},
    }

    _attribute_map = {
        'database_ids': {'key': 'databaseIds', 'type': '[str]'},
    }

    def __init__(self, database_ids):
        self.database_ids = database_ids