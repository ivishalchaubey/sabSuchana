# Generated by Django 3.2.8 on 2021-10-31 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspostmodel',
            name='news_discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newspostmodel',
            name='sub_title',
            field=models.CharField(max_length=250),
        ),
    ]
