#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wang Qiang'
SITENAME = u'Think in Source'
SITEURL = '.'

SITETITLE = SITENAME
SITESUBTITLE = '... never stop learning'
#SITELOGO = ''
#SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

LOCALE = 'en_US'
I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT,
}

THEME = 'Flex'
PLUGIN_PATHS = ['./plugins/']
PLUGINS = ['render_math']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (
          ('linkedin', 'https://www.linkedin.com/in/qiang-wang-69403758/'),
          ('github', 'https://github.com/qwang2505'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Footer ---------------------------
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_NAME = ""
COPYRIGHT_YEAR = 2019
