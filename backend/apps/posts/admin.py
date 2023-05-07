from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from posts.models import Post, PostImage
from django.utils.safestring import mark_safe


class PostImageAdmin(admin.TabularInline):
    model = PostImage
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='120' height='90'>")

    get_image.short_description = "Image(pic)"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ("title", "alt", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='90' height='60'>")

    get_image.short_description = "Image(pic)"






# class PostImageAdmin(admin.TabularInline):
#     model = PostImage
#     extra = 1
#     readonly_fields = ("get_image",)

#     # def get_image(self, obj):
#     #     return mark_safe(f"<img src='{obj.image.url}' width='120' height='90'>")

#     # get_image.short_description = "Изображение"


# class PostAdminForms(forms.ModelForm):
#     body = forms.CharField(widget=CKEditorWidget())
#     inlines = [PostImageAdmin]

#     class Meta:
#         model = Post
#         exclude = []


# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForms


# admin.site.register(Post, PostAdmin)
# admin.site.register(PostImage, PostImageAdmin)

