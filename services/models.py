from django.db import models


class ServicesModel(models.Model):
    services_img = models.ImageField(upload_to='services', verbose_name='Картинка')
    services_title = models.CharField(max_length=100, verbose_name='Заголовок')
    services_descriptions = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return self.services_title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
