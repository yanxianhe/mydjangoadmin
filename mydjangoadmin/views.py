# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/02/02 19:11:20
@Contact :   xianhe_yan@sina.com
'''
from django.http import HttpResponse
import json
import  logging
logger = logging.getLogger("django")

def ping(req):
    if req.method == 'GET':
        logger.info(" -------------------> ping  get")
        return HttpResponse(json.dumps({"status_code": "000000", "msg": "GET"}))