# listings/admin.py
from django.contrib import admin
from .models import Listing, Booking, Review

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "price", "user", "created_at")
    list_filter = ("location", "created_at")
    search_fields = ("title", "description", "location", "user__email")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("booking_id", "listing", "user", "status", "start_date", "end_date", "total_price", "created_at")
    list_filter = ("status", "start_date", "end_date", "created_at")
    search_fields = ("listing__title", "user__email", "booking_id")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("review_id", "listing", "user", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("listing__title", "user__email", "review_id")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
