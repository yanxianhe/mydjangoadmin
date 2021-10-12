#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/10/11 16:21:21
@Contact :   xianhe_yan@sina.com
'''

from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json,timeit

# 登录
@csrf_exempt
@csrf_exempt
def login_api (req) :
    postBody = req.body
    # 判断传值是否位空
    if len(postBody) > 0 :
        start_timeit=timeit.default_timer()
        if req.method == 'POST' :
            json_result = json.loads(postBody) 
            print(json_result)
            ## 验证账户是否存在
            ## 
            ## 生成token
            ## 将token 写入到 Redis/mysql
            ## 将token
            username = json_result["username"]
            password = json_result["pwd"]
            user_obj = auth.authenticate(username=username,password=password)

            if not user_obj :
                pass
            else :
                # 等价于 req.session['key'] = req
                auth.login(req,user_obj)

            csrftoken = req.session.get('csrftoken')
            sessionid = req.session.get('sessionid')
            print(f"{csrftoken} {sessionid}")
            return HttpResponse(json.dumps({"status_code": "000000", "msg": "msg"}))
        else :
            return HttpResponse(json.dumps({"status_code": "000000", "msg": req.method,"Admin-Token" : start_timeit}))
    return HttpResponse(json.dumps({"status_code": "Y_E0000", "msg": req.method}))

@login_required(login_url="/admin/")
def logout_api(req) :
    auth.logout(req)
    return HttpResponse(json.dumps({"status_code": "000000", "msg": timeit.default_timer()}))
