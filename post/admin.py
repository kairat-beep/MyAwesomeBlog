# Register your models here.
from django.contrib import admin

from post.models import PostPage


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "view_count", "TLTR"]
    verbose_name = "Post Visit"
    verbose_name_plural = "Post Visit"


admin.site.register(PostPage, PostAdmin)
