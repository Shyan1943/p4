# Generated by Django 2.2.6 on 2020-08-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]