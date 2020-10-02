from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Repair, Stiching, Weaving, Maintainance)

class ViewAdmin(admin.ModelAdmin):
    pass


