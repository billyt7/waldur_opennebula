# Generated by Django 1.11.21 on 2019-07-18 09:28
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_opennebula', '0013_add_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='folder',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='waldur_opennebula.Folder',
            ),
        ),
    ]
