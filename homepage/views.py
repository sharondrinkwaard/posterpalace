from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.core.mail import send_mail
from .forms import ContactForm, NewsletterForm
from django.conf import settings
from django.contrib import messages
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import requests

# import logging

# logger = logging.getLogger(__name__)



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



def subscribe_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Fetch all groups from the updated MailerLite API
            api_key = settings.MAILERLITE_API_KEY  # Use your API key from settings
            print(f"MailerLite API Key: {api_key}")  # Debugging line
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}',  # Bearer token authentication
            }

            # Updated MailerLite API endpoint to get groups
            response = requests.get('https://connect.mailerlite.com/api/groups', headers=headers)

            if response.status_code == 200:
                groups = response.json()
                print(groups)  # Print all groups with their corresponding IDs in the console
                
                # Assuming you want to use the first group in the list (you can change this logic)
                if groups:
                    group_id = groups[0]['id']
                    print(f"Using Group ID: {group_id}")

                    # Prepare subscriber data
                    data = {
                        "email": email,
                        "groups": [group_id],  # Subscriber is added to the selected group
                    }

                    try:
                        # Send the subscriber data to the correct API endpoint
                        subscribe_response = requests.post(
                            'https://connect.mailerlite.com/api/subscribers',
                            json=data,
                            headers=headers
                        )
                        if subscribe_response.status_code == 200:
                            # Success: Add a success message
                            messages.success(request, 'Thank you for subscribing!')
                            return redirect('homepage')  # Redirect after success
                        else:
                            # Error from MailerLite: Add an error message
                            messages.error(request, f"An error occurred while subscribing: {subscribe_response.content}")
                            return render(request, 'base.html', {'form': form})

                    except requests.RequestException as e:
                        # Catch request exceptions and display an error message
                        messages.error(request, f"An error occurred: {str(e)}")
                        return render(request, 'base.html', {'form': form})
                else:
                    # No groups found in MailerLite
                    messages.error(request, 'No groups found in MailerLite.')
                    return render(request, 'base.html', {'form': form})
            else:
                # Failed to retrieve groups from MailerLite
                messages.error(request, f"Failed to retrieve groups: {response.status_code}")
                return render(request, 'base.html', {'form': form})

    # Render the form if the request is not POST
    return render(request, 'base.html', {'form': NewsletterForm()})






# mailchimp
# client = MailchimpMarketing.Client()
# client.set_config({
#     "api_key": settings.MAILCHIMP_API_KEY,
#     "server": settings.MAILCHIMP_SERVER_PREFIX
# })

# def subscribe_view(request):
#     if request.method == "POST":
#         form = NewsletterForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             try:
#                 response = client.lists.add_list_member(settings.MAILCHIMP_AUDIENCE_ID, {
#                     "email_address": email,
#                     "status": "subscribed"
#                 })
#                 return HttpResponse("Thank you for subscribing!")
#             except ApiClientError as error:
#                 return HttpResponse(f"An error occurred: {error.text}")
#     else:
#         form = NewsletterForm()

#     return render(request, 'homepage/index.html', {'form': form})
# def subscribe_view(request):
#     if request.method == "POST":
#         form = NewsletterForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             try:
#                 response = client.lists.add_list_member(settings.MAILCHIMP_AUDIENCE_ID, {
#                     "email_address": email,
#                     "status": "subscribed"
#                 })
#                 return HttpResponse("Thank you for subscribing!")
#             except ApiClientError as error:
#                 logger.error(f"Mailchimp API error: {error}")
#                 return HttpResponse(f"An error occurred: {error.text}", status=400)
#             except Exception as e:
#                 logger.error(f"An unexpected error occurred: {e}")
#                 return HttpResponse(f"An unexpected error occurred: {e}", status=500)