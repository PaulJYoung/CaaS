from django import template
#from django .models import UpdateText

register = template.Library()

#@register.simple_tag
#def update_string_header(update_value)
#
#    Updatetext = UpdateText.objects.order_by('-post_date')[:1]
#    context = {
# 	      'Updatetext': Updatetext,
#    }
#    return Updatetext
