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


class Auth(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Пользователь',
        related_name='auth'
    )
    login = models.CharField(max_length=64, verbose_name='Логин')
    password = models.CharField(max_length=64, verbose_name='Пароль')


class Service(models.Model):
    name = models.CharField(max_length=30, verbose_name='Сервис')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Сервисы'
        verbose_name = 'Сервис'


class Seats(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Сервис',
        related_name='seats'
    )
    seat_number = models.IntegerField(verbose_name='Номер шезлонга')

    def __str__(self):
        return f'{self.seat_number}'

    class Meta:
        verbose_name_plural = 'Шезлонги'
        verbose_name = 'Шезлонг'


class Vault(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Сервис',
        related_name='vault'
    )
    vault_number = models.IntegerField(verbose_name='Номер сейфа')

    def __str__(self):
        return f'{self.vault_number}'

    class Meta:
        verbose_name_plural = 'Сейфы'
        verbose_name = 'Сейф'


class Visit(models.Model):
    date_visit = models.DateField(verbose_name='Дата')
    time = models.ForeignKey(
        'Time',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Период',
        related_name='visit'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Сервис',
        related_name='visit'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Пользователь',
        related_name='visit'
    )

    class Meta:
        verbose_name_plural = 'Посещения'
        verbose_name = 'Посещение'


class Time(models.Model):
    start_time = models.CharField(max_length=50, verbose_name='Время')

    def __str__(self):
        return f'{self.start_time}'

    class Meta:
        verbose_name_plural = 'Время'
        verbose_name = 'Время'


class Ticket(models.Model):
    visit = models.ForeignKey(
        Visit,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Посещение',
        related_name='ticket'
    )
    reservation = models.ForeignKey(
        'Reservation',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Резервирование',
        related_name='ticket'
    )
    ticket_number = models.IntegerField(verbose_name='Номер билета')
    number_persons = models.IntegerField(verbose_name='Количество персон')
    rate = models.ForeignKey(
        'Rate',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Тариф',
        related_name='ticket'
    )

    def __str__(self):
        return f'{self.ticket_number}'

    class Meta:
        verbose_name_plural = 'Билеты'
        verbose_name = 'Билет'


class Reservation(models.Model):
    reservation_date = models.DateTimeField(verbose_name='Дата резервирования')

    def __str__(self):
        return f'Дата резервирования: {self.reservation_date}'

    class Meta:
        verbose_name_plural = 'Резервирования'
        verbose_name = 'Резервирование'


class Bill(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Билет',
        related_name='bill'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Пользователь',
        related_name='bill'
    )
    rate = models.ForeignKey(
        'Rate',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Тариф',
        related_name='bill'
    )

    class Meta:
        verbose_name_plural = 'Счета'
        verbose_name = 'Счет'


class Rate(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тариф')
    price = models.FloatField(verbose_name='Стоимость', default=None)
    description = models.TextField(verbose_name='Описание тарифа')
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='Сервис',
        related_name='rate'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Тарифы'
        verbose_name = 'Тариф'
