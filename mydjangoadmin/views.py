# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/02/02 19:11:20
@Contact :   xianhe_yan@sina.com
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def ping(req):
    if req.method == 'GET':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "GET"}))
    elif req.method == 'POST':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "POST"}))
    elif req.method == 'PUT':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "PUT"}))
    elif req.method == 'DELETE':
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "DELETE"}))
