# Generated by Django 2.0.2 on 2018-04-20 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180420_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_post',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='shop.account'),
        ),
    ]