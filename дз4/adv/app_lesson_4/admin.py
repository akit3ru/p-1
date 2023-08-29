from django.contrib import admin
from .models import Advert
from django.utils.html import format_html


class AdvAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'image_img']
    list_filter = ['auction', 'created_at']
    actions = ['auction_false', 'auction_true']

    @admin.action(description='Сделать торг неуместным')
    def auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Сделать торг уместным')
    def auction_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display
    def image_img(self,  obj):
        return format_html('<img src="{}" style="width: 130px; height: 100px"/>'.format(obj.image))

    image_img.short_description = 'image_img'

    fieldsets = (
        ('Общее', {'fields': ('title', 'description', 'image')}),
        ('Финансы', {'fields': ('price', 'auction'), 'classes': ['collapse']}),
    )


admin.site.register(Advert, AdvAdmin)
