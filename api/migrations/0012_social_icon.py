# Generated by Django 4.2.3 on 2023-07-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_education_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='icon',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
