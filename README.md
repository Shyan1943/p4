# DEPLOYMENT

## b) PRODUCTION

### 1. Setting up Github Pages
    i. Sign up <a href="https://github.com/" target="_blank">Github</a>
    ii. Log in to GitHub
    iii. Create a new GitHub Repository

### 2. Launch a workspace container at Gitpod
    i. Click to install <a href="https://www.gitpod.io/docs/browser-extension/" target="_blank">Gitpod Browser Extension </a>on browser in you are using Chrome or Firefox for convenient
    ii. Use `Ctrl+F5` on your Github Repository Page to refresh the browser
    iii. You will see a Gitpod button (Green color) is added to GitHub that does the prefixing for your convenience. And click on that button 
    iv. A workspace is creating as easy as prefixing any GitHub URL with gitpod.io/#.

### Take note to commit often for each individual feature/ﬁx, ensuring that commits are small, well-deﬁned and have clear descriptive messages

### 3. Create file --> requirements.txt  
```
Django==2.2.6
pytz==2020.1
sqlparse==0.3.1
```
### 4. How to use requirements.txt
```
pip3 install -r requirements.txt
```
### 5. Create `.env` file to store the passwords and security-sensitive information.
### 6. Create `.gitignore` file to git ignore the environment variables file, which are never committed to the repository.
```
db.sqlite3
__pycache__
.env
```
### 7. take note to keep debug on any error messages prompt in Gitpod to ensure the use Python code that is consistent in style and conforms to the PEP8 style guide and validated HTML and CSS code.

### 8. Setting up new Django Project
    i. At the Gitpod terminal type `django-admin startproject DGReviewsProject .` to create a new Django project. 
    ii. At settings.py file, `ALLOWED_HOSTS = ["*"]` & saved to allow all server to run this Django project.  

### 9. To create A Superuser : 
    i. At the Gitpod Terminal :
        * Enter `python3 manage.py migrate`, 
        * Enter `python3 manage.py createsuperuser`, 
        * create an admin username, email, password and do remember the details. 
        * Enter `python3 manage.py runserver 8080` to test run Django server 
        * A blue button should appear at the right bottom & to click: "Open Browser".

    ii. At the browser : 
        * enter `/admin` at the end of the url 
        * Enter in the Username & password, which just created at the above step & press enter.

### 10. To create and install a new App : 
    i. At the Gitpod Terminal :
        * Enter `ls -l` to make sure we can see the "manage.py" at our current working directory.
        * Enter `django-admin startapp <app name>` to create a new apps
    ii. In the file *settings.py*, install the app & save 
    iii. Create a new function in "views.py" apps file
    iv. Setup the URLs to the view function: 
        a) At "urls.py" which inside the master project folder :
            * import `include` 
            * add in new path  `path('dg/', include('dgs.urls'))`
        b) Go "dgs" app :
            * right click to create new file "urls.py"
                    ```
                    from django.contrib import admin
                    from django.urls import path, include
                    import dgs.views

                    urlpatterns = [
                        path('', dgs.views.index),
                    ]
                    ```
    v. Test Run Django server by adding `/dg` at the end of the browser url link

### 11. Create Templates  
    i. Create a templates folder in the <dgs> app.
    ii. Inside the templates folder, create another folder named <dgs>
    iii. Create the template named <dg.template.html>
    iv. Change the view function in "views.py" to render the template

### 12. Set up static styles.css file
    i. Create static folder, which must be in the same folder as manage.py
    ii. Inform Django where to find static files by adding below code at "settings.py" & save 
        ```
            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, "static")
            ] 
        ```
    iii. Create <styles.css> file inside the static folder
    iv. To use the static function inside Django templates by including `{%load static %}` CSS file inside the template 
    v. At the template, link stylesheet by including {% static 'styles.css' %}

### 13. Create models 
    i. Create a <Dg> model inside the "dgs/models.py"
    ii. At Gitpod terminal, enter `python3 manage.py makemigrations` to make migrations
    iii. At Gitpod terminal, enter `python3 manage.py migrate` to migrate
    iv. Register the model at dgs/admin.py
    v. Log into the brower admin page, should see the <Dgs> model in the admin 
    
### 14. Create C"R"UD Route for Dgs 
    i. Inside dgs/views.py, import the <Dg> model `from .models import Dg`
    ii. Inside dgs/views.py, change the index() route
    iii. Inside dgs/dg.template.html, use for loop to pull the data

