#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-1-6 下午3:29
# @Author  : Omar Shehab & LXFY
# @Site    : https://stackoverflow.com/questions/4674460/how-to-get-favicon-by-using-beautiful-soup-and-python
# @File    : favicon.py
# @Software: PyCharm
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
from libs import fileext
from libs.fileext import file_ext


def get_favicon(id, url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read())
    icon_link = soup.find("link", rel="icon")
    if icon_link == '':
        return '' # break
    try:
        icon = urllib.request.urlopen(icon_link['href'])
    except:
        icon = urllib.request.urlopen(url + icon_link['href'])
    if icon.url:
        icon_ext = file_ext(icon.url)
        localpath = str(os.path.abspath("../static/img/favicon/") + "/" + str(id) + icon_ext) #TODO 扩展名
        urllib.request.urlretrieve(icon.url, localpath)
        return localpath
