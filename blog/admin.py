from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


from .models import Post, Category, Tag


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'status', 'is_nav', 'created_time']  # 展示的内容
    fields = ('name', 'status', 'is_nav')  # 填写的内容

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')  # 展示的内容
    fields = ('name', 'status')  # 填写的内容

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_time', 'operator')  # 展示的内容
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category_name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True
    fields = (
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}>编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
