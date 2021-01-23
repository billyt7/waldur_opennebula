from django.contrib import admin
from django.contrib.admin import options
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from django.utils.translation import ugettext_lazy as _

from waldur_core.core.admin import ExecutorAdminAction
from waldur_core.structure import admin as structure_admin
from waldur_opennebula.utils import is_basic_mode

from . import executors, models


class DiskAdmin(structure_admin.ResourceAdmin):
    class Pull(ExecutorAdminAction):
        executor = executors.DiskPullExecutor
        short_description = _('Pull')

        def validate(self, instance):
            if instance.state not in (models.Disk.States.OK, models.Disk.States.ERRED):
                raise ValidationError(_('Disk has to be in OK or ERRED state.'))

    pull = Pull()


class VirtualMachineAdmin(structure_admin.ResourceAdmin):
    class Pull(ExecutorAdminAction):
        executor = executors.VirtualMachinePullExecutor
        short_description = _('Pull')

        def validate(self, instance):
            if instance.state not in (
                models.VirtualMachine.States.OK,
                models.VirtualMachine.States.ERRED,
            ):
                raise ValidationError(
                    _('Virtual machine has to be in OK or ERRED state.')
                )

    pull = Pull()


class CustomerInlineFormset(BaseInlineFormSet):
    service_property_field = None

    def clean(self):
        """
        When basic mode is activated we should require one service property
        (network, cluster and folder) defined per customer
        per shared service setting.
        """
        super(CustomerInlineFormset, self).clean()
        if is_basic_mode():
            enabled_settings = {}
            for form in self.forms:
                cleaned_data = getattr(form, 'cleaned_data', None)

                # Skip empty form
                if not cleaned_data:
                    continue

                # Skip deleted form
                if cleaned_data.get('DELETE'):
                    continue

                # Ensure that the same service settings are not used multiple times
                service_settings = cleaned_data[self.service_property_field].settings
                if service_settings in enabled_settings:
                    raise ValidationError(
                        _(
                            'There should be exactly one property '
                            'assigned to the each service settings.'
                        )
                    )
                else:
                    enabled_settings[service_settings] = True


class CustomerClusterNewInlineFormset(CustomerInlineFormset):
    service_property_field = 'cluster'


class CustomerClusterNewInline(options.TabularInline):
    model = models.CustomerClusterNew
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'Customer OpenNebula clusters'
    formset = CustomerClusterNewInlineFormset


class CustomerNetworkNewInlineFormset(CustomerInlineFormset):
    service_property_field = 'network'


class CustomerNetworkNewInline(options.TabularInline):
    model = models.CustomerNetworkNew
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'Customer OpenNebula networks for new VMs'
    formset = CustomerNetworkNewInlineFormset


class CustomerNetworkNewPairInline(options.TabularInline):
    model = models.CustomerNetworkNewPair
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'Customer OpenNebula networks for existing VMs'


class CustomerDatastoreNewInline(options.TabularInline):
    model = models.CustomerDatastoreNew
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'Customer OpenNebula datastores'


class CustomerFolderNewInlineInlineFormset(CustomerInlineFormset):
    service_property_field = 'folder'


class CustomerFolderNewInline(options.TabularInline):
    model = models.CustomerFolderNew
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'Customer OpenNebula folders'
    formset = CustomerFolderNewInlineInlineFormset


admin.site.register(models.OpenNebulaService, structure_admin.ServiceAdmin)
admin.site.register(
    models.OpenNebulaServiceProjectLink, structure_admin.ServiceProjectLinkAdmin
)
admin.site.register(models.Disk, DiskAdmin)
admin.site.register(models.VirtualMachine, VirtualMachineAdmin)
admin.site.register(models.Template, structure_admin.ServicePropertyAdmin)
admin.site.register(models.Cluster, structure_admin.ServicePropertyAdmin)
admin.site.register(models.Datastore, structure_admin.ServicePropertyAdmin)
admin.site.register(models.Network, structure_admin.ServicePropertyAdmin)
admin.site.register(models.Folder, structure_admin.ServicePropertyAdmin)

structure_admin.CustomerAdmin.inlines += [CustomerClusterNewInline]
structure_admin.CustomerAdmin.inlines += [CustomerNetworkNewInline]
structure_admin.CustomerAdmin.inlines += [CustomerNetworkNewPairInline]
structure_admin.CustomerAdmin.inlines += [CustomerDatastoreNewInline]
structure_admin.CustomerAdmin.inlines += [CustomerFolderNewInline]
