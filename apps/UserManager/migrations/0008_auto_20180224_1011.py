# Generated by Django 2.0.2 on 2018-02-24 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0007_useraccount_displayname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'default_permissions': (), 'verbose_name': '联系人', 'verbose_name_plural': '联系人'},
        ),
        migrations.AlterModelOptions(
            name='groups',
            options={'default_permissions': (), 'verbose_name': '项目分组', 'verbose_name_plural': '项目分组'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'default_permissions': (), 'verbose_name': '用户角色分类', 'verbose_name_plural': '用户角色分类'},
        ),
        migrations.AlterModelOptions(
            name='useraccount',
            options={'default_permissions': (), 'verbose_name': '用户账户', 'verbose_name_plural': '用户账户'},
        ),
    ]
