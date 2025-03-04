# Generated by Django 5.1.5 on 2025-01-18 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='Default Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.blogs'),
        ),
    ]
