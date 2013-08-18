from django.contrib import admin
from models import Knot, Link


class LinkInlineAdmin(admin.TabularInline):
    model = Link


class KnotAdmin(admin.ModelAdmin):
    inlines = [LinkInlineAdmin, ]


admin.site.register(Knot, KnotAdmin)
