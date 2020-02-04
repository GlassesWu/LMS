from django.contrib import admin
from .models import Cargo, CargoType, CargoBoxType

# Register your models here.

admin.site.register(CargoType)
admin.site.register(CargoBoxType)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):

    exclude = ('uuid',)

    list_display = ['customerlabel', 'type', 'box', 'quantity', 'is_split', 'is_assign', 'created_time', 'updated_time']

    list_filter = ['customerlabel', 'type', 'box', 'quantity', 'is_split', 'is_assign']

    list_editable = ['customerlabel', 'type', 'box', 'quantity', 'is_split', 'is_assign']

    search_fields = ['customerlabel', 'type', 'box', 'quantity', 'is_split', 'is_assign']

    list_display_links = None
