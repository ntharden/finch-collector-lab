# Generated by Django 4.1 on 2022-08-07 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('drink', models.CharField(choices=[('C', 'Coffee'), ('B', 'Beer')], default='C', max_length=1)),
                ('food', models.CharField(choices=[('T', 'Turkey'), ('S', 'Spaghetti')], default='T', max_length=1)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.friend')),
            ],
        ),
    ]
