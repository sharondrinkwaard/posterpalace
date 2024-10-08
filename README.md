# Poster Palace

Welcome to Poster Palace, the place where you can buy digital posters and pictures. For everyone looking to 'cheer up' their wall, this is your place. 
This is a business to customer project (B2C). 

![Mockup](https://posterpalace.s3.amazonaws.com/media/mockup.png)

## Table of Contents

- [Project Overview](#poster-palace)
- [Features](#features)
  - [Favicon](#favicon)
  - [Navigation Bar](#navigation-bar)
  - [Categories](#categories)
  - [Products](#products)
  - [About Us](#about-us)
  - [Contact](#contact)
  - [Terms & Conditions](#terms--conditions)
  - [Footer](#footer)
  - [Payment System](#payment-system)
  - [Features Left to Implement](#features-left-to-implement)
- [Design](#design)
- [Wireframes](#wireframes)
- [Libraries & Installations](#libraries--installations)
- [Agile Methodology](#agile-methodology)
- [SEO](#seo)
- [Testing](#testing)
  - [Bugs](#bugs)
- [AWS](#AWS)
- [Deployment](#deployment)
- [E-commerce Business Model](#e-commerce-business-model)
- [Credits](#credits)
  - [Acknowledgments](#acknowledgments)


## Features
Below you can find all features that are included in this project.

### Favicon
I generated a Favicon with the logo of Poster Palace on [WebsitePlanet](https://www.websiteplanet.com/nl/webtools/favicon-generator/)

![Favicon](https://posterpalace.s3.amazonaws.com/media/favicon.png)

### Navigation Bar
The navigation bar starts with a logo on the left (on mobile on the right), followed by Posters, about, login, register and the shoppingcart. When logged in, the 'Login' and 'Register' change to 'My Orders' and 'Logout' 
The 'Posters' is a dropdown menu which displays all categories. The 'About' is a dropdown as well and displays the Terms, cookies and contact. 

![Navigation desktop](https://posterpalace.s3.amazonaws.com/media/navigation-bar-desktop.png)

![Navigation mobile](https://posterpalace.s3.amazonaws.com/media/navigation-bar-mobile.png)

### Categories
There are currently 4 categories named Nature, Architecture, People and Artistic. All posters are linked to a category. 

![Categories](https://posterpalace.s3.amazonaws.com/media/categories.png)

### Products
The products being sold on this website are digital posters. I loaded them in using fixtures in the Posters app. 
With some help of ChatGPT Plus I generated these fixtures including images from [Pexels](https://pexels.com). 
To clarify; I created the fixtures myself and let Chat GPT add extra items to this. I chose to do this so I could experience what a tool like AI is capable of. 
All posters have a name, description, price, sku, rating, image + image url and category asigned to it.

All products are sorted by categories. There are four categories named 'Architecture', 'Nature', 'People' which includes portraits and 'Artistic' which included art and graphics. The last one also will eventually include a few posters that are generated by AI. This will be mentioned in the description of the image. 

After deployemnt all new posters will be added through the admin/superuser account and not by updating fixtures. 

![Products](https://posterpalace.s3.amazonaws.com/media/products.png)

### About Us
A short intro about Poster Palace.

![About](https://posterpalace.s3.amazonaws.com/media/about.png)

### Contact
A contact form which enables users to contact Poster Palace. The form is placed on several places on the site and doesn't have a page assigend to it. 

![contact](https://posterpalace.s3.amazonaws.com/media/contact.png)

### Terms & Conditions
Some Terms & Conditions and Cookies because these are nesseccary and obligatory for a webshop.

### Footer
A footer with links to extra information, social media buttons and a newsletter sign up form. 
For the sign up form I am using an external service called [MailerLite](https://www.mailerlite.com/).

![Footer](https://posterpalace.s3.amazonaws.com/media/footer.png)

### Payment System

The payment system I am currently using is [Stripe](https://stripe.com). I used the code to implement Stripe like in the Boutique Ado walkthrough and barely modified it as the code is quite complicated. 

## Features left to implement
- <strong>Watermark</strong> The images need a watermark
- <strong>Identation.</strong> I played around with different identation tabs. 4 and 2. This is why some pages of html are in 4 tabs and others in 2. I am going to set these to the same value of tabs which will be 2.
- <strong>Grammar and spelling. </strong> As English is my second language, there might be some grammar or spelling mistakes. I want to correct these in the future.
- <strong>Filtering and sorting.</strong> I want the user to be able to sort and filter the products not only by category as is right now. But also by price and name. 
- <strong>Pinterest.</strong >I want to add a Pinterest link to the Pinterest account (not signed up yet).
- <strong>Design. </strong> I'm not content about the design of this project. Due to a time limit I decided to not put too much time in it and focus on the technical side first.
- <strong>Unsolved bugs.</strong> I want to fix unsolved bugs.
- <strong>Category for AI.</strong> Eventually I want to add an extra (sub) category for posters that are generated by AI. Currently they are under the 'Artistic' category as the images are all related to art. 
- <strong>Description for AI.</strong> The images that are generated by AI need to have a description which mentions that the posters are generated by AI. So far this is not mentioned. 
- <strong>Able admin to upload posters without having to access the django admin panel.</strong>
- <strong>Improve the scores of the lighthouse report.</strong>
- <strong>Set options like color or quality of posters.</strong> Currently these options are not available. Though I started adding some code for the color options. The code is not in use yet, but I decided to leave it there and not delete it. As I want to continue implementing this after getting the project results back.
 

## Design
- I used Balsamiq to create a wireframes and first picture of what this project would look like.

### Wireframes
The wireframes are very basic and only display the nesseccary features. 

Homepage

![Homepage](https://posterpalace.s3.amazonaws.com/media/home.png)


Product page

![Products](https://posterpalace.s3.amazonaws.com/media/products-page.png)

Product detail

![Product detail](https://posterpalace.s3.amazonaws.com/media/product-detail.png)


Shopping cart

![shoppingcart](https://posterpalace.s3.amazonaws.com/media/shoppingcart.png)


Checkout page

![Payments](https://posterpalace.s3.amazonaws.com/media/payment.png)


Order confirmation

![order confirmation](https://posterpalace.s3.amazonaws.com/media/order-confirmation.png)

### Flowchart
I created a flowchart with [Whimsical](https://whimsical.com).

![flowchart](https://posterpalace.s3.amazonaws.com/media/flowchart.png)


### Code used from other resources
Some of the code of this project are from other resources. 
The hover of the image grid idea on the homepage is taken from [CodePen](https://codepen.io/knyttneve/pen/YgZbLO) and I customized it so it would fit into my project.
When you hover over it (only on desktop), the image zooms in and the letters underneath disappear.

![image hover](https://posterpalace.s3.amazonaws.com/media/image-hover.png)

## Libraries & Installations
- Django Allauth
- Summernote 
- Pillow
- Crispy forms
- Flask
- Stripe Payments
- MailChimp
- MailerLite

## Agile
When planning this project, I started writing the epics first. Then I broke them down into user stories. For this I have created an Excel sheet and a kanban board.

For this portfolio project the estimated time is 16 weeks.
For the total project (including the features left to implement) I am estimating 20 weeks

Backlog:
![Backlog](https://posterpalace.s3.amazonaws.com/media/backlog.png)
In progress:
![Kanban board in progress](https://posterpalace.s3.amazonaws.com/media/kanban_board_progress.png)
Finished:
![Kanban board finished](https://posterpalace.s3.amazonaws.com/media/kanban_board_finish.png)


Items:
![Team items](https://posterpalace.s3.amazonaws.com/media/team_items_1.png)
![Team items 2](https://posterpalace.s3.amazonaws.com/media/team_items_2.png)


### User stories and kanban board link
[Click Here](https://github.com/users/sharondrinkwaard/projects/7)

User stories are found in the sheet below and are devided by three categories named customer, admin and developer.
The light blue and white lines seperate the epics. Mostly, one user story is also one epic. 
Normally I would add several user stories under one epic, but in this case, the user stories where already quite big, that I decided to make (almost) every user story, also one epic. 
This way it helped me keep track and stay focussed on one user story.
![User stories](https://posterpalace.s3.amazonaws.com/media/user_stories.png)

## SEO
- I added Meta tags to add keywords and a description
- Lighthouse report
- I used Semantic Code like a header, h1 and h2 on every page in the correct order, several sections, footer etc.
- I did research on what would be correct keywords to use
- Alt + rel attributes
- Account on Facebook and Instagram and will use Pinterest in the future as well.
- Email newsletter through MailerLite- A newsletter welcome email is being send when a new subscriber is added to the newsletter group.
- Lighthouse report 

![Lighthouse report](https://posterpalace.s3.amazonaws.com/media/lighthouse-report.png)
## Testing

When running through the validators, I run in a few issues. 
The html validator is very specific only for html and I am working with integrated python inside the html. 
This way I have to look bypass all django errors which is very confusing.
As far as I could see there are no specific html errors in this project.

- [HTML Validator](https://validator.w3.org/).

- [CSS validator](https://jigsaw.w3.org/) - No errors returned.

- [Python validator](https://extendsclass.com/python-tester.html) - No errors returned.

### Manual Testing - Python & JavaScript
- I tested it the project displays well in Chrome and Microsoft Edge.

- I tested if all buttons and links work correctly. I confirm that they indeed do by clicking on all of them.

- I confirm that this design is responsive, functions well and looks good on all standard media devices, desktop, tablet and mobile phone. I tested this by using DevTools in the Chrome browser.

- I tested if all images are being displayed correctly from AWS S3. Previously the images were not loading. Now they do and I confirm that they indeed are all being displayed. I tested this by loading every page several times to see if the images are being displayed.

- I confirm that the messages/alerts (JavaScript) are working. I tested this by logging in and out several times. Each time a messages was being displayed at the top of the page. I also checked that the message would dissappear on it's own. They don't do that on the deployed project. This is also mentioned in unsolved bugs. 

- I confirm that all user stories are implemented and are fullfilled.


## Bugs
Below you can find a description of bugs I ran into while making this project. 
### Solved Bugs
- Copying the allauth templates into my own directory. 
Using the commands in the terminal like in the videos didn't work. So I tried installing django allath again. Now the terminal displayed 'Requirement already satisfied' with the correct path of where allauth was installed. Using this helped me copy all those files into my own directory.
'''
    cp -r /usr/local/python/3.10.13/lib/python3.10/site-packages/allauth/templates* ./templates/allauth/
'''

- Currently when typing 
''' pip3 freeze > requirements.txt ''' 
in the terminal, it did result in an empty file. Previously this file was filled with all the dependencies, but now it is empty. 
The problem was not in the terminal,  but that I created a new workspace on Gitpod so I could use the PRO version provided by Code Institute. I didn't know that I had to install all requirements again, so I did using:
''' pip install -r requirements.txt ''' 

- Dependency conflict when installing MailChimp. When installing, an error occurred displaying that the newest version of MailChimp required 'request'. The version of request I had installed wasn't compatible, but I couldnt upgrade it because other versions of urllib and botocore (and lots of other installations) depend on it. I checked this using 'pip3 check' in the terminal. Long story short, I eventually solved the conflict and all versions where working correctly. I just couldn't use the newest version of MailChimp. I downgraded MailChimp and continued implementing it in my project. When installing the API, I learned that for the API to work, I do need the newest version of MailChimp. I decided to use MailerLite instead as I was afraid that AWS won't work correctly if I have to downgrade boto and botocore for MailChimp to work. 
MailerLite was quite easy to set up and is working correctly. 

- AWS bucket issue. Staticfiles were not uploading to the bucket. Due to some spelling mistakes like 'acces' instead of  'access' and naming the bucket policy instead of the bucket name itself, it was not working. When I changed those, the staticfiles where working.

### Unsolved Bugs
 - Bootstrap alert doesnt close after a few seconds. The user has to click 'X' to close it.
 - alignment of shoppingcart and checkout page. By accident I deleted and modified some code for these pages. Which results in not being fully responsive.


## AWS and File Storage
Poster Palace uses Amazon Web Services (AWS) S3 (Simple Storage Service) to store and manage all media and static files. The S3 bucket is used to store all digital poster images, and static assets such as CSS and images needed for the website's interface.

By using AWS S3, the platform ensures that:
- Files are securely stored and easily accessible.
- Media files, including high-resolution digital posters, are delivered quickly and reliably to users.
- Static files are offloaded from the web server to improve the website’s performance and scalability.

S3’s integration with Django allows Poster Palace to manage all files in the cloud, ensuring that the webshop can handle future growth with ease. AWS S3 also provides redundancy and backups, so all files are safely stored and always available for downloads by customers.

By setting the Content-Disposition header to attachment (in AWS settings, Metadata), it is ensured that the file is being downloaded instead of being displayed in the browser.

## Deployment
1. <strong>Create a Heroku Account.</strong> Go to Heroku's website. Sign up for a free Heroku account if you don’t have one.
2. <strong>Create a New Heroku App</strong>After logging in, click on the "New" button on the dashboard, then select "Create New App".
Give your app a unique name and choose the appropriate region (United States or Europe).
Click "Create App".
3. <strong>Connect to GitHub Repository</strong>
In the Deploy tab of your newly created app, scroll down to the Deployment method section.
Select GitHub as the deployment method.
Click Connect to GitHub, and authorize Heroku to access your GitHub account if prompted.
In the Search for a repository field, type the name of your webshop’s GitHub repository and click Search.
Once your repository is found, click Connect next to the correct one.
4. <strong>Enable Automatic Deploys (Optional)</strong>
If you want Heroku to automatically deploy your app every time you push changes to your GitHub repository, scroll down to the Automatic Deploys section.
Click Enable Automatic Deploys.
5. <strong>Manual Deployment</strong>
If you prefer manual deployments, scroll down to the Manual Deploy section.
Choose the branch you want to deploy (usually main or master).
Click Deploy Branch to start the deployment process.
6. <strong>Add Buildpacks</strong> (I didn't for my project.)
Go to the Settings tab in your Heroku app dashboard.
Scroll down to the Buildpacks section and click Add Buildpack.
Add the following buildpacks in the correct order:
Python (select from the list and click Save).
Node.js (if your Django project includes front-end build tools like Webpack).
7. <strong>Configure Environment Variables</strong>
Still in the Settings tab, scroll down to the Config Vars section and click Reveal Config Vars.
Add the following environment variables:
SECRET_KEY: Your Django secret key.
ALLOWED_HOSTS: Add your Heroku app URL.
Any other environment variables your app needs (e.g., database URL, Stripe keys, MailerLite etc.).
8. <strong>Provision the Heroku Postgres Add-on (Optional)</strong>
If your project uses a PostgreSQL database, scroll down to the Add-ons section on the Resources tab.
In the search bar, type Heroku Postgres and select the free Hobby Dev plan.
Click Submit Order Form to add the database to your app.
As I'm using the free version, I do not have add-ons. 
9. Create a Django Superuser (Optional)
In the same console, you can create a superuser to access Django’s admin panel by running:
'python manage.py createsuperuser' 
10. Launch Your App
After the deployment completes, go to the Activity tab to see the deployment logs.
Once it’s ready, click the Open App button in the top-right corner to view your live webshop.


## E-commerce Business Model
<strong>1. Revenue Streams.</strong>
The webshop generates revenue by selling digital posters, with customers purchasing individual posters through secure Stripe payments.

2. <strong>Product Offering</strong>
The shop offers digital posters which customers can instantly download after purchase.

3. <strong>Target Audience</strong>
The target audience includes art enthusiasts, homeowners, and small businesses seeking affordable, customizable digital artwork.

4. <strong>Customer Acquisition</strong>
The webshop utilizes SEO, email marketing via MailerLite, social media (Facebook and Instagram) to attract customers.

5. <strong>Payment and Transaction Model</strong>
Stripe is used for secure online payments. After purchase, customers receive a confirmation email with a download link for their digital poster. The posters can also be downloaded right after purchase on the checkout_succes page.

6. <strong>Distribution and Delivery</strong>
All products are digital, ensuring instant delivery via email, eliminating shipping costs and delays.

7. <strong>Customer Support</strong>
Support is available for issues like purchase errors or download problems. Refunds are provided in specific cases, and customer engagement is enhanced through emails and a contact form.

8. <strong>Growth Strategy</strong>
The business plans to expand its product range, collaborate with artists, and explore partnerships with other platforms to broaden its reach.

## Credits
- [Stackoverflow](https://stackoverflow.com/)
- [Google Translate](https://translate.google.com/)
- [W3Schools](https://www.w3schools.com/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Stripe Documentation](https://docs.stripe.com/)

### Acknowledgments
- Thank you Code Institute and mentor Daisy for guiding me through this project. 
- Thank you fellow students on Slack for the contact and motivation.
- Thank you Tutor support for guiding me in the right direction.
- Thank you Student Care for reaching out.

