# Generated by Django 2.2.7 on 2019-12-02 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0002_auto_20191130_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='id',
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Unique_Squirrel_ID',
            field=models.CharField(default='', help_text='Unique_Squirrel_ID', max_length=100, primary_key=True, serialize=False),
        ),
    ]
