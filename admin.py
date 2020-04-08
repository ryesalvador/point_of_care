from django.contrib import admin
from .models import Resident

# Register your models here.
# admin.site.register(Resident)

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')
