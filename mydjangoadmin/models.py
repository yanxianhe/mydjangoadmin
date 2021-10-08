#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/10/08 10:46:11
@Contact :   xianhe_yan@sina.com
'''

from django.conf import settings
from django.db import models

from django.contrib.auth.models import User

# 公共模型
class Main(models.Model) :
    id = models.AutoField(primary_key=True,verbose_name="自增ID")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    remark = models.CharField(max_length=256,verbose_name="备注")
    class Meta :
        abstract = True

# 出版社
class Press(Main) :
    name = models.CharField(max_length=256,verbose_name="名称")

    def __str__(self) :
        return self.name

    class Meta :
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

# 书籍
class Book(Main) :
    name = models.CharField(max_length=256,verbose_name="名称")
    status = models.CharField(choices=(('0',"可借"),('1',"已借"),('2',"不借")),null=True,max_length=1,verbose_name="状态")
    authors = models.ManyToManyField(to=User,related_name="book_authors",verbose_name="作者")
    press = models.ForeignKey(to=Press,on_delete=models.CASCADE,related_name="book_press",verbose_name="出版社")
    
    def __str__(self) :
        return self.name

    class Meta :
        verbose_name = "书籍"
        verbose_name_plural = verbose_name

