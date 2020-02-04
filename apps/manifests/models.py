import uuid
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from apps.stalls.models import Stall
from apps.customers.models import CustomerLabel
from apps.cargos.models import Cargo, CargoBoxType, CargoType

# Create your models here.


class Manifest(models.Model):
    """
    货单流水号
    """
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, verbose_name="流水号")
    created_date = models.DateField(auto_now_add=True, verbose_name="创建日期")
    truck_number = models.CharField(max_length=20, default="未分配车辆", null=True, blank=True, verbose_name="车号")
    trucker = models.CharField(max_length=20, null=True, blank=True, verbose_name="车主")
    trucker_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="电话")
    stall_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="档口联系电话")
    destination = models.CharField(max_length=50, null=True, blank=True, verbose_name="目的地")
    total_quantity = models.IntegerField(null=True, blank=True, verbose_name="总数量")
    total_price = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2, verbose_name="总金额")
    truckage = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2, verbose_name="搬运费")
    deadweight = models.FloatField(null=True, blank=True, verbose_name="载重量")
    weight_unit = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2, verbose_name="超载每吨补充费用")
    overweight = models.FloatField(null=True, blank=True, verbose_name="超载重量")
    overweight_cost = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2, verbose_name="超载费用")
    cartage = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2, verbose_name="车费")
    total = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2, verbose_name="合计费用")
    prepay = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2, verbose_name="预付费用")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "货单流水号"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.created_date}-{self.truck_number}"


class ManifestInfo(models.Model):
    """
    货单详细信息
    """
    uuid = models.ForeignKey(Manifest, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="流水号")
    stallname = models.ForeignKey(Stall, on_delete=models.DO_NOTHING, verbose_name="档口名称")
    cargo = models.OneToOneField(Cargo, on_delete=models.DO_NOTHING, verbose_name="关联库存")
    label = models.ForeignKey(CustomerLabel, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="商标名称")
    type = models.ForeignKey(CargoType, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="货品类型")
    box = models.ForeignKey(CargoBoxType, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="包装类型")
    quantity = models.IntegerField(null=True, blank=True, verbose_name="货物数量")
    unit_price = models.DecimalField(max_digits=5, null=True, blank=True,
                                     default=0.00, decimal_places=2, verbose_name="单价")
    price = models.DecimalField(max_digits=13, null=True, blank=True, default=0.00, decimal_places=2, verbose_name="金额")
    is_output = models.BooleanField(default=False, verbose_name="是否出库")
    is_paycollect = models.BooleanField(default=False, verbose_name="是否回款")
    detail = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "货单详细信息"
        verbose_name_plural = verbose_name
        constraints = [models.UniqueConstraint(fields=("uuid", "stallname", "cargo", "label", "type"),
                                               name="unique_manifest")]

    def __str__(self):
        self.quantity = self.cargo.quantity
        return f"{self.stallname.stallname}-{self.cargo.customerlabel}-{self.cargo.type}-{self.price}"


#
@receiver(pre_save, sender=ManifestInfo)
def pre_save(sender, instance, **kwargs):
    # 保存时将对应的库存设置为已分配
    cargo_obj = Cargo.objects.get(uuid=instance.cargo_id)
    cargo_obj.is_assign = True
    cargo_obj.save()
    # 将库存中的货物类型、商标类型、包装类型、数量赋值到本条数据，并根据单价推断总价
    instance.label_id = cargo_obj.customerlabel_id
    instance.type_id = cargo_obj.type_id
    instance.box_id = cargo_obj.box_id
    instance.quantity = cargo_obj.quantity
    if not type(instance.unit_price) is "int":
        instance.unit_price = 0
    instance.price = instance.quantity * instance.unit_price


# 信号方法，在后台删除对象实例（即表条目）时触发的动作
@receiver(post_delete, sender=ManifestInfo)
def post_delete(sender, instance, **kwargs):
    cargo_obj = Cargo.objects.get(uuid=instance.cargo_id)
    cargo_obj.is_assign = False
    cargo_obj.save()
