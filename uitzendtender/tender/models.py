from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class Tenderbase(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class TenderUserManager(BaseUserManager):
    def create_user(self, email, userrole, password=None):
        """
        Creates and saves custom user (non-django) with email and userrole
        :param email:
        :param userrole:
        :param password:
        :param is_staff:
        :param is_superuser:
        :param extra_fields:
        :return:
        """
        now = timezone.now()

        if not email:
            msg = "Emailadres is een verplicht veld"
            raise ValueError(msg)

        if not userrole:
            msg = "Gebruikersrol is een verplicht veld"
            raise ValueError(msg)

        email = TenderUserManager.normalize_email(email)
        user = self.model(
            email=email,
            userrole=userrole,
            is_active=True,
            last_login=now,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, userrole, password):
        user = self.create_user(email=email,
                                password=password,
                                userrole=userrole
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class TenderUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='emailadres', max_length=254, unique=True, db_index=True)

    GUEST = '0'
    COMMISSIONER = '1'
    AGENCY = '2'
    STAFF = '3'

    ROLE_CHOICES = ((GUEST, 'guest'), (COMMISSIONER, 'commissioner'), (AGENCY, 'agency'), (STAFF, 'staff'))
    userrole = models.CharField(max_length=20, choices=ROLE_CHOICES, default=GUEST)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["userrole",]

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_created = models.DateTimeField(verbose_name='registratiedatum', auto_now=False, auto_now_add=True)

    objects = TenderUserManager()

    def get_full_name(self):
        return "%s _ %s " % (self.email, self.userrole)

    def get_short_name(self):
        return self.userrole

    def __unicode__(self):
        return self.email


class Branch(Tenderbase):
    name = models.CharField(verbose_name='branchenaam', max_length=150)

    def __unicode__(self):
        return self.name


class Country(Tenderbase):
    name = models.CharField(verbose_name='land', max_length=80, default='Nederland')
    code = models.CharField(verbose_name='ISO drieletterige code', max_length=3, default='NLD')