from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager


class Department(models.Model):
    name = models.CharField('Название отдела', max_length=256)
    is_public = models.BooleanField('Публичный', default=True)


class Role(models.Model):
    name = models.CharField('Должность', max_length=256)


class Specialty(models.Model):
    name = models.CharField('Специализация', max_length=256)


class WWUser(AbstractBaseUser):
    username = None
    email = models.EmailField('E-mail', unique=True)
    phone = models.CharField('Телефон', max_length=16)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    bio = models.TextField('Инфо', max_length=256)
    specialty = models.ManyToManyField(
        Specialty,
        related_name='user',
        blank=True,
        null=True
    )
    rating = models.FloatField(
        'Рейтинг',
        max_length=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.0)],
        default=5.0
    )
    is_staff = models.BooleanField('Корпоративная', default=False)
    is_superuser = models.BooleanField('Админ', default=False)
    is_editor = models.BooleanField('Редактор', default=False)
    is_active = models.BooleanField('Активна', default=True)
    is_public = models.BooleanField('Публичная', default=True)
    reg_date = models.DateTimeField('Дата регистрации', auto_now_add=True)
    department = models.ForeignKey(
        Department,
        related_name='user',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Отдел'
    )
    role = models.ForeignKey(
        Role,
        related_name='user',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Должность'
    )
    picture = models.ImageField(
        'Фото',
        blank=True,
        null=True,
        upload_to='images/profile/'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name', ]

    def __str__(self) -> str:
        return (self.first_name + ' ' + self.last_name)
