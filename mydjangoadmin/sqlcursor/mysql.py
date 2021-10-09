#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/10/09 15:31:10
@Contact :   xianhe_yan@sina.com
'''

from typing import Counter
from django.db import connection

class sqlcursor() :
    
    def query_db_list(sql) :
        try :
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e :
            return f"SQL ERROR {e}"
        finally :
            connection.close


    def query_one_db_deict(sql,params=None) :
        try :
            with connection.cursor() as cursor :
                if params :
                    cursor.execute(sql,params=params)
                else :
                    cursor.execute(sql)
                
                col_names = [desc[0] for desc in cursor.description]
                row = cursor.fetchall()
                deict = dict(zip(col_names,row))
            return deict
        except Exception as e :
            return f"SQL ERROR {e}"
        finally :
            connection.close


    def query_db_deict(sql,params=None) :
        try :
            with connection.cursor() as cursor :
                rowList = []
                if params :
                    cursor.execute(sql,params=params)
                else :
                    cursor.execute(sql)
                col_names = [desc[0] for desc in cursor.description]
                row = cursor.fetchall()
                for list in row :
                    tmp = dict(zip(col_names,list))
                    rowList.append(tmp)
            return rowList
        except Exception as e :
            return f"SQL ERROR {e}"
        finally :
            connection.close


