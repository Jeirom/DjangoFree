# admin.py
from django.contrib import admin
from .models import Student, Product, Category

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year')
    list_filter = ('year',)
    search_fields = ('first_name', 'last_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)  # фильтрация по категории
    search_fields = ('name', 'description')  # поиск по полям name и description

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
