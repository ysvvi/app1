from django.db import models

from tabnanny import verbose

class Post(models.Model):
    title= models.CharField('Заголовок записи', max_length=60)
    description = models.TextField('Текст записи')
    author = models.CharField('Автор', max_length=250)
    data = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='blog_images', blank=True, null=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural= 'Записи'

    def __str__(self):
        return f'{self.title}, {self.author}'
    

