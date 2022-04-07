from django.db import models
from django.contrib.auth.models import User  # D2 импортируем модель User
from django.db.models import Sum  # D2 импортируем Sum

# D2 модель Автор
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)  # поле "автор юзер" со связью "один к одному" с моделью User
    ratingAuthor = models.SmallIntegerField(default=0)  # поле "Рейтинг Автора", по умолчанию =0

    def update_rating(self):  # суммарный рейтинг автора
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

    #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.authorUser}'


# D2 модель Категории
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)  # поле "имя", макс. длина =64, уникальность =Да

    #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.name}'

# D2 модель Сообщение
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # поле "автор" со связью "один к одному" с моделью "Автор"

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )

    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)  # поле "Категория Выбора", макс. длина =2, выбрать из CATEGORY_CHOICES, по умолчанию =СТАТЬЯ
    dateCreation = models.DateTimeField(auto_now_add=True)  # поле "дата создания", автоматически добавить =Да
    postCategory = models.ManyToManyField(Category, through='PostCategory')  # поле "категория сообщение" со связью "многие ко многим" с моделью "Категории", с промежуточным полем "Категория Стати"
    title = models.CharField(max_length=128)  # поле "заголовак", макс. длина =128
    text = models.TextField()  # поле "текст"
    rating = models.SmallIntegerField(default=0)  # поле "рейтинг", по умолчанию =0

    def like(self):  # метод лайк
        self.rating += 1  # +1 к рейтингу
        self.save()  # сохраняем

    def dislike(self):  # метод дизлайк
        self.rating -= 1  # -1 к рейтингу
        self.save()  # сохраняем

    def preview(self):  # метод предпросмотр
        return self.text[0:123] + '...'  # возвращает первые 123 символа текста

    #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.title}'

    # абсолютный путь, чтобы после создания перебрасывало на страницу с новостью
    def get_absolute_url(self):
        return f'/news/{self.id}'


# D2 модель промежуточная Категории Сообщений
class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)  # поле "собщение через", "внешний ключ" с моделью "Сообщения"
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)  # поле "категория через", "внешний ключ" с моделью "Категории"


# D2 модель Комментарии
class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)  # поле "коментарии сообщения", "внешний ключ" с моделью "Сообщения"
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)  # поле "коментарий .юзер", "внешний ключ" с моделью "Юзер"
    text = models.TextField()  # поле "текст"
    dateCreation = models.DateTimeField(auto_now_add=True)  # поле "дата создания", автоматически добавить =Да
    rating = models.SmallIntegerField(default=0)  # поле "рейтинг", по умолчанию =0

    def like(self):  # метод лайк
        self.rating += 1  # +1 к рейтингу
        self.save()  # сохраняем

    def dislike(self):  # метод дизлайк
        self.rating -= 1  # -1 к рейтингу
        self.save()  # сохраняем

    #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.commentUser}: {self.text[:20]}'
