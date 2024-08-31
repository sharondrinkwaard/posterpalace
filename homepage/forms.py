from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class NewsletterForm(forms.Form):
    email = forms.EmailField(label="Your Email", max_length=100)