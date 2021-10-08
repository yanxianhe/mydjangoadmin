# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/02/02 19:11:20
@Contact :   xianhe_yan@sina.com
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,timeit

@csrf_exempt
@csrf_exempt
def login (req) :
    postBody = req.body
    # 判断传值是否位空
    if len(postBody) > 0 :
        start_timeit=timeit.default_timer()
        if req.method == 'POST' :
            ## 验证账户是否存在
            ## 
            ## 生成token
            ## 将token 写入到 Redis/mysql
            ## 将token
            json_result = json.loads(postBody) 
            print(json_result)
            return HttpResponse(json.dumps({"status_code": "000000", "msg": req.method,"Admin-Token" : start_timeit}))
        else :
            return HttpResponse(json.dumps({"status_code": "000000", "msg": req.method,"Admin-Token" : start_timeit}))
    return HttpResponse(json.dumps({"status_code": "Y_E0000", "msg": req.method}))