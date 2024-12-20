# Generated by Django 3.2.25 on 2024-12-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0012_auto_20241220_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletranslation',
            name='source_type',
        ),
        migrations.AddField(
            model_name='article',
            name='source_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Press Release'), (1, 'Paper')], default=0, help_text='Press release, paper, etc.', verbose_name='source type'),
        ),
    ]
