from django.db import models


class Article(models.Model):
    art_title = models.CharField('Название статьи', max_length=125)
    art_text = models.TextField('Содержание статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.art_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
