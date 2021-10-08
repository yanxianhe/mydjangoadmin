#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/10/08 15:07:38
@Contact :   xianhe_yan@sina.com
'''
from django.contrib import admin
from .models import Book , Press

#admin.site.register(Book)
#admin.site.register(Press)

@admin.register(Book)
class ItemAdmin(admin.ModelAdmin) :

    def author(self,obj) :
        return [user.username for user in obj.authors.all()]
        pass
    author.short_description = "作者"
    def press(self,obj) :
        return obj.press.name
        pass
    press.short_description = "出版社"
    # 搜索
    search_fields = ('id','name')
    # 筛选 过滤
    date_hierarchy = ('create_time')
    list_filter = ('create_time','update_time')
    # 只读属性
    readonly_fields = ('create_time','update_time')
    list_display = ('id','name','press','author','status','create_time','update_time')
    # 超链接
    list_display_links = ('id','name')
    pass

@admin.register(Press)
class ItemAdmin(admin.ModelAdmin) :
    # 搜索
    search_fields = ('id','name')
    # 筛选 过滤
    date_hierarchy = ('create_time')
    list_filter = ('create_time','update_time')
    # 只读属性
    readonly_fields = ('create_time','update_time')

    # 列表显示字段
    list_display = ('id','name','create_time','update_time','remark')
    # 超链接
    list_display_links = ('id','name')
