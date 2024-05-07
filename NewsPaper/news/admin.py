from django.contrib import admin
from .models import Post, Comment


def reset_rating(modeladmin, request, queryset):
    queryset.update(rating=0)


reset_rating.short_description = 'Обнулить рейтинг'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'dateCreation', 'text', 'rating',)
    list_filter = ('category', 'postType',)
    search_fields = ('title',)
    actions = [reset_rating]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
