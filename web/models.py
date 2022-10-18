from django.db import models
from utils import upload_function
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    slug = models.SlugField(unique=True, verbose_name='Псевдоним/Slug')
    description = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to=upload_function, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name

    @property
    def ct_model(self):
        return self._meta.model_name

    def get_comments(self):
        return self.comments.filter(post=self).all()

    def get_comments_count(self):
        return self.comments.filter(post=self).count()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField(blank=True, verbose_name='Почта')
    body = models.TextField(null=True, verbose_name='Текст комментария')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)

    def __str__(self):
        return 'Комментарий {} на {}'.format(self.name, self.post)


class Avatar(models.Model):
    image = models.ImageField(upload_to='media/avatars')

    class Meta:
        verbose_name = 'Аватар'
        verbose_name_plural = 'Аватарки'

    def __str__(self):
        return self.id

