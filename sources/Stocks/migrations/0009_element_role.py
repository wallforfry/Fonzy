# Generated by Django 2.1.7 on 2019-02-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0008_marque_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Bon état'), (2, 'Réparable'), (3, 'En réparation'), (4, 'Inconnu')], null=True),
        ),
    ]