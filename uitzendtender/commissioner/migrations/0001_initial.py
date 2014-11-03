# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tender', '0005_auto_20141103_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80, verbose_name=b'bedrijfsnaam')),
                ('description', models.TextField(verbose_name=b'omschrijving bedrijf')),
                ('website', models.URLField(max_length=100, verbose_name=b'website')),
                ('changed_by', models.CharField(max_length=254, verbose_name=b'laatste wijziging door')),
                ('branche', models.ManyToManyField(to='tender.Branch')),
            ],
            options={
                'verbose_name_plural': 'bedrijven',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('street', models.CharField(max_length=80, verbose_name=b'straat')),
                ('number', models.CharField(max_length=30, verbose_name=b'huisnummer')),
                ('addition', models.CharField(max_length=30, verbose_name=b'huisnummer toevoeging')),
                ('zipcode', models.CharField(max_length=7, verbose_name=b'postcode')),
                ('city', models.CharField(max_length=60, verbose_name=b'plaatsnaam')),
                ('latitude', models.FloatField(null=True, verbose_name=b'breedtegraad', blank=True)),
                ('longitude', models.FloatField(null=True, verbose_name=b'lengtegraad', blank=True)),
                ('addresstype', models.CharField(default=b'0', max_length=3, choices=[(b'0', b'bezoekadres'), (b'1', b'postadres'), (b'2', b'factuuradres')])),
                ('company', models.ForeignKey(to='commissioner.Company')),
                ('country', models.OneToOneField(to='tender.Country')),
            ],
            options={
                'verbose_name': 'bedrijfsadres',
                'verbose_name_plural': 'bedrijfsadressen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(max_length=3, verbose_name=b'geslacht', choices=[(b'M', b'man'), (b'F', b'vrouw'), (b'U', b'onbekend')])),
                ('firstname', models.CharField(max_length=40, verbose_name=b'voornaam')),
                ('prefix', models.CharField(max_length=40, verbose_name=b'voorvoegsel')),
                ('lastname', models.CharField(max_length=80, verbose_name=b'achternaam')),
                ('phonenumber', models.CharField(max_length=15, verbose_name=b'telefoonnummer')),
                ('approved', models.BooleanField(default=False)),
                ('changed_by', models.CharField(max_length=254, verbose_name=b'laatste wijziging door')),
                ('company', models.ForeignKey(to='commissioner.Company')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
