from django.contrib import admin
from .models import FAQ, Specialization
# Register your models here.


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(FAQ, FAQAdmin)
admin.site.register(Specialization, SpecializationAdmin)
