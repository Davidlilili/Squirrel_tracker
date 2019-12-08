# Generated by Django 2.2.7 on 2019-11-29 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.CharField(help_text='Latitude', max_length=100)),
                ('Longitude', models.CharField(help_text='Longitude', max_length=100)),
                ('Unique_Squirrel_ID', models.CharField(help_text='Unique_Squirrel_ID', max_length=100)),
                ('Shift', models.CharField(help_text='Shift', max_length=100)),
                ('Date', models.CharField(help_text='Date', max_length=100)),
                ('Age', models.CharField(default='', help_text='Age', max_length=100)),
                ('Primary_Fur_Color', models.CharField(default='', help_text='Primary_Fur_Color', max_length=100)),
                ('Location', models.CharField(default='', help_text='Location', max_length=100)),
                ('Specific_Location', models.CharField(default='', help_text='Specific_Location', max_length=100)),
                ('Running', models.CharField(default='', help_text='Running', max_length=100)),
                ('Chasing', models.CharField(default='', help_text='Chasing', max_length=100)),
                ('Climbing', models.CharField(default='', help_text='Climbing', max_length=100)),
                ('Eating', models.CharField(default='', help_text='Eating', max_length=100)),
                ('Foraging', models.CharField(default='', help_text='Foraging', max_length=100)),
                ('Other_Activities', models.CharField(default='', help_text='Other_Activities', max_length=100)),
                ('Kuks', models.CharField(default='', help_text='Kuks', max_length=100)),
                ('Quaas', models.CharField(default='', help_text='Quaas', max_length=100)),
                ('Moans', models.CharField(default='', help_text='Moans', max_length=100)),
                ('Tail_flags', models.CharField(default='', help_text='Tail_flags', max_length=100)),
                ('Tail_twitches', models.CharField(default='', help_text='Tail_twitches', max_length=100)),
                ('Approaches', models.CharField(default='', help_text='Approaches', max_length=100)),
                ('Indifferent', models.CharField(default='', help_text='Indifferent', max_length=100)),
                ('Runs_from', models.CharField(default='', help_text='Runs_from', max_length=100)),
            ],
        ),
    ]
