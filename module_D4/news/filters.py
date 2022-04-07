#import django_filters
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter
from .models import Post, Author


# создаем фильтр
class PostFilter(FilterSet):
    date = DateFilter(
        field_name="dateCreation",
        lookup_expr="lt",
        label="Дата ",
    )
    date.field.error_messages = {'invalid': 'Введите дату в формате ДД.ММ.ГГГГ. Например 31.12.2020'}
    date.field.widget.attrs = {'placeholder': 'ДД.ММ.ГГГГ'}
    title = CharFilter(lookup_expr='icontains')
    author = ModelChoiceFilter(queryset=Author.objects.all())

    # в мета классе предоставляем модель и указываем поля, по которым будет фильтроваться информация
    # class Meta:
    #     model = Post
    #     fields = ('author', 'title', 'date')

