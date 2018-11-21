from django import template
from ..models import UpdateText

register = template.Library()

@register.inclusion_tag('CloudasaService/base.html')
def update_string_header():
    Updatetext = UpdateText.objects.order_by('-post_date')[:1]
#    context = {
# 	      'Updatetext': Updatetext,
#    }
    return {'Updatetext': Updatetext}
