# Generated by Django 5.1.4 on 2025-03-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
