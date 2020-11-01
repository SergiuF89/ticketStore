from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django.shortcuts import reverse

ADDRESS_CHOICES = (
      ('B', 'Billing'),
      ('S', 'Shipping'),
)
GENDER = (
      (1, 'Male'),
      (2, 'Female'),
      (3, 'N/A'),
)


class UserProfile(AbstractUser):
      gender = models.IntegerField(choices=GENDER, default=3)
      birth_date = models.DateField(null=True, blank=True)
      stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
      one_click_purchasing = models.BooleanField(default=False)
      phone_number = models.CharField(max_length=15, blank=True)
      profile_image = models.ImageField(blank=True, default='no_image.png', upload_to='')
      country = CountryField(default='Romania')
      joined_on = models.DateField(auto_now_add=True, blank=True)

      def get_absolute_url(self):
            return reverse('core:profile-view', kwargs={
                  'pk': self.pk
            })

      def __str__(self):
            return self.username


class Address(models.Model):
      user = models.ForeignKey(UserProfile,
                               on_delete=models.CASCADE)
      street_address = models.CharField(max_length=100)
      apartment_address = models.CharField(max_length=100)
      country = CountryField(multiple=False)
      zip = models.CharField(max_length=100)
      address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
      default = models.BooleanField(default=False)

      def __str__(self):
            return self.user

      class Meta:
            verbose_name_plural = 'Addresses'
