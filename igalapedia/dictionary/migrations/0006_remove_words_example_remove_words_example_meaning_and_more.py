# Generated by Django 5.0.3 on 2024-04-06 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0005_rename_figureofspeech_partofspeech_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='words',
            name='example',
        ),
        migrations.RemoveField(
            model_name='words',
            name='example_meaning',
        ),
        migrations.AddField(
            model_name='words',
            name='igala_meaning',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
