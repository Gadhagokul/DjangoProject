# Generated by Django 4.2.5 on 2023-09-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='phone',
            field=models.CharField(default=2, max_length=12),
            preserve_default=False,
        ),
    ]