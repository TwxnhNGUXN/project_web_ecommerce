from django import template

register = template.Library()

@register.filter
def vnd(value):
    """Format số tiền thành dạng 12.345.000₫"""
    try:
        value = float(value)
        return f"{value:,.0f}".replace(",", ".") + "₫"
    except (ValueError, TypeError):
        return value
