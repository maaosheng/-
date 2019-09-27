# Generated by Django 2.1.5 on 2019-01-17 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('pushier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Pushier')),
            ],
        ),
    ]
