# Generated by Django 4.0 on 2021-12-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="article",
            new_name="post",
        ),
        migrations.AlterField(
            model_name="post",
            name="link",
            field=models.CharField(max_length=200),
        ),
    ]
