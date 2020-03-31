from django.contrib import admin

from shop.models import item


class Item(admin.ModelAdmin):
    list_display = ['itemName', 'itemDescription']
    model = item

# Register your models here.
# class User(admin.ModelAdmin):
#    list_display = ['firstName','lastName']
#    model= Person

admin.site.register(item,Item)