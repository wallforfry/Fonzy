# Generated by Django 2.1.7 on 2019-02-26 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0009_element_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='role',
            new_name='state',
        ),
    ]