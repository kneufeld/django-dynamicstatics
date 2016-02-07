from django.conf import settings
from django import template

register = template.Library()

from . import __lookup

@register.simple_tag(takes_context=True)
def media_url(context):
    request = context['request']
    return __lookup( request, settings.MEDIA_URLS, settings.MEDIA_URL )
