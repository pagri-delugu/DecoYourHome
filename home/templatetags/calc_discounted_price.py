from django import template
from math import trunc

register = template.Library()

@register.filter
def discounted(price:int, discount_percentage:int):
    return trunc(price * ((100-discount_percentage)/100))