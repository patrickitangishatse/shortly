from django.contrib import admin
from . models import Url

# Register your models here.
@admin.register(Url)
class URlAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url')
    search_fields = ('long_url', 'short_url')
    ordering = ('-long_url',)