from django.contrib import admin

# Register your models here.

from .models import TestTask

@admin.register(TestTask)
class TestTaskAdmin(admin.ModelAdmin):
    pass
