# Generated by Django 2.0.2 on 2018-05-01 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
    ]