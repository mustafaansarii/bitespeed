# Generated by Django 5.2.4 on 2025-07-16 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('linkPrecedence', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], max_length=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, null=True)),
                ('linkedId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='identity.contact')),
            ],
        ),
    ]
