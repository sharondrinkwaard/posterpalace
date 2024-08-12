from .models import UserProfile
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        ''' Add placeholder '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_email': 'E-mail',
            'default_phone_number': 'Phone Number',
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
        }