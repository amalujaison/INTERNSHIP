from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class MyAccount(BaseUserManager):
    def create_user(self, name, email,  phone, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            # username = username,
            name=name,
            phone=phone,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, email, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            **extra_fields,
            # username = username,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = False
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    name = models.CharField(blank=True,null=True,max_length=50)
    email = models.EmailField(max_length=50, unique=True,primary_key=True)
    password = models.TextField(max_length=30)
    phone = models.CharField(max_length=10)
    # publish = models.DateTimeField(default=timezone.now)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone']
    # REQUIRED_FIELDS = ['password']

    objects = MyAccount()



    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True



