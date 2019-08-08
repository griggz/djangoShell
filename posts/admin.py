from django.contrib import admin
from django.db import models
from .models import Post
from .forms import PostForm
from pagedown.widgets import AdminPagedownWidget


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_display = ["title", "publish", "updated", "timestamp", "id"]
    list_filter = ["timestamp"]
    search_fields = ["title", "content"]
    form = PostForm

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)