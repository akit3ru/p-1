from django.db import models


class Advert(models.Model):
    # для небольшого текста с опр. значением символов
    title = models.CharField('Заголовок', max_length=128)
    # для длинного текста и не знаем какой длины
    description = models.TextField('Описание')
    # для целых и дробных чисел
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Если торг уместен - True (1), если не уместен - False (0)')
    # срабатывает 1 раз при создании
    created_at = models.DateTimeField(auto_now_add=True)
    # срабатывает каждый раз при изменениях
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.description} {self.price} {self.auction} {self.created_at} {self.updated_at}"
