# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/02/02 19:11:20
@Contact :   xianhe_yan@sina.com
'''
import json
import logging

from django import template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
from mydjangoadmin.sqlcursor import mysql

@login_required
def ping(req):
    if req.method == 'GET':
        user = req.user.username
        sql = f"SELECT last_login from djangoadmin.auth_user where username = '{user}' LIMIT 1;"
        time_login = mysql.sqlcursor.query_db_list(sql)
        # 获取上次登录是时间
        time_login = time_login[0][0].strftime('%Y-%m-%d %H:%M:%S')
        con = json.dumps({"status_code": "000000", "msg": time_login})
        return HttpResponse(con)