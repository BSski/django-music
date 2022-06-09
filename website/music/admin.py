from django.contrib import admin

from .models import Author, Song


class SongInline(admin.TabularInline):
    """
    Enables displaying of many-to-many relations of Author instances in the admin panel.
    """

    model = Song.authors.through


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """View of the Song model in the admin panel."""

    list_display = ("title", "created_at")
    search_fields = ("title", "authors", "created_at")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """View of the Author model in the admin panel."""

    list_display = ("name", "surname")
    search_fields = ("name",)
    inlines = [
        SongInline,
    ]
