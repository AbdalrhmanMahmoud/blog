from django.contrib import admin

# show the Post in admin page
from .models import Post


# customize admin page


class PostModelAdmin(admin.ModelAdmin):
    # itm to display
    list_display = ['title', "updated", "timestamp", "p"]
    # add filter
    list_filter = ["updated", "timestamp"]
    # add search function
    search_fields = ['title', 'content']
    # edit from admin\
    list_editable = ['title']
    list_display_links = ["updated"]

    class Meta:

        model = Post


admin.site.register(Post, PostModelAdmin)
