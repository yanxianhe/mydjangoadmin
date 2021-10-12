# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/02/02 19:11:20
@Contact :   xianhe_yan@sina.com
'''
import json
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
from mydjangoadmin import models
from mydjangoadmin.sqlcursor import mysql


@login_required(login_url="/admin/")
def ping(req):
    if req.method == 'GET':
        user = req.user.username
        # 自定义 sql 查询
        sql = f"SELECT last_login from djangoadmin.auth_user where username = '{user}' LIMIT 1;"
        time_login = mysql.sqlcursor.query_db_list(sql)
        # 获取上次登录是时间
        time_login = time_login[0][0].strftime('%Y-%m-%d %H:%M:%S')
        sql_info = {"time_login":time_login}

        #通过 ORM 提供的 objects 查询
        last_login_dict = models.User.objects.filter(username=user).values("last_login")
        info = last_login_dict[0]["last_login"].strftime('%Y-%m-%d %H:%M:%S')
        orm_info = {"time_login":info}

        msg = {"sql_info":sql_info,"orm_info":orm_info}

        con = json.dumps({"status_code": "000000", "msg":msg})
        return HttpResponse(con)