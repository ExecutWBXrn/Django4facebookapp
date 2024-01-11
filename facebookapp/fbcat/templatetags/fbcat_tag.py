from django import template
import fbcat.views as views

register = template.Library()

@register.simple_tag(name='cat_db')
def cat_db():
    return views.cat_db

@register.simple_tag(name='db_fb')
def db_fb():
    return views.db_fb