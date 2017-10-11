# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineDetail(Model):
    """VirtualMachineDetail.

    :param max_nested_vsphere_snapshots:
    :type max_nested_vsphere_snapshots: int
    :param is_vm_paused: Whether to pause or resume backups/archival for this
     VM
    :type is_vm_paused: bool
    :param configured_sla_domain_id: Assign this VM to the given SLA domain.
    :type configured_sla_domain_id: str
    :param snapshot_consistency_mandate: Consistency level mandated for this
     VM or empty string for none. Possible values include: 'UNKNOWN',
     'INCONSISTENT', 'CRASH_CONSISTENT', 'FILE_SYSTEM_CONSISTENT',
     'VSS_CONSISTENT', 'APP_CONSISTENT'
    :type snapshot_consistency_mandate: str or :class:`enum
     <rubriklib.models.enum>`
    :param pre_backup_script:
    :type pre_backup_script: :class:`VirtualMachineScriptDetail
     <rubriklib.models.VirtualMachineScriptDetail>`
    :param post_snap_script:
    :type post_snap_script: :class:`VirtualMachineScriptDetail
     <rubriklib.models.VirtualMachineScriptDetail>`
    :param post_backup_script:
    :type post_backup_script: :class:`VirtualMachineScriptDetail
     <rubriklib.models.VirtualMachineScriptDetail>`
    :param is_array_integration_enabled: User setting to dictate whether to
     use storage array snaphots for ingest. This setting only makes sense for
     VMs where array based ingest is possible.
    :type is_array_integration_enabled: bool
    :param cloud_instantiation_spec: Cloud instantiation specification for the
     selected virtual machine.
    :type cloud_instantiation_spec: :class:`CloudInstantiationSpec
     <rubriklib.models.CloudInstantiationSpec>`
    :param moid:
    :type moid: str
    :param vcenter_id:
    :type vcenter_id: str
    :param host_name:
    :type host_name: str
    :param host_id:
    :type host_id: str
    :param cluster_name:
    :type cluster_name: str
    :param power_status: The power status of VM(ON,OFF,SLEEP etc.)
    :type power_status: str
    :param protection_date:
    :type protection_date: datetime
    :param ip_address:
    :type ip_address: str
    :param tools_installed:
    :type tools_installed: bool
    :param is_replication_enabled:
    :type is_replication_enabled: bool
    :param folder_path: Brief info of all the objects in the folder path to
     this VM
    :type folder_path: list of :class:`VmPathPoint
     <rubriklib.models.VmPathPoint>`
    :param infra_path: Brief info of all the objects in the infrastructure
     path to this VM
    :type infra_path: list of :class:`VmPathPoint
     <rubriklib.models.VmPathPoint>`
    :param vmware_tools_installed:
    :type vmware_tools_installed: bool
    :param is_relic:
    :type is_relic: bool
    :param guest_credential_authorization_status: Status of authentication
     with a specific virtual machine using guest credentials. Possible values
     are: SUCCESSFUL, PENDING, or FAILED.
    :type guest_credential_authorization_status: str
    :param effective_sla_domain:
    :type effective_sla_domain: :class:`SlaDomainSummary
     <rubriklib.models.SlaDomainSummary>`
    :param blackout_window_status:
    :type blackout_window_status: :class:`BlackoutWindowStatus
     <rubriklib.models.BlackoutWindowStatus>`
    :param blackout_windows:
    :type blackout_windows: :class:`BlackoutWindows
     <rubriklib.models.BlackoutWindows>`
    :param current_host:
    :type current_host: :class:`VmwareHostSummary
     <rubriklib.models.VmwareHostSummary>`
    :param virtual_disk_ids:
    :type virtual_disk_ids: list of str
    :param snapshots:
    :type snapshots: list of :class:`VmSnapshotSummary
     <rubriklib.models.VmSnapshotSummary>`
    :param snapshot_count:
    :type snapshot_count: int
    :param physical_storage:
    :type physical_storage: long
    :param guest_os_name:
    :type guest_os_name: str
    :param is_array_integration_possible: Whether it is possible to ingest
     using storage array snapshots for this VM. Array based ingest is possible
     if all of a VM's disks are located on a datastore backed by a configured
     storage array.
    :type is_array_integration_possible: bool
    :param guest_credential:
    :type guest_credential: :class:`BaseGuestCredentialDetail
     <rubriklib.models.BaseGuestCredentialDetail>`
    :param is_agent_registered: Whether the agent is installed and Rubrik
     service is registered.
    :type is_agent_registered: bool
    """

    _attribute_map = {
        'max_nested_vsphere_snapshots': {'key': 'maxNestedVsphereSnapshots', 'type': 'int'},
        'is_vm_paused': {'key': 'isVmPaused', 'type': 'bool'},
        'configured_sla_domain_id': {'key': 'configuredSlaDomainId', 'type': 'str'},
        'snapshot_consistency_mandate': {'key': 'snapshotConsistencyMandate', 'type': 'str'},
        'pre_backup_script': {'key': 'preBackupScript', 'type': 'VirtualMachineScriptDetail'},
        'post_snap_script': {'key': 'postSnapScript', 'type': 'VirtualMachineScriptDetail'},
        'post_backup_script': {'key': 'postBackupScript', 'type': 'VirtualMachineScriptDetail'},
        'is_array_integration_enabled': {'key': 'isArrayIntegrationEnabled', 'type': 'bool'},
        'cloud_instantiation_spec': {'key': 'cloudInstantiationSpec', 'type': 'CloudInstantiationSpec'},
        'moid': {'key': 'moid', 'type': 'str'},
        'vcenter_id': {'key': 'vcenterId', 'type': 'str'},
        'host_name': {'key': 'hostName', 'type': 'str'},
        'host_id': {'key': 'hostId', 'type': 'str'},
        'cluster_name': {'key': 'clusterName', 'type': 'str'},
        'power_status': {'key': 'powerStatus', 'type': 'str'},
        'protection_date': {'key': 'protectionDate', 'type': 'iso-8601'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'tools_installed': {'key': 'toolsInstalled', 'type': 'bool'},
        'is_replication_enabled': {'key': 'isReplicationEnabled', 'type': 'bool'},
        'folder_path': {'key': 'folderPath', 'type': '[VmPathPoint]'},
        'infra_path': {'key': 'infraPath', 'type': '[VmPathPoint]'},
        'vmware_tools_installed': {'key': 'vmwareToolsInstalled', 'type': 'bool'},
        'is_relic': {'key': 'isRelic', 'type': 'bool'},
        'guest_credential_authorization_status': {'key': 'guestCredentialAuthorizationStatus', 'type': 'str'},
        'effective_sla_domain': {'key': 'effectiveSlaDomain', 'type': 'SlaDomainSummary'},
        'blackout_window_status': {'key': 'blackoutWindowStatus', 'type': 'BlackoutWindowStatus'},
        'blackout_windows': {'key': 'blackoutWindows', 'type': 'BlackoutWindows'},
        'current_host': {'key': 'currentHost', 'type': 'VmwareHostSummary'},
        'virtual_disk_ids': {'key': 'virtualDiskIds', 'type': '[str]'},
        'snapshots': {'key': 'snapshots', 'type': '[VmSnapshotSummary]'},
        'snapshot_count': {'key': 'snapshotCount', 'type': 'int'},
        'physical_storage': {'key': 'physicalStorage', 'type': 'long'},
        'guest_os_name': {'key': 'guestOsName', 'type': 'str'},
        'is_array_integration_possible': {'key': 'isArrayIntegrationPossible', 'type': 'bool'},
        'guest_credential': {'key': 'guestCredential', 'type': 'BaseGuestCredentialDetail'},
        'is_agent_registered': {'key': 'isAgentRegistered', 'type': 'bool'},
    }

    def __init__(self, max_nested_vsphere_snapshots=None, is_vm_paused=None, configured_sla_domain_id=None, snapshot_consistency_mandate=None, pre_backup_script=None, post_snap_script=None, post_backup_script=None, is_array_integration_enabled=None, cloud_instantiation_spec=None, moid=None, vcenter_id=None, host_name=None, host_id=None, cluster_name=None, power_status=None, protection_date=None, ip_address=None, tools_installed=None, is_replication_enabled=None, folder_path=None, infra_path=None, vmware_tools_installed=None, is_relic=None, guest_credential_authorization_status=None, effective_sla_domain=None, blackout_window_status=None, blackout_windows=None, current_host=None, virtual_disk_ids=None, snapshots=None, snapshot_count=None, physical_storage=None, guest_os_name=None, is_array_integration_possible=None, guest_credential=None, is_agent_registered=None):
        self.max_nested_vsphere_snapshots = max_nested_vsphere_snapshots
        self.is_vm_paused = is_vm_paused
        self.configured_sla_domain_id = configured_sla_domain_id
        self.snapshot_consistency_mandate = snapshot_consistency_mandate
        self.pre_backup_script = pre_backup_script
        self.post_snap_script = post_snap_script
        self.post_backup_script = post_backup_script
        self.is_array_integration_enabled = is_array_integration_enabled
        self.cloud_instantiation_spec = cloud_instantiation_spec
        self.moid = moid
        self.vcenter_id = vcenter_id
        self.host_name = host_name
        self.host_id = host_id
        self.cluster_name = cluster_name
        self.power_status = power_status
        self.protection_date = protection_date
        self.ip_address = ip_address
        self.tools_installed = tools_installed
        self.is_replication_enabled = is_replication_enabled
        self.folder_path = folder_path
        self.infra_path = infra_path
        self.vmware_tools_installed = vmware_tools_installed
        self.is_relic = is_relic
        self.guest_credential_authorization_status = guest_credential_authorization_status
        self.effective_sla_domain = effective_sla_domain
        self.blackout_window_status = blackout_window_status
        self.blackout_windows = blackout_windows
        self.current_host = current_host
        self.virtual_disk_ids = virtual_disk_ids
        self.snapshots = snapshots
        self.snapshot_count = snapshot_count
        self.physical_storage = physical_storage
        self.guest_os_name = guest_os_name
        self.is_array_integration_possible = is_array_integration_possible
        self.guest_credential = guest_credential
        self.is_agent_registered = is_agent_registered