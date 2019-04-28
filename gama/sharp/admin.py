from django.contrib import admin
from .models import Tools, Sharpen, ListSharpen

class ToolsAdmin(admin.ModelAdmin):
    list_display = ['stock_code', 'internal_description', 'factory_name',
                    'manufacturer', 'created', 'modified']
    search_fields = ['stock_code', 'internal_description']

class ListInlineAdmin(admin.StackedInline):

    model = ListSharpen

class SharpenList(admin.ModelAdmin):
    list_display = ['name_sharpen', 'author', 'created', 'modified']
    search_fields = ['author']
    inlines = [
        ListInlineAdmin  # classe inserida o model Material para ser apresentada junta com o Lesson
    ]


admin.site.register(Tools, ToolsAdmin)
admin.site.register(Sharpen, SharpenList)