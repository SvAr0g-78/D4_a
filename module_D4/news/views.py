from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML,
    # в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 7   # поставим постраничный вывод в три элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу
        # другого фильтра
        return context


# создаём представление, в котором будут детали конкретного отдельного товара
class PostsDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта


# создаем представление поиска
class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self,*args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }


# представление добавления новостей
class Add(CreateView):
    model = Post
    template_name = 'add.html'
    form_class = PostForm
    success_url = '/news/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаем новую форму

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся
            form.save()  # сохраняем

        return super().get(request, *args, **kwargs)


# представление редактирования
class Update(UpdateView):
    template_name = 'add.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте,
    # который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# представление для удаления новости или статьи
class Delete(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all
    success_url = '/news/'

