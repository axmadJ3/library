# Generated by Django 5.0.4 on 2024-04-30 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_book_on_trend"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="genre",
            new_name="genres",
        ),
    ]
