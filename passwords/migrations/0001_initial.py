# Generated by Django 3.1.1 on 2020-09-23 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capitals', models.BooleanField(default=False)),
                ('numbers', models.BooleanField(default=False)),
                ('symbols', models.BooleanField(default=False)),
                ('min_length', models.IntegerField(default=0)),
                ('max_length', models.IntegerField(default=0)),
                ('other_text', models.CharField(max_length=500)),
                ('votes', models.IntegerField(default=0)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passwords.website')),
            ],
        ),
    ]
