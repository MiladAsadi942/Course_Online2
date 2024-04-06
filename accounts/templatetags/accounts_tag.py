from django import template
from web.models import Contact

register = template.Library()

@register.simple_tag
def get_about_model():
    try:
        cont = Contact.objects.filter(active=False).count()
    except cont.DoesNotExist:
        about = None
    return about