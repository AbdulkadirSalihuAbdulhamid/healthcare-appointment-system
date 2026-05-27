# core/templatetags/money.py

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def money(amount, decimals=2):
    """
    Usage in templates:
      {% load money %}
      {% money value %}            -> ₦ 12,345.67
      {% money value 0 %}          -> ₦ 12,346
      {% money value 2 %}          -> ₦ 12,345.67
    """
    symbol = getattr(settings, "CURRENCY_SYMBOL", "₦")
    try:
        n = float(amount)
    except (TypeError, ValueError):
        return f"{symbol} 0.00" if decimals else f"{symbol} 0"
    fmt = f"{{:,.{int(decimals)}f}}"
    return f"{symbol} {fmt.format(n)}"
