# Generated by Django 2.1 on 2018-08-21 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('surname', models.CharField(max_length=220)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=220)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('bio', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='events/talks/speaker/')),
                ('organization', models.CharField(blank=True, max_length=220)),
                ('position', models.CharField(blank=True, max_length=220)),
                ('twitter', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('telegram', models.URLField(blank=True)),
                ('medium', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('in_english', models.BooleanField(default=False)),
                ('keynote', models.BooleanField(default=False)),
                ('duration', models.PositiveSmallIntegerField()),
                ('when', models.DateTimeField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True)),
                ('repo', models.URLField(blank=True)),
                ('slides', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TalkLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('order', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TalkTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('slug', models.SlugField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracks', to='locations.Location')),
            ],
        ),
        migrations.AddField(
            model_name='talk',
            name='level',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='talks', to='talks.TalkLevel'),
        ),
        migrations.AddField(
            model_name='talk',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='talks', to='talks.TalkTag'),
        ),
        migrations.AddField(
            model_name='talk',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='talks', to='talks.Track'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='talk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='speakers', to='talks.Talk'),
        ),
    ]