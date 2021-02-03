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
def check(req):
    start_timeit=timeit.default_timer()
    if req.method == 'GET':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "GET ","date" : start_timeit}))
    elif req.method == 'POST':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "POST ","date" : start_timeit}))
    elif req.method == 'PUT':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "PUT ","date" : start_timeit}))
    elif req.method == 'DELETE':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "DELETE ","date" : start_timeit}))

