# Generated by Django 3.1 on 2020-05-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]