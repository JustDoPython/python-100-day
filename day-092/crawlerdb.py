#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import mysql.connector
import pymysql

from pyspider.result import ResultWorker


class crawlerdb:
    conn = None
    cursor = None

    def __init__(self):
        self.conn = pymysql.connect("127.0.0.1", "root", "12345678", "crawler")
        self.cursor = self.conn.cursor()


    def insert(self, _result):
        

        sql = "insert into info(title,body,editorial,ctime) VALUES('{}','{}','{}','{}')"

        try:
            sql = sql.format(pymysql.escape_string(_result.get('title')), pymysql.escape_string(_result.get('body')), _result.get('editorial'),_result.get('ctime'))
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except mysql.connector.Error:
            print('插入失败')
            return False

