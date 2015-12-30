"""
URLpatterns for the debug panel.

These should not be loaded explicitly; It is used internally by the
debug-panel application.
"""
from distutils.version import StrictVersion
import django

_PREFIX = '__debug__'

if StrictVersion(django.get_version()) < StrictVersion('1.9'):
    # Handle legacy urls.py, which use the patterns function to build urls
    try:
        from django.conf.urls import patterns, url
    except ImportError:  # django < 1.4
        from django.conf.urls.defaults import patterns, url

    urlpatterns = patterns('debug_panel.views',
        url(r'^%s/data/(?P<cache_key>\d+\.\d+)/$' % _PREFIX, 'debug_data', name='debug_data'),
    )
else:
    # Django 1.9+ uses just a list of url instances, and does not use string
    # view arguments to url()
    from debug_panel.views import debug_data
    from django.conf.urls import url

    urlpatterns = [
        url(r'^%s/data/(?P<cache_key>\d+\.\d+)/$' % _PREFIX, debug_data, name='debug_data'),
    ]
