from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")

@register.filter
def rnreplace(value):
    return value.replace("\r\n","<br/>")