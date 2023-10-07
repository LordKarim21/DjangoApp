from django import template
from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu_app/menu.html')
def draw_menu(menu_name, request_path):
    menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children')
    return {'menu_items': menu_items, 'request_path': request_path}
