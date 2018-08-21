# Generated by Django 2.1 on 2018-08-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('slug1', models.SlugField(max_length=150)),
                ('slug2', models.SlugField(max_length=150)),
                ('active', models.BooleanField(default=False)),
                ('opened_ticket_sales', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='events/event/')),
            ],
        ),
    ]
