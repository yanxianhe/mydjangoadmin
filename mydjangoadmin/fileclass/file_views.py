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
import  logging
logger = logging.getLogger("django")

import time
import pyclamd,jieba


# 保存上传文件返回文件路径
#  dir_path req.FILES.get("myfile", None)
def save_file(dir_path,myfile) :
    if not os.path.isfile(dir_path) :
        pass
    else :
        logger.info(" save_file -------------------> %s" % "存在相同的文件")
        return ""
    if not os.path.exists(dir_path) :
        # 创建文件夹
        os.mkdir(dir_path)
    try:
        # 打开特定的文件进行二进制的写操作
        destination = open(os.path.join(dir_path, myfile.name), 'wb+')  
        # 分块写入文件
        for chunk in myfile.chunks():  
            destination.write(chunk)
        destination.close()
        return os.path.join(dir_path, myfile.name)
    except Exception as e:
        logger.error(" save_file -------------------> %s" % e)
        return ""

## 文件绝对路径 file_path
## 返回文件信息
def get_file_properties(file_path) :
    # 判断文件
    if not os.path.isfile(file_path) :
        logger.info(" get_file_properties  -------------------> %s" % "空的文件")
        return ""
    else :
        statinfo = os.stat(file_path)
        st_size = statinfo.st_size
        st_atime = statinfo.st_atime
        st_mtime =  statinfo.st_mtime
        st_ctime = statinfo.st_ctime
        file_pro = {"dir_path":file_path,"st_size":st_size,"st_atime":st_atime,"st_mtime":st_mtime,"st_ctime":st_ctime}
        return  file_pro

## 服务需要开启扫描端口 
## 扫描本机文件绝对路径 file_path
def check_file(file_path) :
    try:
        cd = pyclamd.ClamdAgnostic()
        cd_msg = cd.scan_file(file_path)
        return cd_msg
    except Exception as e:
        logger.error(" check_file -------------------> %s" % e)
        return ""


@csrf_exempt
def upload_file(req):
    curPath = os.path.abspath(os.path.dirname(__file__))
    msg = "success"
    if req.method == "POST":  # 请求方法为POST时，进行处理
        myFile = req.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse(json.dumps({"status_code": "999999", "msg": "no files for upload!"}))
        # 保存文件
        file_paths = save_file(curPath,myFile)
        if(len(file_paths) == 0) :
            return HttpResponse(json.dumps({"status_code": "999999", "msg": "save file error"}))
        try :
            # 扫描文件
            check_files = check_file(file_paths)
            if(len(check_files) == 0) :
                return HttpResponse(json.dumps({"status_code": "999999", "msg": "check file error"}))

            ## 获取文件属性
            get_pro = get_file_properties(file_paths)
            if(len(check_files) == 0) :
                return HttpResponse(json.dumps({"status_code": "999999", "msg": "get_file_properties file error"}))
            ## 文件属性入库/用户
        except Exception as e :
            logger.error(" upload_file -------------------> %s" % e)
            os.remove(file_paths)
            msg = "error"
    return HttpResponse(json.dumps({"status_code": "000000", "msg": msg}))
