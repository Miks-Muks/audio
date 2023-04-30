from django.contrib import admin

# Register your models here.
from .models import Genre, Comment, Track, License, Album, PlayList


admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Track)
admin.site.register(License)
admin.site.register(Album)
admin.site.register(PlayList)