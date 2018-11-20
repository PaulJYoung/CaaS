from django import template
from django .models import UpdateText

register = template.Library()

@register.simple_tag
def update_string_header()


