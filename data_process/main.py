# -*- coding: utf-8 -*-
# !/usr/bin/python
# coding:utf-8
import os
from data_process import MethodClass as MC

os.mkdir('/Users/BuleSky/Desktop/addresult') # 结果文件夹路径
os.mkdir('/Users/BuleSky/Desktop/temperature') # 结果文件夹路径
os.mkdir('/Users/BuleSky/Desktop/liquid') # 结果文件夹路径
os.mkdir('/Users/BuleSky/Desktop/work') # 结果文件夹路径

file_dir = "/Users/BuleSky/Desktop/txt/"  # 数据文件夹路径
for root, dirs, files in os.walk(file_dir):
    for i in range(1):
        name = files[i]
        path = '/Users/BuleSky/Desktop/txt/'
        file_object = MC.file(name, path)
        df_rel = file_object.reline()
        rf2_joint = file_object.joint(df_rel)
        data_tem = file_object.liquid(rf2_joint)
        df_result = file_object.temperature(data_tem)
        file_object.addresult(df_result)

