# Generated by Django 4.0.4 on 2022-04-30 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='question_text',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='interface',
            name='question_text',
            field=models.CharField(default='teste', max_length=200),
        ),
    ]
