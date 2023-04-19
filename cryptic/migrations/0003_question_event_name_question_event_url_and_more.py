# Generated by Django 4.1 on 2023-04-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptic', '0002_tag_question_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='event_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='event_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='from_event',
            field=models.BooleanField(default=False),
        ),
    ]
