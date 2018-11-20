from django import template
from ..models import UpdateText

register = template.Library()

@register.simple_tag
def update_string_header():
    Updatetext = UpdateText.objects.order_by('-post_date')[:1]
#    context = {
# 	      'Updatetext': Updatetext,
#    }
    return Updatetext
