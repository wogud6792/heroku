# Generated by Django 2.2.2 on 2019-06-29 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('place', models.CharField(choices=[('서울', '서울'), ('경기', '경기'), ('강원', '강원')], default='서울', max_length=3)),
                ('placetype', models.CharField(choices=[('카페', '카페'), ('식당', '식당'), ('산책', '산책')], default='카페', max_length=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('explain', models.TextField(default='')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('menupicture', models.ImageField(blank=True, upload_to='images/')),
                ('menutext', models.TextField(default='')),
                ('writer', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_contents', models.CharField(max_length=200)),
                ('post_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Blog')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
