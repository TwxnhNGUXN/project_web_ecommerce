from django import template
print(">>> custom_filters loaded")  # debug

register = template.Library()

@register.filter(name='ten_filter')
def ten_filter(value):
    return value.upper()
