from django.contrib import admin
from .models import Poster, Category

class PosterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'sku',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )

admin.site.register(Poster, PosterAdmin)
admin.site.register(Category, CategoryAdmin)