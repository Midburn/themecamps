# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camp_name_he', models.CharField(unique=True, max_length=50)),
                ('camp_name_en', models.CharField(unique=True, max_length=50)),
                ('camp_desc_he', models.TextField()),
                ('camp_desc_en', models.TextField()),
                ('camp_status', models.IntegerField(choices=[(-1, b'deleted'), (1, b'open'), (2, b'closed'), (3, b'inactive')])),
                ('is_published', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CampEditor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camp', models.ForeignKey(to='themecampsapp.Camp')),
            ],
        ),
        migrations.CreateModel(
            name='CampLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camp_type', models.IntegerField(choices=[(1, b'food'), (2, b'drinking/bar'), (3, b'music'), (4, b'workshops'), (5, b'art-supporting'), (6, b'other')])),
                ('camp_type_other', models.TextField()),
                ('camp_activity_time', models.CommaSeparatedIntegerField(max_length=64, choices=[(1, b'morning'), (2, b'noon'), (3, b'evening'), (4, b'night')])),
                ('child_friendly', models.BooleanField()),
                ('noise_level', models.IntegerField(choices=[(1, b'quiet'), (2, b'medium'), (3, b'noisy'), (4, b'very noisy')])),
                ('public_activity_area_sqm', models.IntegerField()),
                ('public_activity_area_desc', models.TextField()),
                ('support_art', models.BooleanField()),
                ('location_comments', models.TextField()),
                ('camp_location_street', models.CharField(max_length=100)),
                ('camp_location_street_time', models.CharField(max_length=100)),
                ('camp_location_area', models.IntegerField()),
                ('arriving_at', models.DateTimeField()),
                ('has_construction_team', models.BooleanField()),
                ('has_deconst_team', models.BooleanField()),
                ('has_gifting', models.BooleanField()),
                ('has_leds', models.BooleanField()),
                ('camp', models.OneToOneField(to='themecampsapp.Camp')),
                ('requested_nearby_camps', models.ManyToManyField(related_name='requested_nearby_camps', to='themecampsapp.Camp')),
            ],
        ),
        migrations.CreateModel(
            name='CampMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(choices=[(1, b'not a member'), (2, b'awaiting approval'), (3, b'approved')])),
                ('has_ticket', models.BooleanField()),
                ('early_arrival', models.BooleanField()),
                ('camp', models.ForeignKey(to='themecampsapp.Camp')),
            ],
        ),
        migrations.CreateModel(
            name='CampSafety',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('have_art', models.BooleanField()),
                ('installation_over_2m', models.BooleanField()),
                ('is_gas_2m_from_stove', models.BooleanField()),
                ('is_electricity_not_near_water', models.BooleanField()),
                ('camp', models.OneToOneField(to='themecampsapp.Camp')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(unique=True, max_length=254)),
                ('facebook', models.CharField(max_length=254)),
                ('first_name_he', models.CharField(max_length=50)),
                ('last_name_he', models.CharField(max_length=50)),
                ('first_name_en', models.CharField(max_length=50)),
                ('last_name_en', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_name_he', models.CharField(max_length=50)),
                ('activity_name_en', models.CharField(max_length=50)),
                ('activity_desc_he', models.TextField()),
                ('activity_desc_en', models.TextField()),
                ('activity_datetime', models.DateTimeField()),
                ('activity_type', models.IntegerField(choices=[(1, b'workshop'), (2, b'party'), (3, b'lecture'), (4, b'show'), (5, b'parade/hike'), (6, b'game'), (7, b'movie'), (8, b'other')])),
                ('activity_type_other', models.TextField()),
                ('adult_only', models.BooleanField()),
                ('child_friendly', models.BooleanField()),
                ('owner', models.ForeignKey(to='themecampsapp.Camp')),
            ],
        ),
        migrations.AddField(
            model_name='campmember',
            name='user',
            field=models.ForeignKey(to='themecampsapp.User'),
        ),
        migrations.AddField(
            model_name='campeditor',
            name='user',
            field=models.ForeignKey(to='themecampsapp.User'),
        ),
        migrations.AddField(
            model_name='camp',
            name='main_contact',
            field=models.ForeignKey(related_name='main_contact', to='themecampsapp.User'),
        ),
        migrations.AddField(
            model_name='camp',
            name='moop_contact',
            field=models.ForeignKey(related_name='moop_contact', to='themecampsapp.User'),
        ),
        migrations.AddField(
            model_name='camp',
            name='safety_contact',
            field=models.ForeignKey(related_name='safety_contact', to='themecampsapp.User'),
        ),
    ]
