# Generated by Django 4.2.3 on 2023-07-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_user_socials_alter_user_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='educations',
            field=models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='api.education', verbose_name='educations'),
        ),
        migrations.AddField(
            model_name='user',
            name='experiences',
            field=models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='api.experience', verbose_name='experiences'),
        ),
        migrations.AddField(
            model_name='user',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='api.project', verbose_name='projects'),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='api.skill', verbose_name='skills'),
        ),
    ]
