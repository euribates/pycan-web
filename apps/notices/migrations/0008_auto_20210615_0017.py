# Generated by Django 2.2.24 on 2021-06-14 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0007_auto_20210613_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-send_at'], 'verbose_name': 'Aviso para miembro', 'verbose_name_plural': 'Avisos para miembros'},
        ),
    ]