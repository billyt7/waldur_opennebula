import datetime

import factory
from django.urls import reverse

from waldur_core.structure import models as structure_models
from waldur_core.structure.tests import factories as structure_factories

from .. import models


class OpenNebulaServiceSettingsFactory(structure_factories.ServiceSettingsFactory):
    class Meta:
        model = structure_models.ServiceSettings

    type = 'OpenNebula'
    backend_url = 'https://example.com'
    customer = factory.SubFactory(structure_factories.CustomerFactory)


class OpenNebulaServiceFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.OpenNebulaService

    settings = factory.SubFactory(OpenNebulaServiceSettingsFactory)
    customer = factory.SelfAttribute('settings.customer')

    @classmethod
    def get_url(cls, service=None, action=None):
        if service is None:
            service = OpenNebulaServiceFactory()
        url = 'http://testserver' + reverse(
            'opennebula-detail', kwargs={'uuid': service.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-list')


class OpenNebulaServiceProjectLinkFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.OpenNebulaServiceProjectLink

    service = factory.SubFactory(OpenNebulaServiceFactory)
    project = factory.SubFactory(structure_factories.ProjectFactory)

    @classmethod
    def get_url(cls, spl=None, action=None):
        if spl is None:
            spl = OpenNebulaServiceProjectLinkFactory()
        url = 'http://testserver' + reverse('opennebula-spl-detail', kwargs={'pk': spl.pk})
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-spl-list')


class TemplateFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Template

    created = datetime.datetime.now()
    modified = datetime.datetime.now()
    settings = factory.SubFactory(OpenNebulaServiceSettingsFactory)
    name = factory.Sequence(lambda n: 'template-%s' % n)
    backend_id = factory.Sequence(lambda n: 'template-%s' % n)

    @classmethod
    def get_url(cls, template=None, action=None):
        template = template or TemplateFactory()
        url = 'http://testserver' + reverse(
            'opennebula-template-detail', kwargs={'uuid': template.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-template-list')


class ClusterFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Cluster

    settings = factory.SubFactory(OpenNebulaServiceSettingsFactory)
    name = factory.Sequence(lambda n: 'cluster-%s' % n)
    backend_id = factory.Sequence(lambda n: 'cluster-%s' % n)

    @classmethod
    def get_url(cls, cluster=None, action=None):
        cluster = cluster or ClusterFactory()
        url = 'http://testserver' + reverse(
            'opennebula-cluster-detail', kwargs={'uuid': cluster.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-cluster-list')


class CustomerClusterNewFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.CustomerClusterNew

    customer = factory.SubFactory(structure_factories.CustomerFactory)
    cluster = factory.SubFactory(ClusterFactory)


class VirtualMachineFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.VirtualMachine

    name = factory.Sequence(lambda n: 'vm-%s' % n)
    backend_id = factory.Sequence(lambda n: 'vm-%s' % n)
    service_project_link = factory.SubFactory(OpenNebulaServiceProjectLinkFactory)
    template = factory.SubFactory(TemplateFactory)
    cluster = factory.SubFactory(ClusterFactory)

    state = models.VirtualMachine.States.OK
    runtime_state = models.VirtualMachine.RuntimeStates.POWERED_ON
    cores = factory.fuzzy.FuzzyInteger(1, 8, step=2)
    ram = factory.fuzzy.FuzzyInteger(1024, 10240, step=1024)
    disk = factory.fuzzy.FuzzyInteger(1024, 102400, step=1024)

    @classmethod
    def get_url(cls, instance=None, action=None):
        if instance is None:
            instance = VirtualMachineFactory()
        url = 'http://testserver' + reverse(
            'opennebula-virtual-machine-detail', kwargs={'uuid': instance.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-virtual-machine-list')


class DiskFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Disk

    name = factory.Sequence(lambda n: 'disk-%s' % n)
    backend_id = factory.Sequence(lambda n: 'disk-%s' % n)
    service_project_link = factory.SubFactory(OpenNebulaServiceProjectLinkFactory)

    state = models.Disk.States.OK
    size = factory.fuzzy.FuzzyInteger(1, 8, step=1)
    vm = factory.SubFactory(VirtualMachineFactory)

    @classmethod
    def get_url(cls, disk=None, action=None):
        disk = disk or DiskFactory()
        url = 'http://testserver' + reverse(
            'opennebula-disk-detail', kwargs={'uuid': disk.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-disk-list')


class NetworkFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Network

    settings = factory.SubFactory(OpenNebulaServiceSettingsFactory)
    name = factory.Sequence(lambda n: 'network-%s' % n)
    backend_id = factory.Sequence(lambda n: 'network-%s' % n)
    type = 'STANDARD_PORTGROUP'

    @classmethod
    def get_url(cls, network=None, action=None):
        network = network or NetworkFactory()
        url = 'http://testserver' + reverse(
            'opennebula-network-detail', kwargs={'uuid': network.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-network-list')


class PortFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Port

    name = factory.Sequence(lambda n: 'port-%s' % n)
    backend_id = factory.Sequence(lambda n: 'port-%s' % n)
    service_project_link = factory.SubFactory(OpenNebulaServiceProjectLinkFactory)
    vm = factory.SubFactory(VirtualMachineFactory)
    network = factory.SubFactory(NetworkFactory)

    @classmethod
    def get_url(cls, port=None, action=None):
        port = port or PortFactory()
        url = 'http://testserver' + reverse(
            'opennebula-port-detail', kwargs={'uuid': port.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-port-list')


class CustomerNetworkNewFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.CustomerNetworkNew

    customer = factory.SubFactory(structure_factories.CustomerFactory)
    network = factory.SubFactory(NetworkFactory)


class CustomerNetworkNewPairFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.CustomerNetworkNewPair

    customer = factory.SubFactory(structure_factories.CustomerFactory)
    network = factory.SubFactory(NetworkFactory)


class DatastoreFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Datastore

    settings = factory.SubFactory(OpenNebulaServiceSettingsFactory)
    name = factory.Sequence(lambda n: 'datastore-%s' % n)
    backend_id = factory.Sequence(lambda n: 'datastore-%s' % n)
    type = 'VMFS'
    free_space = 200000

    @classmethod
    def get_url(cls, datastore=None, action=None):
        datastore = datastore or DatastoreFactory()
        url = 'http://testserver' + reverse(
            'opennebula-datastore-detail', kwargs={'uuid': datastore.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-datastore-list')


class CustomerDatastoreNewFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.CustomerDatastoreNew

    customer = factory.SubFactory(structure_factories.CustomerFactory)
    datastore = factory.SubFactory(DatastoreFactory)


class FolderFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Folder

    settings = factory.SubFactory(OpenNebulaServiceSettingsFactory)
    name = factory.Sequence(lambda n: 'folder-%s' % n)
    backend_id = factory.Sequence(lambda n: 'folder-%s' % n)

    @classmethod
    def get_url(cls, folder=None, action=None):
        folder = folder or FolderFactory()
        url = 'http://testserver' + reverse(
            'opennebula-folder-detail', kwargs={'uuid': folder.uuid.hex}
        )
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls):
        return 'http://testserver' + reverse('opennebula-folder-list')


class CustomerFolderNewFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.CustomerFolderNew

    customer = factory.SubFactory(structure_factories.CustomerFactory)
    folder = factory.SubFactory(FolderFactory)
