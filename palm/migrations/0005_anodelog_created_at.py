# Generated by Django 2.0.7 on 2018-09-09 16:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('palm', '0004_anodelog_anode'),
    ]

    operations = [
        migrations.AddField(
            model_name='anodelog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
