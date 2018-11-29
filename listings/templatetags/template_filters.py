# template_filters.py
from django import template
register = template.Library()

@register.filter(name='phone_number')
def phone_number(number):#number comes in this format '333-333-333'
    """Convert a 10 character string into (xxx) xxx-xxxx."""
    first = number[0:3]
    second = number[4:7]
    third = number[8:14]
    return '(' + first + ')' + ' ' + second + '-' + third