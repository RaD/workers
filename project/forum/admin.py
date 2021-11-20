from django.contrib import admin

from . import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    class ForumInline(admin.TabularInline):
        model = models.Forum
        fields = ('title', 'group', 'registered_in')
        readonly_fields = fields
        extra = 0

    list_display = ('title', 'registered_in')
    inlines = [ForumInline, ]


@admin.register(models.Forum)
class ForumAdmin(admin.ModelAdmin):
    class PostInline(admin.TabularInline):
        model = models.Post
        fields = ('_text', 'forum', 'registered_by', 'registered_in')
        readonly_fields = fields
        extra = 0

        def _text(self, item):
            return item

    list_display = ('title', 'group', 'registered_in')
    inlines = [PostInline, ]


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    class ReplyInline(admin.TabularInline):
        model = models.Reply
        fields = ('_text', 'post', 'registered_by', 'registered_in')
        readonly_fields = fields
        extra = 0

        def _text(self, item):
            return item

    list_display = ('_text', 'forum', 'registered_by', 'registered_in')
    inlines = [ReplyInline, ]

    def _text(self, item):
        return item


@admin.register(models.Reply)
class Reply(admin.ModelAdmin):
    list_display = ('_text', 'post', 'registered_by', 'registered_in')

    def _text(self, item):
        return item
