# Generated by Django 2.2.6 on 2020-08-05 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dgs', '0004_auto_20200805_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imdgcode',
            name='IMO_class',
            field=models.IntegerField(),
        ),
    ]