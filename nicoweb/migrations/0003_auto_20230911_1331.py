# Generated by Django 3.2.20 on 2023-09-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicoweb', '0002_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='fara categorie', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='titlle_tag',
            field=models.CharField(default='fara tag', max_length=255),
        ),
    ]
