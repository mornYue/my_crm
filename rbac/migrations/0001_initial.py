# Generated by Django 2.2.1 on 2019-06-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='url地址名称/权限名称')),
                ('url', models.TextField(verbose_name='访问url')),
            ],
            options={
                'verbose_name': 'access Url',
                'verbose_name_plural': 'access Urls',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='角色名')),
                ('urls', models.ManyToManyField(blank=True, null=True, related_name='roles', to='rbac.AccessUrl', verbose_name='可以访问的url列表')),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.UUIDField(help_text='这里使用uuid加密后的密码作为用户密码', verbose_name='密码')),
                ('roles', models.ManyToManyField(blank=True, null=True, related_name='users', to='rbac.Role', verbose_name='用户角色列表')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
