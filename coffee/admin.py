from django.contrib import admin
from .models import coffee_db

# Register your models here.
class coffee_dbAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name',)
    list_filter = ('price',)

admin.site.register(coffee_db, coffee_dbAdmin)
