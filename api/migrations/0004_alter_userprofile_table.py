# Generated by Django 5.1.7 on 2025-03-18 09:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_music_artist_alter_artist_table_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="userprofile",
            table="user_profile",
        ),
    ]
