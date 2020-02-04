from django.db import models
import uuid
from ..customers import models as customers
from ..storages import models as storages
# Create your models here.


class CargoType(models.Model):
    """
    货物类型信息
    """
    typeid = models.CharField(max_length=4, verbose_name="货物类型ID")
    typename = models.TextField(null=True, blank=True, verbose_name="货物类型")

    class Meta:
        verbose_name = "货物类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.typeid}-{self.typename}"


class CargoBoxType(models.Model):
    """
    包装类型信息
    """
    typeid = models.CharField(max_length=4, verbose_name="包装类型ID")
    typename = models.TextField(verbose_name="包装类型")

    class Meta:
        verbose_name = "包装类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.typeid}-{self.typename}"


class Cargo(models.Model):
    """
    货物信息
    """
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, verbose_name="流水号")
    type = models.ForeignKey(CargoType, on_delete=models.DO_NOTHING, verbose_name="货品类型")
    box = models.ForeignKey(CargoBoxType, on_delete=models.DO_NOTHING, verbose_name="包装类型")
    quantity = models.IntegerField(verbose_name="货物数量")
    customerlabel = models.ForeignKey(customers.CustomerLabel, on_delete=models.DO_NOTHING, verbose_name="货物商标")
    address = models.ForeignKey(storages.Storage, on_delete=models.DO_NOTHING, verbose_name="存放位置")
    is_split = models.BooleanField(default=False, verbose_name="是否拆分")
    parent_uuid = models.ForeignKey("self", null=True, blank=True, default=None, on_delete=models.DO_NOTHING, verbose_name="归属流水号")
    is_assign = models.BooleanField(default=False, verbose_name="是否分配货单")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="入库时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "货物信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.customerlabel}-{self.type.typename}-{self.box.typename}-{self.quantity}-{str(self.created_time)[:19]}"
