from django.contrib import admin

from .models import AuthUser, Follower, SocialLink


# Register your models here.
@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display_links = ['email']
    list_display = ['email']


admin.site.register(Follower)
admin.site.register(SocialLink)