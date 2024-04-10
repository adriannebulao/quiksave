# Generated by Django 5.0.3 on 2024-04-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('user_address_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'user_profile',
                'managed': False,
            },
        ),
    ]
