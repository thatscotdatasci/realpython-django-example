from django.contrib import admin

from .models import Post, Category, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # TODO: Customise
    pass


class CategoryAdmin(admin.ModelAdmin):
    # TODO: Customise
    pass


class CommentAdmin(admin.ModelAdmin):
    # TODO: Customise
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
