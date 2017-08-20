from .models import Page


def menu(request):
    return {'menu_items': Page.objects.filter(menu=True)}
