from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from posts.models import Post, PostImage


class PostAdminForms(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = []


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForms


class PostImageAdminForms(forms.ModelForm):

    class Meta:
        model = PostImage
        exclude = []


class PostImageAdmin(admin.ModelAdmin):
    form = PostImageAdminForms


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)

