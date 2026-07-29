from django.contrib import admin
from django.utils.html import mark_safe
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ('thumbnail', 'name', 'price', 'discount', 'sold_quantity', 'in_stock')
    search_fields = ['name']
    list_filter   = ('origin', 'in_stock')

    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" />')
        return "Chưa có ảnh"

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display   = ('title', 'is_active', 'image')
    list_editable  = ['is_active']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'created_at')
    search_fields = ['title', 'content']
    list_filter   = ('created_at',)