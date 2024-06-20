from django.contrib import admin
from .models import Pharmacy, Review

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zip_code', 'latitude', 'longitude', 'open_24_hours')
    search_fields = ('name', 'city', 'state')
    list_filter = ('open_24_hours', 'city', 'state')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pharmacy', 'user', 'rating', 'comment', 'created_at')
    search_fields = ('pharmacy__name', 'user__username', 'rating')
    list_filter = ('rating', 'created_at')
