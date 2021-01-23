from django.apps import AppConfig
from django.db.models import signals


class OpenNebulaConfig(AppConfig):
    name = 'waldur_opennebula'
    verbose_name = 'OpenNebula'
    service_name = 'OpenNebula'

    def ready(self):
        from waldur_core.structure import SupportedServices

        from .backend import OpenNebulaBackend
        from . import handlers, models

        SupportedServices.register_backend(OpenNebulaBackend)

        signals.post_save.connect(
            handlers.update_vm_total_disk_when_disk_is_created_or_updated,
            sender=models.Disk,
            dispatch_uid='waldur_opennebula.handlers.'
            'update_vm_total_disk_when_disk_is_created_or_updated',
        )

        signals.post_delete.connect(
            handlers.update_vm_total_disk_when_disk_is_deleted,
            sender=models.Disk,
            dispatch_uid='waldur_opennebula.handlers.'
            'update_vm_total_disk_when_disk_is_deleted',
        )
