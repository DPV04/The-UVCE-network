# Generated by Django 5.0.6 on 2024-06-01 19:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_user_interests'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upload',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='upload',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
