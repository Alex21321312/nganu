from django.contrib import admin
from .models import Users

# Register your models here.

class AdminModels(admin.ModelAdmin):
    list_display = ("username")

admin.site.register(Users)