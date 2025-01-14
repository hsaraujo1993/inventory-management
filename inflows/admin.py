from django.contrib import admin
from .models import Inflow

# Register your models here.

@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'description', 'created_at', 'updated_at')