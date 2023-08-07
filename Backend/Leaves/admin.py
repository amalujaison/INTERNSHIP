from django.contrib import admin

from Leaves import models
from Leaves.models import Account
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.utils.translation import gettext as _

# Register your models here.




admin.site.register(Account)