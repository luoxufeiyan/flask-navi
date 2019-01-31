#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-1-31 下午10:19
# @Author  : Supergnaw
# @Site    : https://stackoverflow.com/questions/4776924/how-to-safely-get-the-file-extension-from-a-url
# @File    : fileext.py
# @Software: PyCharm
import re

def file_ext( url ):
    # compile regular expressions
    reQuery = re.compile( r'\?.*$', re.IGNORECASE )
    rePort = re.compile( r':[0-9]+', re.IGNORECASE )
    reExt = re.compile( r'(\.[A-Za-z0-9]+$)', re.IGNORECASE )

    # remove query string
    url = reQuery.sub( "", url )

    # remove port
    url = rePort.sub( "", url )

    # extract extension
    matches = reExt.search( url )
    if None != matches:
        return matches.group( 1 )
    return None