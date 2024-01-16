from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from django_countries.fields import CountryField
from django.core.validators import URLValidator, RegexValidator
import re


class MyUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    phone = models.PositiveBigIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)

    image = models.ImageField(upload_to='accounts/photos/', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    activation_link_created_at = models.DateTimeField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    facebook_profile = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')])
    # country = models.CharField(null=True,blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='myuser_groups',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='myuser_user_permissions',
        related_query_name='user',
    )

