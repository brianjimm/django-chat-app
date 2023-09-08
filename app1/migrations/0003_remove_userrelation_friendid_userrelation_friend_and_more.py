# Generated by Django 4.2.5 on 2023-09-07 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_alter_userrelation_friendid_alter_userrelation_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrelation',
            name='friendid',
        ),
        migrations.AddField(
            model_name='userrelation',
            name='friend',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='friend_relations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userrelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_relations', to=settings.AUTH_USER_MODEL),
        ),
    ]
