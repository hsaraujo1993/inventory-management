from django.contrib import admin
from .models import Brand

# Register your models here.


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']