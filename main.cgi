#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys
from wsgiref.handlers import CGIHandler
from __init__ import create_app
from libs.links import get_all_groups

app = create_app()

CGIHandler().run(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,)
