from django.contrib import admin
from .models import Outflow

# Register your models here.


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    fields = ['product', 'quantity', 'description', 'created_at', 'updated_at']
