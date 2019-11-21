# Generated by Django 2.2.5 on 2019-11-20 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='students',
            name='college',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='user'),
        ),
        migrations.DeleteModel(
            name='college',
        ),
    ]