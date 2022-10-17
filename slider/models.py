from django.db import models


class SliderModel(models.Model):
    slider_img = models.ImageField(upload_to='sliderimg/', verbose_name='Изображение')
    slider_title = models.CharField(max_length=100, verbose_name='Заголовок')

    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class CardsBenefitsModel(models.Model):
    cards_img = models.ImageField(upload_to='cards/', verbose_name='Изображение карточки')
    cards_title = models.CharField(max_length=120, verbose_name='Заголовок карточки')
    cards_descriptions = models.CharField(max_length=255, verbose_name='Описание карточки')

    def __str__(self):
        return self.cards_title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'


class LatestWork(models.Model):
    latest_img = models.ImageField(upload_to='latest/', verbose_name='Изображение работ')
    latest_title = models.CharField(max_length=100, verbose_name='Заголовок')
    latest_description = models.CharField(max_length=255, verbose_name='Описание работ')

    def __str__(self):
        return self.latest_title

    class Meta:
        verbose_name = 'Последняя работа'
        verbose_name_plural = 'Последние работы'
