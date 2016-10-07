#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chandan Sinha'
SITETITLE = u'Of The Things I Do'
SITESUBTITLE = u'Building my own HogwartsTech'
SITENAME = u'Chandan Sinha | Techblog'

BROWSER_COLOR = '#4285f4'
COPYRIGHT_YEAR = 2016

SITEURL = ''

PATH = 'content'

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['better_figures_and_images', 'render_math']

TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = u'en'
DEFAULT_DATE = u'fs'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Website', 'https://mechanicalcoder.github.io/'),)

# Social widget
SOCIAL = (('envelope-o','mailto:me13b1009@iith.ac.in'),
		('github','https://github.com/mechandansinha'),
		('linkedin','https://in.linkedin.com/in/chandansinha1'),
		('wordpress', 'https://thevindicatedaxiom.wordpress.com/'),
          ('twitter', 'https://twitter.com/quora_addict'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "mechanicalcodertechblog"

FAVICON = 'http://mechanicalcoder.github.io/images/logo.png'

THEME = "Flex"

PYGMENTS_STYLE = 'emacs'

PAGES_ON_MENU = True

MAIN_MENU = True
USE_FOLDER_AS_CATEGORY = True

MENUITEMS = (('Archives','/archives.html'),
	('Categories','/categories.html'),
	('Tags','/tags.html'),)

OUTPUT_PATH = 'output/'

GOOGLE_ANALYTICS = "UA-80245224-1"

# STATIC_PATHS = ['images', 'pdfs']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
