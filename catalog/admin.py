from django.contrib import admin
from .models import Category, Perfume

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Kategori adına göre slug'ı otomatik doldurur

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('name', 'description')