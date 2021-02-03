# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/02/02 19:11:20
@Contact :   xianhe_yan@sina.com
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

import time
import pyclamd,jieba

@csrf_exempt
def upload_file(req):

    curPath = os.path.abspath(os.path.dirname(__file__))
    if req.method == "POST":  # 请求方法为POST时，进行处理
        myFile = req.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse(json.dumps({"status_code": "000000", "msg": "no files for upload!"}))
        # destination=open(os.path.join('upload',myFile.name),'wb+')
        destination = open(os.path.join(curPath, myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        cd_file_name = curPath + myFile.name
        print(cd_file_name)
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

#        cd = pyclamd.ClamdAgnostic()
#        cd_msg = cd.scan_file(cd_file_name)
#        print(cd_msg)

        return HttpResponse(json.dumps({"status_code": "000000", "msg": "upload over"}))
    else:
        file_list = []
        curPaths = curPath + '\\file'
        files = os.listdir(curPaths)
        for i in files:
            file_list.append(i)
        return HttpResponse(json.dumps({"status_code": "000000", "msg": file_list}))