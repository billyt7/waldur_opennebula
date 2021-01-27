import logging
import requests
import pyone

from waldur_opennebula.exceptions import OpenNebulaError

logger = logging.getLogger(__name__)

class OpenNebulaClient:
    """
    OpenNebula vCenter Automation API client.
    See also: http://docs.opennebula.io/5.8/integration/system_interfaces/api.html#actions-for-virtual-machine-management
    """
    one = pyone.OneServer("http://5.254.20.106:2633/RPC2", session="oneadmin:BFGDETio2020")

    #allocate vm, deploy vm on host, action on vm, migrate vm to target host, attach disk to vm, detach disk from vm, attach nic to vm, detach nic from vm, rename vm,
    #create vm snapshot, revert vm to snapshot, delete vm snapshot, info on vm, monitoring vm, 

    def resume_vm(vm_id):
        """
        Power on given virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return one.vm.action('resume', vm_id)

    def stop_vm(vm_id):
        """
        Power off given virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return one.vm.action('suspend', vm_id)

    def list_clusters(self):
        return self._get('vcenter/cluster')

    def get_cluster(self, cluster_id):
        return self._get('vcenter/cluster/{0}'.format(cluster_id))

    def list_datacenters(self):
        return self._get('vcenter/datacenter')

    def list_datastores(self):
        return self._get('vcenter/datastore')

    def list_resource_pools(self):
        return self._get('vcenter/resource-pool')

    def list_networks(self):
        return self._get('vcenter/network')

    def list_folders(self, folder_type=None):
        """
        Returns information about folders in vCenter.
        :param folder_type: Type (DATACENTER, DATASTORE, HOST, NETWORK, VIRTUAL_MACHINE) of the vCenter Server folder.
        :rtype: List[Dict]
        """
        params = {}
        if folder_type:
            params['filter.type'] = folder_type
        return self._get('vcenter/folder', params=params)

    def list_vms(self):
        """
        Get all the VMs from vCenter inventory.
        """
        return self._get('vcenter/vm')

    def get_vm(self, vm_id):
        """
        Returns information about a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._get('vcenter/vm/{}'.format(vm_id))

    def create_vm(self, spec):
        """
        Creates a virtual machine.

        :param spec: new virtual machine specification
        :type spec: dict
        :return: Virtual machine identifier
        :rtype: string
        """
        return self._post('vcenter/vm', json=spec)

    def delete_vm(self, vm_id):
        """
        Deletes a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._delete('vcenter/vm/{}'.format(vm_id))



    def reset_vm(self, vm_id):
        """
        Resets a powered-on virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._post('vcenter/vm/{}/power/reset'.format(vm_id))

    def suspend_vm(self, vm_id):
        """
        Suspends a powered-on virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._post('vcenter/vm/{}/power/suspend'.format(vm_id))

    def get_guest_power(self, vm_id):
        """
        Returns information about the guest operating system power state.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._get('vcenter/vm/{}/guest/power'.format(vm_id))

    def shutdown_guest(self, vm_id):
        """
        Issues a request to the guest operating system asking
        it to perform a clean shutdown of all services.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._post('vcenter/vm/{}/guest/power?action=shutdown'.format(vm_id))

    def reboot_guest(self, vm_id):
        """
        Issues a request to the guest operating system asking it to perform a reboot.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._post('vcenter/vm/{}/guest/power?action=reboot'.format(vm_id))

    def get_cpu(self, vm_id):
        """
        Returns the CPU-related settings of a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._get('vcenter/vm/{}/hardware/cpu'.format(vm_id))

    def update_cpu(self, vm_id, spec):
        """
        Updates the CPU-related settings of a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        :param spec: CPU specification
        :type spec: dict
        """
        return self._patch('vcenter/vm/{}/hardware/cpu'.format(vm_id), json=spec)

    def get_memory(self, vm_id):
        """
        Returns the memory-related settings of a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._get('vcenter/vm/{}/hardware/memory'.format(vm_id))

    def update_memory(self, vm_id, spec):
        """
        Updates the memory-related settings of a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        :param spec: CPU specification
        :type spec: dict
        """
        return self._patch('vcenter/vm/{}/hardware/memory'.format(vm_id), json=spec)

    def create_disk(self, vm_id, spec):
        """
        Adds a virtual disk to the virtual machine

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        :param spec: new virtual disk specification
        :type spec: dict
        """
        return self._post('vcenter/vm/{}/hardware/disk'.format(vm_id), json=spec)

    def get_disk(self, vm_id, disk_id):
        """
        Returns information about a virtual disk.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param disk_id: Virtual disk identifier.
        :type disk_id: string
        """
        return self._get('vcenter/vm/{}/hardware/disk/{}'.format(vm_id, disk_id))

    def delete_disk(self, vm_id, disk_id):
        """
        Removes a virtual disk from the virtual machine.
        This operation does not destroy the VMDK file that backs the virtual disk.
        It only detaches the VMDK file from the virtual machine.
        Once detached, the VMDK file will not be destroyed when the virtual machine
        to which it was associated is deleted.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param disk_id: Virtual disk identifier.
        :type disk_id: string
        """
        return self._delete('vcenter/vm/{}/hardware/disk/{}'.format(vm_id, disk_id))

    def connect_cdrom(self, vm_id, cdrom_id):
        """
        Connects a virtual CD-ROM device of a powered-on virtual machine to its backing.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        :param cdrom_id: Virtual CD-ROM device identifier.
        :type cdrom_id: string
        """
        return self._post(
            'vcenter/vm/{}/hardware/cdrom/{}/connect'.format(vm_id, cdrom_id)
        )

    def disconnect_cdrom(self, vm_id, cdrom_id):
        """
        Disconnects a virtual CD-ROM device of a powered-on virtual machine from its backing.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param cdrom_id: Virtual CD-ROM device identifier.
        :type cdrom_id: string
        """
        return self._post(
            'vcenter/vm/{}/hardware/cdrom/{}/disconnect'.format(vm_id, cdrom_id)
        )

    def create_nic(self, vm_id, network_id):
        """
        Adds a virtual Ethernet adapter to the virtual machine.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param network_id: Identifier of the network that backs the virtual Ethernet adapter.
        :type network_id: string
        """
        spec = {
            'backing': {'network': network_id, 'type': 'DISTRIBUTED_PORTGROUP',},
            'start_connected': True,
        }
        return self._post('vcenter/vm/{}/hardware/ethernet'.format(vm_id), json=spec)

    def delete_nic(self, vm_id, nic_id):
        """
        Removes a virtual Ethernet adapter from the virtual machine.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param nic_id: Virtual Ethernet adapter identifier.
        :type nic_id: string
        """
        return self._delete('vcenter/vm/{}/hardware/ethernet/{}'.format(vm_id, nic_id))

    def list_nics(self, vm_id):
        """
        Returns list of Ethernet adapters by virtual machine ID.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :rtype: List[Dict]
        """
        result = []
        for nic in self.list_nic_ids(vm_id):
            nic_payload = self.get_nic(vm_id, nic['nic'])
            nic_payload['nic'] = nic['nic']
            result.append(nic_payload)
        return result

    def list_nic_ids(self, vm_id):
        """
        Returns list of Ethernet adapter IDs by virtual machine ID.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        """
        return self._get('vcenter/vm/{}/hardware/ethernet'.format(vm_id))

    def get_nic(self, vm_id, nic_id):
        """
        Returns information about a virtual Ethernet adapter.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param nic_id: Virtual Ethernet adapter identifier.
        :type nic_id: string
        """
        return self._get('vcenter/vm/{}/hardware/ethernet/{}'.format(vm_id, nic_id))

    def connect_nic(self, vm_id, nic_id):
        """
        Connects a virtual Ethernet adapter of a powered-on virtual machine to its backing.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param nic_id: Virtual Ethernet adapter identifier.
        :type nic_id: string
        """
        return self._post(
            'vcenter/vm/{}/hardware/ethernet/{}/connect'.format(vm_id, nic_id)
        )

    def disconnect_nic(self, vm_id, nic_id):
        """
        Disconnects a virtual Ethernet adapter of a powered-on virtual machine from its backing.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param nic_id: Virtual Ethernet adapter identifier.
        :type nic_id: string
        """
        return self._post(
            'vcenter/vm/{}/hardware/ethernet/{}/disconnect'.format(vm_id, nic_id)
        )

    def list_libraries(self):
        return self._get('com/opennebula/content/library')

    def list_library_items(self, library_id):
        params = {'library_id': library_id}
        return self._get('com/opennebula/content/library/item', params=params)

    def get_library_item(self, library_item_id):
        return self._get(
            'com/opennebula/content/library/item/id:{}'.format(library_item_id)
        )

    def get_template_library_item(self, library_item_id):
        return self._get('vcenter/vm-template/library-items/{}'.format(library_item_id))

    def list_all_templates(self):
        items = []
        for library_id in self.list_libraries():
            for library_item_id in self.list_library_items(library_id):
                library_item = self.get_library_item(library_item_id)
                if library_item['type'] == 'vm-template':
                    template = self.get_template_library_item(library_item_id)
                    items.append(
                        {'library_item': library_item, 'template': template,}
                    )
        return items

    def deploy_vm_from_template(self, library_item_id, spec):
        """
        Deploys a virtual machine as a copy of the source virtual machine
        template contained in the library item specified by library_item_id.

        :param library_item_id: identifier of the content library item containing the source virtual machine template to be deployed.
        :param spec: deployment specification
        :return: Identifier of the deployed virtual machine.
        :rtype: str
        """
        url = 'vcenter/vm-template/library-items/{}?action=deploy'.format(
            library_item_id
        )
        return self._post(url, json=spec)
