from django.db import models
from django.urls import reverse


class PortfolioModel(models.Model):
    portfolio_img = models.ImageField(upload_to='portfolio/', verbose_name='Фото порфолио')
    portfolio_title = models.CharField(max_length=100, verbose_name='Заголовок')
    portfolio_description = models.CharField(max_length=255, verbose_name='Описание')
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.portfolio_title

    class Meta:
        verbose_name = 'Порфолио'
        verbose_name_plural = 'Порфолио'


class Categories(models.Model):
    categories_name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.categories_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_id': self.pk})
