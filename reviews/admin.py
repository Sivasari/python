from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'review_text', 'created_at')
    search_fields = ('name', 'review_text')
    list_filter = ('created_at',)

