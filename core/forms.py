from crispy_forms.layout import Layout
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from users.models import UserProfile
from django.forms import ModelForm, DateField


PAYMENT_CHOICES = (
      ('S', 'Stripe'),
      ('P', 'PayPal')
)


class EditProfileForm(ModelForm):
      def __init__(self, *args, **kwargs):
            super(EditProfileForm, self).__init__(*args, **kwargs)
            self.fields['birth_date'].widget = forms.DateInput(attrs={'type': 'date'})

      class Meta:
            model = UserProfile
            widgets = {'country': CountrySelectWidget(),
                       'birth_date': forms.SelectDateWidget(attrs={'class': 'date'})}
            fields = ['first_name', 'last_name', 'gender', 'birth_date', 'profile_image', 'phone_number', 'country']


class CheckoutForm(forms.Form):
      shipping_address = forms.CharField(required=False)
      shipping_address2 = forms.CharField(required=False)
      shipping_country = CountryField(blank_label='(select country)').formfield(
            required=False,
            widget=CountrySelectWidget(attrs={
                  'class': 'custom-select d-block w-100',
            }))
      shipping_zip = forms.CharField(required=False)

      billing_address = forms.CharField(required=False)
      billing_address2 = forms.CharField(required=False)
      billing_country = CountryField(blank_label='(select country)').formfield(
            required=False,
            widget=CountrySelectWidget(attrs={
                  'class': 'custom-select d-block w-100',
            }))
      billing_zip = forms.CharField(required=False)

      same_billing_address = forms.BooleanField(required=False)
      set_default_shipping = forms.BooleanField(required=False)
      use_default_shipping = forms.BooleanField(required=False)
      set_default_billing = forms.BooleanField(required=False)
      use_default_billing = forms.BooleanField(required=False)

      payment_option = forms.ChoiceField(
            widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
      code = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Promo code',
            'aria-label': 'Recipient\'s username',
            'aria-describedby': 'basic-addon2'
      }))


class RefundForm(forms.Form):
      ref_code = forms.CharField()
      message = forms.CharField(widget=forms.Textarea(attrs={
            'rows': 4
      }))
      email = forms.EmailField()


class PaymentForm(forms.Form):
      stripeToken = forms.CharField(required=False)
      save = forms.BooleanField(required=False)
      use_default = forms.BooleanField(required=False)
