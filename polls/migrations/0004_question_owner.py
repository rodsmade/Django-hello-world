# Generated by Django 4.1.9 on 2023-06-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0003_alter_choice_choice_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="owner",
            field=models.CharField(default="naynay", max_length=200),
        ),
    ]
