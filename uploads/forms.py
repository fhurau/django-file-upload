from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

    def clean_profile_picture(self):
        file = self.cleaned_data.get('profile_picture', False)
        if file:
            if file.size > 1024 * 1024 * 5:
                raise forms.ValidationError("File size must be under 5MB")
            if not file.content_type in ['image/jpeg', 'image/png', 'application/pdf']:
                raise forms.ValidationError("Only JPEG, PNG, and PDF files are allowed.")
            return file
        else:
            raise forms.ValidationError("Couldn't read uploaded file.")
