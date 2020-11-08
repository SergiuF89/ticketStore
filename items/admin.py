from django.contrib import admin

from items.models import Item, CategoryItem

admin.site.register(Item)
admin.site.register(CategoryItem)

