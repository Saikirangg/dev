from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.views.decorators.csrf import csrf_exempt

class CustomAccountManager(BaseUserManager):
    @csrf_exempt
    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    @csrf_exempt    
    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    role_type_choices = (
        ('1', u'Super Admin'),
        ('2', u'Admin'),
        ('3', u'Team Leader'),
        ('4', u'Telecaller'),
        ('5', u'Delivery '),
    )

    store_type_choices = (
        ('1', u'gourmet-garden-mumbai'),
        ('2', u'gourmet-garden-chennai'),
        ('3', u'gourmet-garden-banglore'),
        ('4', u'gourmet-garden-hyderabad'),
    )

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    contact = models.CharField(max_length=12)
    role_type = models.CharField(max_length=32, choices=role_type_choices, null=True, blank=True)
    store_type = models.CharField(max_length=32, choices=store_type_choices, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', ]

    def __str__(self):
        return self.user_name