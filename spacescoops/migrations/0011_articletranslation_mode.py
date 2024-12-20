# Generated by Django 3.2.25 on 2024-12-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0010_articletranslation_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletranslation',
            name='mode',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Press Release'), (1, 'Paper')], default=0, help_text='Press release, paper, etc.'),
        ),
    ]