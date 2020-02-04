from django.db import models

# Create your models here.


class Storage(models.Model):
    """
    仓库
    """
    warehouse = models.CharField(max_length=20, verbose_name="仓库名称")
    warehouse_area = models.CharField(max_length=20, null=True, blank=True, verbose_name="仓库区域")

    class Meta:
        verbose_name = "仓库信息"
        verbose_name_plural = verbose_name
        constraints = [models.UniqueConstraint(fields=("warehouse", "warehouse_area"), name="unique_area")]

    def __str__(self):
        return f"{self.warehouse}-{self.warehouse_area}"
