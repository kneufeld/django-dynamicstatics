from django.conf import settings
from django import template

from . import __lookup

register = template.Library()

@register.simple_tag(takes_context=True)
def static_url(context):
    request = context['request']
    return __lookup( request, settings.STATIC_URLS, settings.STATIC_URL )
