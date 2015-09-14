from django.template import Library

register = Library()


@register.filter
def bizzfuzz(value):
    if value % 5 == 0 and value % 3 == 0:
        return 'BizzFuzz'
    elif value % 3 == 0:
        return 'Bizz'
    elif value % 5 == 0:
        return 'Fuzz'
    return value