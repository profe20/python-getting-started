# Generated by Django 3.0.7 on 2020-07-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_auto_20200704_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main_product'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='main_product'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='main_product'),
        ),
    ]
