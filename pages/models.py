from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

class Application(models.Model):
    prefix = models.CharField(_("Prefix"), max_length=100, blank=True, null=True)
    referral = models.CharField(_("Referral name"), max_length=100, blank=True, null=True)
    first_name = models.CharField(_("First name"), max_length=100, blank=True, null=True)
    last_name = models.CharField(_("Last name"), max_length=100, blank=True, null=True)
    middle_name = models.CharField(_("Middle name"), max_length=100, blank=True, null=True)
    dob = models.CharField(_("Date of Birth"), max_length=100, blank=True, null=True)
    mother_name = models.CharField(_("Nother name"), max_length=100, blank=True, null=True)
    relationship = models.CharField(_("Relationship Status"), max_length=100, blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=100, blank=True, null=True)
    occupation = models.CharField(_("Occupation"), max_length=100, blank=True, null=True)
    ssn = models.CharField(_("Full SSN"), max_length=100, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=100, blank=True, null=True)
    state = models.CharField(_("City/State/Province"), max_length=100, blank=True, null=True)
    nationality = models.CharField(_("Nationality"), max_length=100, blank=True, null=True)
    phone = models.CharField(_("Telephone number"), max_length=100, blank=True, null=True)
    fax = models.CharField(_("Fax number"), max_length=100, blank=True, null=True)
    income = models.CharField(_("Monthly income"), max_length=100, blank=True, null=True)
    email = models.EmailField(_("Email"), max_length=100, blank=True, null=True)
    bank = models.CharField(_("Financial Institution"), max_length=100, blank=True, null=True)
    description = models.CharField(_("Describe in details how you'll use the money"), max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.first_name