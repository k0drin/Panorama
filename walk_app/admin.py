from django.contrib import admin
from .models import Panorama, Marker, Subscriber


class MarkerInline(admin.TabularInline):
    model = Marker
    fk_name = "panorama"
    extra = 1


@admin.register(Panorama)
class PanoramaAdmin(admin.ModelAdmin):
    inlines = [MarkerInline]


@admin.register(Marker)
class MarkerAdmin(admin.ModelAdmin):
    list_display = (
        "panorama",
        "x_coordinate",
        "y_coordinate",
        "tooltip_text",
        "linked_panorama",
    )
    list_filter = ("panorama", "linked_panorama")


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "ip_address")
