from django.contrib import admin
from .models import Document, Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type', 'price')
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Document)
admin.site.register(Item, ItemAdmin)