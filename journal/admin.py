"""admin.py"""

from django.contrib import admin
from journal.models import Tag, Post


class TagAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
