from django.contrib import admin

from .models import Song, Author


class SongInline(admin.TabularInline):
    model = Song.authors.through


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """Song admin."""

    list_display = ("title", "created_at")
    search_fields = ("title", "authors", "created_at")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Author admin."""

    list_display = ("name", "surname")
    search_fields = ("name",)
    inlines = [
        SongInline,
    ]
