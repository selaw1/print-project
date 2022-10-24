from django import template
from django.urls import translate_url

register = template.Library()

@register.simple_tag(takes_context=True)
def change_lang(context, lang: str, *args, **kwargs):
    """Change lang"""
    path = context["request"].path
    print(path)
    print(context["request"])
    print(context["request"].GET.urlencode())
    return translate_url(path + "?" + context["request"].GET.urlencode(), lang)
