from django.forms import ModelForm
from .models import Post


# Создаем модельную форму
class PostForm(ModelForm):
    # # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text']