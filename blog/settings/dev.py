# -*- coding: utf-8 -*-

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG


DEV_APPS = [
    'django_extensions',
    'debug_toolbar',
]

INSTALLED_APPS += DEV_APPS

MIDDLEWARE = [
    'libs.middleware.AtopdedTo110DebugMiddleware',
] + MIDDLEWARE

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel'
]

DEBUG_TOOLBAR_CONFIG ={
    'JQUERY_URL': '//cdn.bootcss.com/jquery/3.1.0/jquery.min.js',
}
