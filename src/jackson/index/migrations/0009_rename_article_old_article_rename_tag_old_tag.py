# Generated by Django 5.0.1 on 2024-03-26 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_rename_text_review_en_text_review_es_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='old_Article',
        ),
        migrations.RenameModel(
            old_name='Tag',
            new_name='old_Tag',
        ),
    ]