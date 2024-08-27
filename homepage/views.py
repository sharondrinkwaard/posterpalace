from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages


def index(request):
    """ A view to display the index page """
    return render(request, 'homepage/index.html')

def service(request):
    """ A view to display the customer service page """
    return render(request, 'homepage/service.html')


def contact_view(request):
    ''' 
    A view to get the data from the form, Create an email, Send it to the default email adress
    Display a message and error handling
    '''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data; using cleaned_data instead of request.POST.get because the data is
            # already validated and cleaned according to the rules defined in the forms.py
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            email_subject = f"Contact Form Submission: {subject}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            from_email = email
            recipient_list = [settings.DEFAULT_FROM_EMAIL]
            
            try:
                send_mail(email_subject, email_message, from_email, recipient_list)
                messages.success(request, 'Your message has been sent successfully! We will contact you shortly.')
                return redirect(request.path_info)             
            except BadHeaderError:
                messages.error(request, 'Error. Please try again.')
            except Exception as e:
                messages.error(request, 'An error occurred while sending the email. Please try again.')
        else:
            messages.error(request, 'The form is not valid. Fill in all fields correctly and try again.')

    else:
        form = ContactForm()

    return render(request, 'homepage/index.html', {'form': form})