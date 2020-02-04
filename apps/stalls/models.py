from django.db import models

# Create your models here.


class Stall(models.Model):
    """
    档口信息
    """
    stallname = models.CharField(max_length=30, verbose_name="档口名称")
    address = models.CharField(max_length=50, verbose_name="地址")
    consignee = models.CharField(max_length=20, verbose_name="收货人")
    phone = models.CharField(max_length=20, verbose_name="电话")

    class Meta:
        verbose_name = "档口信息"
        verbose_name_plural = verbose_name
        # 新的设置联合主键的方法
        constraints = [models.UniqueConstraint(fields=("stallname", "address"), name="unique_stall")]

    def __str__(self):
        return f"{self.stallname}-{self.address}-{self.consignee}-{self.phone}"
