# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/02/02 19:11:20
@Contact :   xianhe_yan@sina.com
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json,timeit

@csrf_exempt
@login_required
def check(req):
    start_timeit=timeit.default_timer()
    if req.method == 'GET':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": req.method,"date" : start_timeit}))
    elif req.method == 'POST':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": req.method,"date" : start_timeit}))
    elif req.method == 'PUT':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": req.method,"date" : start_timeit}))
    elif req.method == 'DELETE':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": req.method,"date" : start_timeit}))

