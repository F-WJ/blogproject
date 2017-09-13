# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 9 / 6
# 文档https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/5
from ..models import Post, Category
from django import template

register = template.Library()


# 文章模板标签
@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模版标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()

