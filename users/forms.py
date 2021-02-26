from django import forms
from django.contrib.auth.models import User
from .models import Inquiry
from listings.models import Listing

class UserEnquiryForm (forms.ModelForm):
   
    class Meta:
        model = Inquiry
        fields = ['listing', 'name', 'email', 'phone', 'message']


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name is None:
            raise forms.ValidationError("this value cannot be empty")
        else:
            if len(name) > 20:
                raise forms.ValidationError("too many values...")
        return name


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        print(f'Cleaning Phone {phone}')
        return phone
    

    def clean_listing(self):
        listing = self.cleaned_data.get('listing')
        if listing is None:
            raise forms.ValidationError("this value cannot be empty")

        if listing:
            listingObj = Listing.objects.filter(title=listing).exists()
            if not listingObj:
                raise forms.ValidationError("no such listing...")
            
        return listing


