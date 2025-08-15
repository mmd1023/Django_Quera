from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'is_active']
    list_display_links = ['id', 'name']

    list_editable = ['is_active']
    
    fieldsets = (
        ('Identification', {
            'fields': ('name', 'price', 'is_active')
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('category', 'company')
        }),
    )

    actions = ['make_inactive']
    @admin.action(description='Make inactive')
    def make_inactive(self, request, queryset):
        updated = queryset.update(is_active = False)
        self.message_user(request, f"{updated} {ngettext('product', 'products', updated)} inactivated", messages.SUCCESS)