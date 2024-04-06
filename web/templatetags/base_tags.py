from django import template
from ..models import About,Contact,Customer,Catagory

register = template.Library()

@register.simple_tag
def get_about_model():
    try:
        about = About.objects.get(id=1)
    except About.DoesNotExist:
        about = None
    return about


@register.simple_tag
def get_contact_model():
    try:
        cont = Contact.objects.filter(active=False).count()
    except cont.DoesNotExist:
        cont = None
    return cont

@register.simple_tag
def get_customer_count_model():
    try:
        customer_count = Customer.objects.all().count()
    except customer_count.DoesNotExist:
        customer_count = None
    return customer_count

@register.simple_tag
def footer():
    try:
        customer_count = Catagory.objects.all()
    except customer_count.DoesNotExist:
        customer_count = None
    return customer_count
