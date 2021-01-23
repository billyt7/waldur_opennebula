from . import views


def register_in(router):
    router.register(r'opennebula', views.ServiceViewSet, basename='opennebula')
    router.register(r'opennebula-limits', views.LimitViewSet, basename='opennebula-limit')
    router.register(
        r'opennebula-service-project-link',
        views.ServiceProjectLinkViewSet,
        basename='opennebula-spl',
    )
    router.register(
        r'opennebula-virtual-machine',
        views.VirtualMachineViewSet,
        basename='opennebula-virtual-machine',
    )
    router.register(r'opennebula-disks', views.DiskViewSet, basename='opennebula-disk')
    router.register(r'opennebula-ports', views.PortViewSet, basename='opennebula-port')
    router.register(
        r'opennebula-templates', views.TemplateViewSet, basename='opennebula-template'
    )
    router.register(r'opennebula-clusters', views.ClusterViewSet, basename='opennebula-cluster')
    router.register(r'opennebula-networks', views.NetworkViewSet, basename='opennebula-network')
    router.register(
        r'opennebula-datastores', views.DatastoreViewSet, basename='opennebula-datastore'
    )
    router.register(r'opennebula-folders', views.FolderViewSet, basename='opennebula-folder')
