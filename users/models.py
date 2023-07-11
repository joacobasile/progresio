from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models



class CustomUser(AbstractUser):
    name = models.CharField(('name'), max_length=255)
    username = models.CharField(
        ('username'),
        unique=True,
        max_length=150,
        validators=[],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        ('email address'),
        unique=True,
        validators=[EmailValidator],
        error_messages={
            'unique': ("A user with that email already exists."),
        },
    )
    birthday = models.DateField(('birthday'), null=True, blank=True)

    photo = models.ImageField(upload_to='profile_photos/', default='default_photo.jpg')
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'birthday']

    def __str__(self):
        return self.username 

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')


