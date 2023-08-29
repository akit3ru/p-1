from django.db import models
# from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.core import validators
from django.forms import CharField

User = get_user_model()


class SlugField(CharField):
    default_validators = [validators.validate_slug]


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
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, null=True)
    image = models.ImageField('изображение', upload_to='adv/', null=True)

    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: #8A74BE; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: #608BAF; font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    def __str__(self):
        return f"{self.title} {self.description} {self.price} {self.auction} {self.created_at} {self.updated_at}"
