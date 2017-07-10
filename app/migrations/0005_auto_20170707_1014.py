# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 14:14
from __future__ import unicode_literals

from django.contrib.gis.gdal import GDALRaster, OGRGeometry
from django.contrib.gis.geos import GEOSGeometry
from django.db import migrations
import os

def transfer_existing_orthophoto_extent_values(apps, schema_editor):
    Task = apps.get_model('app', 'Task')

    for t in Task.objects.all():
        print("Checking {}".format(t))
        orthophoto_path = t.assets_path("odm_orthophoto", "odm_orthophoto_4326.tif")
        if os.path.exists(orthophoto_path):
            print("Migrating {}".format(orthophoto_path))

            raster = GDALRaster(orthophoto_path)
            geom = OGRGeometry.from_bbox(raster.extent)
            t.orthophoto_extent = GEOSGeometry(geom.wkt)
            t.save()

            os.remove(orthophoto_path)

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170707_1014'),
    ]

    operations = [
        migrations.RunPython(transfer_existing_orthophoto_extent_values),
    ]
