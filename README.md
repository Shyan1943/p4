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
    ii. In the file *setting.py*, install the app & save 
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
    i. Create static folder, which must be in the same folder as the project folder
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