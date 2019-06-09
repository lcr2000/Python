#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 22:08
# @Author  : fangguizhen
# @FileName: index_view.py
# @Software: PyCharm
from django.shortcuts import render
from django.views.decorators import csrf

def index(request):  # index页面加载
    context = {}
    return render(request, 'index.html', context)