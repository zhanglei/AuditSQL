# Generated by Django 2.0.2 on 2018-02-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0006_auto_20180209_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='displayname',
            field=models.CharField(default='', max_length=128, verbose_name='用户显示名'),
        ),
    ]
