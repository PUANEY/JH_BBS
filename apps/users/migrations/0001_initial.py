# Generated by Django 3.0.8 on 2020-08-01 09:20

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('stu_code', models.CharField(help_text='学号', max_length=20, unique=True, verbose_name='学号')),
                ('avatar_url', models.URLField(default='https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTI81hOdg7FFbxuBRZGAKHLemY6UjF4QFdTtibgc2C165fPFqNnSC2Hbmb3Ow8wkEoEhaOplK2UeKEw/132', help_text='用户头像', verbose_name='用户头像')),
                ('qq', models.CharField(help_text='QQ', max_length=20, unique=True, verbose_name='QQ')),
                ('github', models.CharField(help_text='github', max_length=30, verbose_name='github')),
                ('telephone', models.CharField(help_text='手机号', max_length=13, verbose_name='手机号')),
                ('is_vip', models.BooleanField(default=False, help_text='是否是VIP用户', verbose_name='是否是VIP用户')),
                ('is_svip', models.BooleanField(default=False, help_text='是否是SVIP用户', verbose_name='是否是SVIP用户')),
                ('jifen', models.IntegerField(default=0, help_text='积分', verbose_name='积分')),
                ('level', models.IntegerField(default=1, help_text='等级', verbose_name='等级')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别')),
                ('token', models.CharField(help_text='令牌', max_length=50, verbose_name='令牌')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]