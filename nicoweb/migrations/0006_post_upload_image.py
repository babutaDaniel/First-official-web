# Generated by Django 3.2.20 on 2023-09-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicoweb', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
