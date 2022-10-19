from django.db import models


class AboutModel(models.Model):
    about_img = models.ImageField(upload_to='about/', verbose_name='Изображение')
    about_title = models.CharField(max_length=120, verbose_name='Зашоловок')
    about_descriptions = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return self.about_title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'