#!/usr/bin/env python
# coding: utf-8

import os
import sys

sys.path.append('/data/www')
sys.path.append('/data/www/testserver')

os.environ['DJANGO_SETTINGS_MODULE'] = 'testserver.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