### 15. Create "C"RUD Route for Dgs 
    i. Create a file named "forms.py" inside the dgs app folder.
    ii. Inside "dgs/forms.py" file, import the <Dg> model by entering `from .models import Dg` and add a Form class
    iii. Inside "dgs/views.py" file, import the <DgForm> form by entering `from .forms import DgForm` and add in function
    iv. Create new template `create_dg.template.html`
    v. Inside "dgs/urls.py" file, add a URL for the view function
    vi. Go to browser "/dgs/create" and see if the form shows up.
    vii. To adding a new dg experience, back to the "dgs/views.py" file :
        * we need to import in the reverse and redirect functions from Django
        * modify the create_dg function

### 16. Create CR"U"D Route for Dgs 
    i.  Inside "dgs/views.py" file, import in get_object_or_404 function
    ii. Create a View Function for updating dgs
    iii. Create a `update_dg.template.html` to display the update form
    iv. Inside "dgs/urls.py" file, create the url path
    v. Test
    vi. Inside "dgs/views.py" file, modify the update_dg function to carter for update
    vii. Inside "dgs/dg.template.html" file, add the link to update route 

### 17. Create CRU"D" Route for Dgs 
    i. Inside "dgs/views.py" file, define the view function for delete
    ii. Create a `delete_dg.template.html` to display the delete form
    iii. Test
    iv. Inside "dgs/views.py" file, implement the delete_dg funtion
    v. Inside "dgs/dg.template.html" file, add the link to delete route

### 18. Create a One to Many Relationships (IMDGCode)
    i. Inside "dgs/models.py" file, define the IMDGCode model
    ii. and, define the relationship in the Dg Model
    iii. Inside "dgs/admin.py" file, register IMDGCode model
    iv. At Gitpod terminal, make migrations and migrate (see step 13th ii & iii.)
    v. Inside "dgs/forms.py" file, allow the user to select IMDGCode for Dg

### 19. Setting up User Authentication
    i. At Gitpod terminal, install allauth `pip3 install django-allauth`
    11. Update "DGReviewsProject/settings.py" file
    iii. Go admin panel to add initial settings. 
            * Go to Email Addresses (under Accounts)
            * Click on the superuser email, 
            * Check the Primary and Verified checkbox,
            * Ensure that the superuser email is verified and is the primary email
    iv. Stay on th admin panel to update site settings 
            * Admin Home page and then select Sites
            * Select the first site in the list, and update it to:
            * Domain name: <your browser urls> 
            * Display Name: DG Review Site
    v. Inside the "DGReviewsProject/urls.py" file, import Django `include` & setup
    vi. At the browser, `/accounts/logout` to logout first, then test log in `/accounts/login`
            ```
                To sign up, go to the accounts/signup URL
                To log out, go to the accounts/logout URL
                To log in, go to the accounts/login URL
            ```
    vii. Inside "dgs/dg.template.html" file, display the current logged in user
    viii. Inside "dgs/views.py" to protect a view function by :-
            * import `from django.contrib.auth.decorators import login_required, permission_required`
            * add `@login_required` before the view function that you want to restrict

### 20. Master Templates and Overriding Templates
    i. Create "templates" folder, which must be in the same folder as manage.py
    ii. Right click the "templates" folder, to create "base.template.html" file
    ii. Right click the "templates" folder, to create "allauth" folder
    iii. At Gitpod terminal, enter `cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* templates/allauth`
    iv. Setup the "base.template.html" including load static & link stylesheet
    v. Inside "DGReviewsProject/settings.py" file, tell Django where to find the master template and the overridden templates
    vi. Test : Update the "dgs/dg.template.html" to use the base template

### 21. Flashing messages
    i. Inside "dgs/views.py" : 
            * import `from django.contrib import messages`
            * input flash message `messages.success()` method when a CUD is done successfully
    ii. Insert `MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'` into "DGReviewsProject/settings.py" file to enable flash messages
    iii. Inside "base.template.html" add in flash messages
    iv. Test by creating a new book

### 22. Django Crispy Forms
    i. At Gitpod terminal, enter `pip3 install django-crispy-forms` to install Django Crispy Forms 
    ii. To enable the Django Crispy Forms, inside "DGReviewsProject/settings.py" file :
            * Add `crispy_forms` to INSTALLED_APPS 
            * set the template pack to be Bootstrap 4 `CRISPY_TEMPLATE_PACK = 'bootstrap4'`
    iii. Render form using Crispy Form by loading `{% load crispy_forms_tags %}` & `{{ form|crispy}}`

### 23. Create Reviews App + CRUD 
    i. See step 10, to create and install a new "reviews" App 
    ii. See step 13, to create `Review` models
    iii. See step 15, to create "C"RUD Route for Reviews

