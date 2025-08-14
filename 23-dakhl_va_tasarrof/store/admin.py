from django.contrib import admin
from .models import Product, Category, Company, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['postal_address', 'city']
    list_filter = ['city']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'company', 'price']
    list_filter = ['category', 'company']
    sortable_by = ['price']
    list_display_links = ['id', 'name']


class ProductStackedInline(admin.StackedInline):
    model = Product
    extra = 0

class ProductTabularInline(admin.TabularInline):
    model = Product
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductStackedInline]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [ProductTabularInline]
