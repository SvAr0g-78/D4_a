from django import template

register = template.Library()


@register.filter(name='Censor')
def Censor(value, arg):
    value = value.replace("договорились", "№*?*№")
    value = value.replace("Выступление", "###-????????-###")
    value = value.replace("Lenta", "******")
    return value
