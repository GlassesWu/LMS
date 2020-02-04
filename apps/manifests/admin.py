from django.contrib import admin
from .models import Manifest, ManifestInfo
from ..cargos.models import Cargo

# Register your models here.


@admin.register(Manifest)
class ManifestAdmin(admin.ModelAdmin):

    # 创建/编辑的时候不显示的字段
    exclude = ('uuid',)
    # 管理界面显示列标题
    list_display = ['created_date', 'truck_number', 'trucker', 'trucker_phone', 'stall_phone', 'destination',
                    'total_quantity', 'total_price', 'truckage', 'deadweight', 'weight_unit', 'overweight',
                    'overweight_cost', 'cartage', 'total', 'prepay', 'created_time', 'updated_time']
    # 数据筛选字段
    list_filter = ['created_date']
    # 数据搜索字段
    search_fields = ['created_date', 'truck_number', 'trucker', 'trucker_phone']
    # 可编辑字段，Ajax无需刷新界面
    list_editable = ['truck_number', 'trucker', 'trucker_phone', 'stall_phone', 'destination',
                     'total_quantity', 'total_price', 'truckage', 'deadweight', 'weight_unit', 'overweight',
                     'overweight_cost', 'cartage', 'total', 'prepay']


@admin.register(ManifestInfo)
class ManifestInfoAdmin(admin.ModelAdmin):

    # 创建和修改时对外键的筛选
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'cargo':  # 外键字段
            kwargs["queryset"] = Cargo.objects.filter(is_assign=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # 重写后台admin在创建和修改后保存的动作,这个只对admin的操作生效，API的还是需要使用信号方法
    def save_model(self, request, obj, form, change):
        obj.label_id = obj.cargo.customerlabel_id
        obj.type_id = obj.cargo.type_id
        obj.box_id = obj.cargo.box_id
        obj.quantity = obj.cargo.quantity
        print(type(obj.unit_price))
        if not type(obj.unit_price) is "int":
            obj.unit_price = 0
        obj.price = obj.quantity * obj.unit_price

        # 保存时将仓库单标记为已分配
        cargo_obj = Cargo.objects.get(uuid=obj.cargo.pk.hex)
        cargo_obj.is_assign = True
        cargo_obj.save()

        super().save_model(request, obj, form, change)

    # 创建/编辑的时候不显示的字段
    exclude = ('label', 'type', 'box', 'quantity', 'price', 'is_output', 'is_paycollect',)
    list_display = ['uuid', 'stallname', 'cargo', 'label', 'type', 'box', 'quantity', 'unit_price', 'price',
                    'is_output', 'is_paycollect', 'created_time', 'updated_time', 'detail']
    # 可筛选的字段
    list_filter = ['uuid']
    # search_fields = ['uuid']
    # 可编辑的字段
    list_editable = ['uuid', 'stallname', 'unit_price', 'detail']
    # 因为uuid设置成了可编辑，所以要把跳转的链接换成别的字段或者None
    list_display_links = None
    # 外键字段设置搜索帮助样式（默认为下拉框），有个bug，这里用过的字段在formfield_for_foreignkey中会不生效
    raw_id_fields = ('uuid', 'stallname',)
    # raw_id_fields = ('uuid', 'stallname', 'cargo',)
