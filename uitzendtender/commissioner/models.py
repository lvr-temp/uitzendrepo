from django.db import models
from django.conf import settings

from tender.models import Tenderbase, Branch, Country


class Company(Tenderbase):
    name = models.CharField(verbose_name='bedrijfsnaam', max_length=80)
    description = models.TextField(verbose_name='omschrijving bedrijf', blank=True, null=True)
    website = models.URLField(verbose_name='website', max_length=100, blank=True, null=True)
    branche = models.ManyToManyField('tender.Branch')

    def __str__(self):
        return 'inlener_%s' % self.name

    class Meta:
        verbose_name_plural = 'bedrijven'


class CompanyAddress(Tenderbase):
    company = models.ForeignKey(Company)
    street = models.CharField(verbose_name='straat', max_length=80)
    number = models.CharField(verbose_name='huisnummer', max_length=30)
    addition = models.CharField(verbose_name='huisnummer toevoeging', max_length=30)
    zipcode = models.CharField(verbose_name='postcode', max_length=7)
    city = models.CharField(verbose_name='plaatsnaam', max_length=60)
    country = models.OneToOneField('tender.Country')
    latitude = models.FloatField(verbose_name='breedtegraad', blank=True, null=True)
    longitude = models.FloatField(verbose_name='lengtegraad', blank=True, null=True)

    ADDRESS = '0'
    POSTALADDRESS = '1'
    BILLINGADDRESS = '2'

    ADDRESSTYPE = ((ADDRESS, 'bezoekadres'), (POSTALADDRESS, 'postadres'), (BILLINGADDRESS, 'factuuradres'))
    addresstype = models.CharField(max_length=3, choices=ADDRESSTYPE, default=ADDRESS)

    def __str__(self):
        return '%s_%s' % self.company, self.street

    class Meta:
        verbose_name = 'bedrijfsadres'
        verbose_name_plural = 'bedrijfsadressen'


class Contact(Tenderbase):
    company = models.ForeignKey(Company)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'

    GENDERTYPES = ((MALE, 'man'), (FEMALE, 'vrouw'), (UNKNOWN, 'onbekend'))
    gender = models.CharField(verbose_name='geslacht', max_length=3, choices=GENDERTYPES, default=UNKNOWN)
    firstname = models.CharField(verbose_name='voornaam', max_length=40)
    prefix = models.CharField(verbose_name='voorvoegsel', max_length=40, blank=True, null=True)
    lastname = models.CharField(verbose_name='achternaam', max_length=80)
    phonenumber = models.CharField(verbose_name='telefoonnummer', max_length=15)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s' % self.firstname, self.prefix, self.lastname

    class Meta:
        verbose_name = 'contactpersoon'
        verbose_name_plural = 'contactpersonen'