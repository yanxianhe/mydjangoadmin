#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/10/12 15:50:17
@Contact :   xianhe_yan@sina.com
'''
import timeit
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse
nu = None
class Befores(MiddlewareMixin) :
    start_timeit=timeit.default_timer()

    print(f"-------------------XXXXX 启动成功 :---------------- \n {start_timeit}")
    def process_request(self,request) :
        print(f"{id(request)}")

    def process_response(self,request, response) :
        print(f"{id(request)}")

        return response