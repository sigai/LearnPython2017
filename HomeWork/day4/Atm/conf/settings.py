#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = "Sigai"
import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

DATABASE ={
    'engine': 'file_storage',
    'name': 'accounts',
    'path': os.path.join(BASE_DIR, 'db')# 用os模块拼接路径
}

LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'accesses.log',
}

LOG_LEVEL = logging.DEBUG
