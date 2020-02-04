from django.db import models

# Create your models here.


class Customer(models.Model):
    """
    客户基本信息
    """
    name = models.CharField(max_length=20, verbose_name="客户姓名")
    mobile_phone = models.CharField(max_length=20, verbose_name="客户电话")

    class Meta:
        verbose_name = "客户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CustomerLabel(models.Model):
    """
    客户商标
    """
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, verbose_name="客户")
    labelname = models.TextField(verbose_name="商标名称")
    image = models.BinaryField(verbose_name="照片")

    class Meta:
        verbose_name = "客户商标"
        verbose_name_plural = verbose_name
        constraints = [models.UniqueConstraint(fields=("customer", "labelname"), name="unique_customerlabel")]

    def __str__(self):
        return f"{self.customer}-{self.labelname}"