### 24. Associating Dgs with User
    i. Inside "dgs/models.py", import `from django.contrib.auth.models import User` and the relationship to the Dg model
    ii. `python3 manage.py makemigrations` & `python3 manage.py migrate`
    iii. Inside "dgs/forms.py", add the relationship field to the Dgform (for testing purpose)
    iv. At browser, test creating a new post with an user
    v. Inside "dgs/views.py", modify create_dg view function
    vi. Inside "dgs/forms.py", remove the relationship field from the Dgform

### 25. Create C"R"UD Route for One Dg_id & its details 
    i. Inside "dgs/views.py" add in a route function to view a dg's details
    ii. Create "dgs/details_dg.template.html" template 
    iii. Inside "dgs/urls.py", create details path, id & route name
    iv. Go "dg.template.html" to add link href to "view_dg_route"
    v. Test browser. On all dgs page, you should able to click href to "dgs/details_dg.template.html" page

### 26. Associating One Dg_id with reviews
    i. Inside "reviews/views.py" :
            * import `from dgs.models import Dg`
            * go to "create_review" function, `dg = get_object_or_404(Dg, pk=dg_id)`
            * process the saving of the review
    ii. Inside "reviews/urls.py" update the create_review_route and give it an id & name
    iii. Inside "reviews/forms.py", remove the "dg" relationship field from the Reviewform
    iv. Inside "reviews/create_review.template.html", pull the dg.title
    v. Go "dgs/details_dg.template.html", use `{% for r in dg.review_set.all %}` to pull all reviews from Review model, which related to a book

### 27. Create CRUD comments & associating its to review 
    i. Step 13~17 to create Comments Model & CUD 
    ii. Step 26 to create "R" route & associate One review_id with comments

### 28. Search engine
    i. See Step 10 to create new "home" app and set up it's url route 
    ii.  Create "home/forms.py", creata a SearchForm
    iii. Inside "home/views.py" :
            * import `from django.db.models import Q` 
            * Update the index view function to do the search
    iv. Create "home/home.template.html"
    v. At "home/urls.py" create home path

### 29. Create "Program" App, Model & CR
    i. Step 10, 13~15 to create "Program" app, models & CR route

### 30. Create "Cart" App & CRUD item from the cart
    i. Create "carts" app (see step 10)
    ii. Create "C" Cart Route to add program to cart (see step 15 & NOTE need the argument program_id)
    iii. Create "R" view cart route (see step 14 & NOTE need have cart array [] in view function)
    iv. Create "D" items route from cart (see step 17 & NOTE to use cart = request.session["shopping_cart"])
    v. Create "U" items route on cart (see step 16 & NOTE to use cart = request.session["shopping_cart"])

### 31. Setting up Cloudinary for Uploading images 
    i. Sign up <a href="https://cloudinary.com">Cloudinary</a>
    ii. Save the cloud name, API Key & API Secret in .env file. 
    NOTE : Ensure we did inclulde `.env` in `.gitignore`
    iii. At Gitpod terminal, enter : 
            * `pip3 install cloudinary`
            * `pip3 install python-dotenv`
    iv. Inside "settings.py", add 
            * `from dotenv import load_dotenv`, which instruct Django to load the environment file
            * `load_dotenv(os.path.join(BASE_DIR, '.env'))` tell Django where is the .env file located
            * Register the cloudinary app in the INSTALLED_APPS list
            * At bottom of "setting.py", add the following to retrieve the cloud info from the .env file
                    ```
                        CLOUDINARY = {
                            'cloud_name': os.environ.get("CLOUDINARY_CLOUD_NAME"),
                            'api_key': os.environ.get("CLOUDINARY_API_KEY"),
                            'api_secret': os.environ.get("CLOUDINARY_API_SECRET"),
                        }
                    ```
    v. Runserver, go to admin site, delete all dgs
    vi. At "dgs/models.py" :
            * import `from cloudinary.models import CloudinaryField`
            * insert `cover = CloudinaryField()` inside Dg model
    vii. At Gitpod terminal, makemigrations & migrate & testing at backend admin site
 
### 31. Allow user to "CR" images  
    i. At "dgs/forms.py" :
            * import `from cloudinary.forms import CloudinaryJsFileField`
            * add in "cover" inside the form's fields.
            * insert `cover = CloudinaryJsFileField()` at the end of the class Form & ensure its align with the `class Meta:`
    ii. Upgrade <a href="https://code.jquery.com/">jQuery CDN</a> minified version by replacing the jQuery <script> inside base.template.html
    iii. At "dgs/create_dg.template.html" : 
            * load `{% load cloudinary %}` & `{% load static %}`
            * use `enctype="multipart/form-data" id="form"`
            * Code JQuery script  
    iv. At display template, load {% load cloudinary %} & insert {% cloudinary dg.image %} to show the image 

    