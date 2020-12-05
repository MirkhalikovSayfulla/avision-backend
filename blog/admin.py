from django.contrib.auth.models import User, Group
from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blog.models import (
    BlogNews,
    BlogVideo,
    Comment,
    Tag,
    Advertising,
    Subscribe
)


class BlogNewsAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogNews
        fields = '__all__'


@admin.register(BlogNews)
class BlogNewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'position', 'status']
    list_filter = ['category', 'tag']
    search_fields = ['name']
    list_per_page = 10
    form = BlogNewsAdminForm


@admin.register(BlogVideo)
class BlogVideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'view']
    list_filter = ['tag']
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['name', 'perc']


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.unregister(User)
admin.site.unregister(Group)
