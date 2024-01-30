from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.core.validators import URLValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
import uuid


class MyUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    phone = models.PositiveBigIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)

    image = models.ImageField(upload_to='accounts/photos/', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    activation_link_created_at = models.DateTimeField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    facebook_profile = models.URLField(max_length=200,blank=True,null=True,validators=[URLValidator()])
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_verification_code = models.CharField(max_length=6, blank=True, null=True)
    activation_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"User Name is : ' {self.username} ' || ID is : ' {self.id} ' || Email is '{self.email}' || From ' {self.country} ' "

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            Token.objects.create(user=self)
    
    @classmethod
    def get_all_users(cls):
        return cls.objects.all()


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




class Notification(models.Model):
    statuses = [
        ('READ', 'Read'),
        ('UNREAD', 'Unread')
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='notifications')
    title = models.CharField()
    description = models.CharField()
    date = models.DateTimeField(auto_now_add=True)
    readDate = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=statuses, default='UNREAD')

    def clean(self) :
        if self.status == 'UNREAD':
            self.readDate = None
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class PasswordResetToken(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
