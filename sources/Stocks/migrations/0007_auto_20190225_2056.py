# Generated by Django 2.1.7 on 2019-02-25 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0006_auto_20190225_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
            ],
        ),
        migrations.AddField(
            model_name='element',
            name='model',
            field=models.CharField(blank=True, max_length=255, verbose_name='Modèle'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='element',
            name='marque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Stocks.Marque', verbose_name='Marque'),
        ),
    ]
