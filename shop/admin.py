from django.contrib import admin

from shop.models import item, usage, archive, store


class Item(admin.ModelAdmin):
    list_display = ['itemName', 'itemDescription']
    model = item


class Usage(admin.ModelAdmin):
    list_display = ['usagePerc']
    model=usage

class Store(admin.ModelAdmin):
    list_display = ['store_NAME']
    model=store


class Archive(admin.ModelAdmin):
    list_display = []
    model=archive

# Register your models here.
# class User(admin.ModelAdmin):
#    list_display = ['firstName','lastName']
#    model= Person

admin.site.register(item,Item)
admin.site.register(usage,Usage)
admin.site.register(store,Store)
admin.site.register(archive,Archive)
