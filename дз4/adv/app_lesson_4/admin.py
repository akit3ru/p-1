from django.contrib import admin
from .models import Advert


class AdvAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ['auction_false', 'auction_true']

    @admin.action(description='Сделать торг неуместным')
    def auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Сделать торг уместным')
    def auction_true(self, request, queryset):
        queryset.update(auction=True)

    fieldsets = (
        ('Общее', {'fields': ('title', 'description')}),
        ('Финансы', {'fields': ('price', 'auction'), 'classes': ['collapse']}),
    )


admin.site.register(Advert, AdvAdmin)
