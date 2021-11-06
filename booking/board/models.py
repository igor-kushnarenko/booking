from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(max_length=30, verbose_name='Электронная почта')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        ordering = ['second_name']
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


class Service(models.Model):
    name = models.CharField(max_length=30, verbose_name='Сервис')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Сервисы'
        verbose_name = 'Сервис'


class Rate(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тариф')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Тарифы'
        verbose_name = 'Тариф'


class PriceRate(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Сервис',
        related_name='price_rate'
    )
    rate = models.ForeignKey(
        Rate,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Тариф',
        related_name='price_rate'
    )
    price = models.FloatField(verbose_name='Стоимость')

    def __str__(self):
        return f'{self.service} - {self.rate} - {self.price}'

    class Meta:
        verbose_name_plural = 'Стоимости'
        verbose_name = 'Стоимость'


class Chair(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Шезлонг',
        related_name='chair'
    )
    number = models.IntegerField(verbose_name='Номер шезлонга')

    def __str__(self):
        return f'{self.number} - {self.service}'

    class Meta:
        verbose_name_plural = 'Шезлонги'
        verbose_name = 'Шезлонг'


class Time(models.Model):
    start_time = models.CharField(max_length=50, verbose_name='Время')

    def __str__(self):
        return f'{self.start_time}'

    class Meta:
        verbose_name_plural = 'Время'
        verbose_name = 'Время'


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Пользователь',
        related_name='booking'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Сервис',
        related_name='booking'
    )
    date = models.DateField(verbose_name='Дата')
    time = models.ForeignKey(
        Time,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Время',
        related_name='booking'
    )
    chair = models.ForeignKey(
        Chair,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Шезлонг',
        related_name='booking'
    )
    rate = models.ForeignKey(
        PriceRate,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Тариф',
        related_name='booking'
    )

    class Meta:
        verbose_name_plural = 'Брони'
        verbose_name = 'Бронь'