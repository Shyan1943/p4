# Generated by Django 2.2.6 on 2020-08-05 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dgs', '0002_imdgcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='dg',
            name='imdgcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dgs.IMDGCode'),
        ),
        migrations.AlterField(
            model_name='dg',
            name='example',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dg',
            name='prohibited_reason',
            field=models.CharField(max_length=255),
        ),
    ]
