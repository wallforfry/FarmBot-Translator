# Generated by Django 2.2.1 on 2019-05-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('original', models.TextField()),
                ('translation', models.TextField()),
                ('translated', models.BooleanField(default=False)),
                ('language', models.ForeignKey(on_delete=models.SET(None), to='app.Language')),
            ],
        ),
    ]