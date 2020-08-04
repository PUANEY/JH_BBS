from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    stu_code = models.CharField(max_length=20, unique=True, help_text="学号", verbose_name="学号")
    avatar_url = models.URLField(verbose_name="用户头像", help_text="用户头像", default="https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTI81hOdg7FFbxuBRZGAKHLemY6UjF4QFdTtibgc2C165fPFqNnSC2Hbmb3Ow8wkEoEhaOplK2UeKEw/132")
    qq = models.CharField(verbose_name="QQ", help_text="QQ", max_length=20, unique=True)
    github = models.CharField(verbose_name="github", help_text="github", max_length=30)
    telephone = models.CharField(verbose_name="手机号", help_text="手机号", max_length=13)
    is_vip = models.BooleanField(verbose_name="是否是VIP用户", help_text="是否是VIP用户", default=False)
    is_svip = models.BooleanField(verbose_name="是否是SVIP用户", help_text="是否是SVIP用户", default=False)
    jifen = models.IntegerField(verbose_name="积分", help_text="积分", default=0)
    level = models.IntegerField(verbose_name="等级", help_text="等级", default=1)
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female",
                              verbose_name="性别")
    token = models.CharField(max_length=255, verbose_name="令牌", help_text="令牌")
