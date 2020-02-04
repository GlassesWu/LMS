# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# # Create your models here.
#
#
# class UserProfile(AbstractUser):
#     """
#     用户信息
#     """
#     name = models.TextField(verbose_name="姓名")
#     company = models.TextField(primary_key=True, verbose_name="公司")
#     mobile_phone = models.TextField(verbose_name="手机号")
#     email = models.EmailField(verbose_name="邮箱")
#
#     class Meta:
#         verbose_name = "用户"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
