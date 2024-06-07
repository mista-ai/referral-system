from django.contrib import admin
from referral_system.models import ReferralCode, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'referrer')
    search_fields = ('user__username', 'referrer__username')


# Register your models here.
@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'expiration_date', 'is_active')
    list_filter = ('is_active', 'expiration_date')
    search_fields = ('user__username', 'code')
