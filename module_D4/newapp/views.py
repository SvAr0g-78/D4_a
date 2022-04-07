from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from .forms import NewsForm
from .filters import NewsFilter


# class PostsList(ListView):
#     model = Post
#     template_name = 'posts.html'
#     context_object_name = 'posts'
#     queryset = Post.objects.order_by('-dateCreation')
#
#
# class PostsDetail(DetailView):
#     model = Post
#     template_name = 'post.html'
#     context_object_name = 'post'


class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # вписываем наш фильтр в контекст
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # вписываем наш фильтр в контекст
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()


class NewsAddView(CreateView):
    template_name = 'news_add.html'
    form_class = NewsForm
    success_url = '/news/'


class NewsEditView(UpdateView):
    template_name = 'news_edit.html'
    form_class = NewsForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
