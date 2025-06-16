from django.contrib import admin
from .models import Actor, Movie, Review

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display   = ('id', 'first_name', 'last_name')
    search_fields  = ('first_name', 'last_name')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display   = ('id', 'title', 'average_rating')
    search_fields  = ('title',)
    filter_horizontal = ('actors',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display   = ('id', 'movie', 'rating', 'short_description')
    list_filter    = ('rating',)
    search_fields  = ('movie__title', 'description')

    def short_description(self, obj):
        return (obj.description[:47] + '...') if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Commentaire'
