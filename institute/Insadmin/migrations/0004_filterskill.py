# Generated by Django 3.1.2 on 2020-11-23 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insadmin', '0003_auto_20201120_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='filterskill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insadmin.skillmodel')),
            ],
        ),
    ]
