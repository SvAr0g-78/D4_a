from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно
# их искать и фильтры потеряются

# заменяет слова "жесть", "афигенно", "круто" на слово "здорово" (для рабочего примера: первая стать, 10 слово)
@register.filter(name='Censor')
def Censor(value, arg):
    value = value.replace("что", "№*?*№")
    value = value.replace("раз", "###-????????-###")
    value = value.replace("Борис", "******")
    return value