from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        return

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )

        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


#        return self._create_user(email, password, **extra_fields)
# Create your models here.
class User(AbstractUser):
    first_name =  models.CharField(max_length=255, null=False, blank=False)
    last_name =  models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='images/logo.png')
    public_email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    objects = MyUserManager()

    # username = models.CharField(max_length=50, default=None)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.first_name+' '+self.last_name
