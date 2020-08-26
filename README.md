# DGExpect
View the live project <a href="https://shyan-tgc-pro4.herokuapp.com/" >here</a>.

This is a Free <b><u>Dangerous Goods</u></b>, (hereafter known as <b><i>"DG"</i></b>) Public Q&A site and we promote training program.  

<strong>Purpose:</strong>
* In this project, I build a full-stack site based around business logic used to control a centrally-owned dataset. I set up an authentication mechanism, provide a Free Public Q&A platform and paid access to the site's training program.

<strong>Value provided:</strong>
* By authenticating on the site, users can enjoy the free <b><u>Create, Read, Update & Delete</u></b>, (hereafter known as <b><i>"CRUD"</i></b>) Public Q&A and give review. To advance users' own goals, users paying for training program to upgrade their skill. Before authenticating, the site makes it clear how those goals would be furthered by the site. 
* The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without singup or paying.

<a href="https://shyan-tgc-pro4.herokuapp.com/" target="_blank"><img src="static/images/introduction.png" alt="Ask or give Dangerous Goods Public Q&A or review site. Or you can choose to upgrade your skill by signup our training programs."/></a>


# User Experience - User Interface (UX-UI)
## 1) STRATEGY
* <strong>External user’s goal: </strong>To join a DG Public Q&A community and purchase training program

* <strong>Site owner's goal : </strong>
    * Build an active community discusssion site around the product based on site admin or users free signup to CRUD Q&A and review 
    * Sell DG Training program 

* <strong>Target audience : </strong>
    * Consumer-to-business 
    * Traveller, Trader, Career change, airport or seaport staff & Freight Forwarder

* <strong>Therefore, the site should focus on :</strong>
    * Community
        ```
            ● Design a front end for a full stack application following the principles of UX design which meets accessibility guidelines, is easy to navigate and allows the user to ﬁnd information and resources intuitively
            ● Design a full stack application that lets the user initiate and full control actions and gives immediate and full feedback on information
            ● Implement a full stack application whose purpose is immediately evident to a new user and which provides a good solution to the user’s demands and expectations
            ● which has a clear, well-deﬁned purpose addressing the needs of multiple related target audiences
            ● Free Public Q&A & reviews 
            ● All CRUD actions are immediately reﬂected in the user interface
        ``` 
    * E-commerce
        ```
            ● Authentication and authorisation mechanism for user and administrators
            ● A puchase payment model
        ```

## 2) SCOPE
### Identifying External Users:
* The primary purpose of this site is to allow users to share their experience, problem facing or any inquire about handling of DG product. and benefit from having convenient access to the information provided by all other members. The person may be the <b><u>site owner, traveller, trader, people seek for career change, airport or seaport staff & Freight Forwarder</u></b> (hereafter known as <b><i>"EXTERNAL USERS"</i></b>). 

### Identifying Site Owner:
* The site owner advances their own goals by providing this functionality, potentially by being a regular external user themselves. The site owner also benefit from the collection of the dataset as a whole and program training fee. 

### 2a) User Stories 
```
    ● US1. As an external user, I want to get the information easily within few clicks, so that I get what I wanted as soon as possible. 
    ● US2. As an external user, I want to visit a responsive website, so that I can surt the net at anytime anywhere easily without rely on computers.
    ● US3. As an external user, I want to visit a good user interactive website, so that i feel it is a trustworthy website to fish information. 
    ● US4. As an external user, I want to get the information easily within a particular domain, so that it save my memory & time. 
    ● US5. As an external user (Traveller), I want to have more information or suggestion on certain product, so that I know whether should I buy it during travelling.  
    ● US6. As an external user, I want to have a "any keyword" search engine, so that I can find the information easily.
    ● US7. As an external user, I want to share my experience, problem facing or any inquire about handling of DG product within the particular domain, so that I have a clear picture what to do next.
    ● US8. As an external user, I want to share my knowledge for those who needs by giving reviews, so that I can improve myself at the same time. 
    ● US9. As an external user, I want my post or review can be updated or deleted anytime by myself, so that I can do any adjustment immediately. 
    ● US10. As an external user, I want to upgrade my DG knowledge & handling skill, so that I can reach next level in my career path or career change. 
    ● US11. As an Site Onwer, I want to collect data information through this site, so that I can develop it to other businesses in future. 
    ● US12. As an Site Onwer, I want to have a program sign up section, so that I can sell my program and the payment transaction complete through the site.
```

### 2b) Functional Requirement (FR)					
| User Stories | FR |	Functional Requirement (FR)  |			
|     :---:    |     :---: |:---       |					
| US1 |	FR1 |	FixedTop Navigation that all resources are easy to find, allowing users to navigate the layout of the site intuitively.   |	
| US2 |	FR2 |	Responsive design  |	
| US6 |	FR3 |	Search Engine by input any keyword or IMDG Code category  |	
| US7 & 9 |	FR4 |	Allow users to CR Public Q&A to share their experience, problem facing or any inquire about handling of DG product & related image |	
| US8 & 9 |	FR5 |	Allow users to CR Review to share their knowledge & experience for giving help to those who needs |	
| US7 ~ 9 |	FR6 |	Only allow the same users to see, click & access UD button for their own Public Q&A & Review |	
| US11 | FR7 |	Allow users to free sign up, identify and apply authorisation, authentication and permission features for Site Onwer to collect user data information |	
| US12 | FR8 |	Allow users to purchase training program on site |  
| US12 | FR9 |	Only allow the Site admin to see, click & access CUD button for programs site |	

### 2c) Content Requirement (CR)			
| User Stories | CR |	Content Requirement (CR)  |			
|     :---:    |     :---: |:---       |			
| US3 |	CR1 |	User interactions design  |	
| US4 |	CR2 |	A short & quick introduction to attract more users to CRUD their experience, inquiry & review  |	
| US5 |	CR3 |	View Public Q&A + image & review section |	
| US6 |	CR4 |	Search Engine section |	
| US7 & 9 |	CR5 |	CRUD Public Q&A section  |	
| US8 & 9 |	CR6 |	CRUD Review Section  |	
| US10 |	CR7 |	"R" View program section   |	
| US11 |	CR8 |	Authentication and authorisation mechanism for users and administrators section |	
| US12 |	CR9 |	Shopping cart & payment section   |	
| US12 |	CR10 |	CUD program section   |


## 3) STRUCTURE				
### 3a) Information Architecture				
#### Image required				
Image required on the website to fulfill the content requirements.				
| US |	CR |	CI |	Content Inventory (CI)  |	
|     :---:    |     :---: |     :---:    |:---       |	
| US4 |	CR2 |	CI1 |	Site introduction image  |	
				
#### Content Inventory (CI)				
Information required on the website to fulfill the content requirements.				
				
| US |	CR |	CI |	Content Inventory (CI)  |	
|     :---:    |     :---: |     :---:    |:---       |	
| US4 |	CR2 |	CI2 |	A nice & short sentences to introduce the site  |	
| US5 |	CR3 |	CI3 |	"R" View all Public Q&A with image section |	
| US5 |	CR3 |	CI4 |	"R" View a Public Q&A details with image & its' reviews section |	
| US6 |	CR4 |	CI5 |	Search (Any keyword & IMDG Code category) Engine section  |	
| US6 |	CR4 |	CI6 |	Result section for Search Engine to show all programs & related Public Q&A Topic  |	
| US7 & 9 |	CR5 |	CI7 |	"CUD" Public Q&A & image section  |	
| US8 & 9 |	CR6 |	CI8 |	"CUD" Review section  |
| US10 | CR7 |	CI9 |	"R" View all programs section  |	
| US10 | CR7 |	CI10 |	"R" View a program with full details section  |	
| US11 | CR8 |	CI11 |	Sign up section  |
| US12 | CR9 |	CI12 |	"R" View Shopping cart & payment section  |
| US12 | CR10 |	CI13 |	Site admin to CUD a program details section  |	

#### Content Structure (CS)
In these modern days, users are constantly bombarded with too much content, people love simplicity. With this, we design it as a "One-page websites" offer a fast and clear reading experience. The contents will be regroup into a sequential structure as below IA Sitemap for landing Page & overall. 

<img src="static/images/iasitemap_landingpage.png" align="left" width="130px" height="420px"/>

##### Landing Page :
```
CI2.	The landing page starts with a nice & short sentences allow visitor perceive briefly of what is the site related to 
FR1.    as well as clickable buttons at the center of the landing page allowing users to navigate the layout of the site intuitively	
```			
##### Introduction section :  			
```			
CI1.    Site introduction image allow visitor insight into the site functionality
CI2.    Short Introduction are given to each image allow visitor to more understand the site a little better
	
```			
##### Search Engine section :  			
```			
CI5.	Search Engine section	
CI6.    Search Engine result section will always return all programs to promote Site owner product
CI6.    Search Engine result section will return related Public Q&A Topic or return all when Search Engine leave blank	
```

#### IA Sitemap (Overall)
<img src="static/images/iasitemap_overall.png">

#### Database Structure
##### Entity Relationship Diagram (ERD)
This ERD  is relevant on this particular domain, consisting of Six Django models (User, Dg, IMDGCode, Review, Program, Purchase), where build a Django ﬁle structure that is consistent and logical, following the Django conventions
<img src="static/images/data_erd.png">

#### Data model
##### Logical Diagram
There are 5 set of forms with validation that will allow users to records in the database (in addition to the authentication mechanism).
* Search form for all visitors to search (Any keyword & IMDG Code category) at the Search Engine section
* accounts SignupForm for user to register account with the Site
* CUD Dgs (Public Q&A) forms for user to share their experience, problem facing or any Dg inquire
* CUD Review forms for user to give review to a particular Dgs (Public Q&A) post 
* CUD Program forms ONLY allow Site admin access to CUD program
<img src="static/images/data_logicaldiagram.png">

### 3b) Interaction Design      	
#### Learnability	
      i.	Different navigation are positions at the familiar location a web surfer, and throughout the website to enhance familiarity and consistency. (FR1)
            a.	Logo that leads back to the home page
            b.	navigation system in the all pages of site map allowing visitor to view all the sections at a glance
            c.  a clear and unambiguous navigation structures to <a href="http://www.flaskboilerplate.com/" target="_blank">fixed at the top</a>
            d.	all resources on the site are easy to ﬁnd, allowing users to navigate the layout of the site intuitively
            e.  4 clear navigation buttons at the right of the landing page center 
      ii.	Button with hover effect will be used to indicate there's a link to the working project to increase the predictability.
      iii.  Users who direct to a non-existent page or resource are redirected back to the main page without having to use the browser navigation buttons

#### Understandability	
      i.	Content are group into logical order with short word or phrase title easily understandable 
      ii.	Readability (Flesch Kincaid Reading Ease Test = 73.7, Flesch-Kincaid Grade Level Score = 4.5)       

#### Operability	
      i.	The visitors can simply key in any word or choose a related IMDG Code at the Search Engine to search for the related Public Q&A without encountering any issues. (FR3)
      ii.	Allow users to CR Public Q&A to share their experience, problem facing or any inquire about handling of DG product & related image (FR4)
      iii.	Allow users to CR Review to share their knowledge & experience for giving help to those who needs (FR5)
      iv.   Allow users to purchase training program on site (FR8)
#### Attractiveness	
      i.	Responsive design to take into consideration how it looks when on viewed on a desktop browsers as well as smaller screens like mobile phone. The layout will change to cater for different size of the device. (FR2)
      ii.	Utilization of negative space between different sections and components of the page to increase readability
      iii.  Allow users to free sign up, identify and apply authorisation, authentication and permission features for Site Onwer to collect user data information (FR7)
#### Usability compliance	
      i.	Semantic HTML to enhance code readability 
      ii.	Rearrangement of the component 
      iii.	Used of <a href="https://docs.djangoproject.com/en/3.1/ref/contrib/messages/" target="_blank">Django flash message framework</a> allows us to temporarily store messages in one request and retrieve them for display  a one-time notification message to the user after processing a form or some other types of user input.
#### Accessibility	
      i.	there is clear conformity to accessibility guidelines across all pages/sections and in all interactivity
      ii.	The <a href="https://v4-alpha.getbootstrap.com/getting-started/accessibility/">aria-label attribute</a> is used to define a string that labels the current element, in cases where a text label is not visible on the screen. 
      iii.  Only allow the same users to see the UD clickable button & access UD for their own Public Q&A & Review (FR6)
      iv.   Only allow the Site admin to see, click & access CUD button for programs site (FR9)

### 3c) Defensive design
* Only allow the same users to see, click & access UD button for their own Public Q&A & Review (FR6)
* Only allow the Site admin to see, click & access CUD button for programs site (FR9)

## 4) SKELETON
### 4a) Interface design
<img src="/static/images/skeleton_mainlayout.png" align="left" width="200px" height="130px">

1. Each page will include two parts - header and main content to keep the consistency
2. Header include sections that will be repeated all the pages to improve predictability and consistency.
3. Fixed-top Header will include a logo and the main navigation 
4. The main content section will display content related to the page.

<br>

#### <u>Skeleton (Landing Page)</u>
<img src="/static/images/skeleton_landingpage.png">

#### <u>Skeleton CI3 (All dgs Public Q&A)</u>
<img src="/static/images/skeleton_ci3_all_dgs.png">

#### <u>Skeleton CI4 (details for a dgs Public Q&A)</u>
<img src="/static/images/skeleton_ci4_details_dg.jpg">

#### <u>Skeleton CI10 (details for a program)</u>
<img src="/static/images/skeleton_ci10_a_program.png">

#### <u>Skeleton (CUD & other forms)</u>
<img src="/static/images/skeleton_form.jpg">

### 4b) Navigation design 
If External User get lost, the navigation bar will point them in the right direction. Bootstrap component will be used to make the fixed-top navigation responsive.
```
Logo
● Logo on every page, clicking on it will bring the visitor to the Home Page. [Bootstrap Component - Navbar] 

Main Navigation
● Main Navigation is a fixed position menu at the top of every web page. It designed for External User's convenience from one page to another easily. They are hyperlinked to their respective pages. There is hover function too, so users know its clickable when mouse over. [Bootstrap Component - Navbar] 

Collapsible Hamburger Mobile Menu
● The top navigation will be minimized into a hamburger menu when displayed in mobile screens or other small screens. Clicking on it will display the familiar 3 choices. [Bootstrap Component - Navbar] 

Button for "Create", "Explore", "Upgrade" & "Search" 
● Place it at the right center of the landing page 
● It also can easily get it from the navigation bar, which will point external users to the right direction. 

Button for "Update", "Delete" & "CUD program"
● Update & delete icon will be showed on every id object, but only the same user able to see, click & access it. 
● CUD program icon will be showed on every id object, but only the Site admin able to see, click & access it. 
```

#### 4c) Information Design
##### Site Branding
A brand is the set of expectations, memories, stories and relationships that, taken together, account for a consumer's decision to choose one product or service over another. Here are the key design elements we use to create a brand identity that is strong, consistent, and attractive. 

      (CI1) Site introduction images to be displayed at the landing page, which can build an emotional connection with the External User.
      (CI2) Clear brand purpose and positioning
      (CI2) Memorable brand "DGExpect" also is created to make an impression.
      (FR1) Good navigation is key to attracting the External User, show them we care about their feeling, even just a single movement on the webpage. We do not want them to get lost. 
      (FR2) A Modern Responsive Web Design will tell External User that the platform is ahead of others, a free flexible and free advertisement Shipping platform
            (CS) One-page websites
            (FR2) Responsive design
            (FR3) Search Engine function
            (FR4~FR7) CRUD for any members at zero cost
      (5. Surface Color) Attractive color palette 
      (5. Surface Font) Professional typography 
      (5. Surface Image) A modern & energetic aesthetic image 

## 5) SURFACE
<img src="/static/images/surfacecolorpalette.png"> 

### Colour
The color palette keep at simple, with only 1–3 primary colors. In this website, the site logo is dark blue #3b464f, so I will choose Yellow and light blue to neutral it. 

### Typography
Font-Family <a href="https://fonts.google.com/specimen/Open+Sans?category=Sans+Serif&selection.family=Open+Sans:wght@600&sidebar.open=true" target="_blank">“Sans serif”</a> are chosen as the most famous fonts are recognizable even when taken out of context. A single primary typeface to lead the brand identity design, and it also work well with the branding and color palette. And giving the image of being modern, approachable, and clean. 
CSS rules to specify families font-family: 'Open Sans', sans-serif;
Open Sans Semi-bold 600 `<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap" rel="stylesheet">`

### Imagery
The 3 "Site introduction" images selected aims to build an emotional connection with External User, tell them what can they do with the site, as well as Illustrations strengthen the branding.


# FEATURES
### Ease of navigation (FR1)
      Feature 1. Allow the External User to view all the sections at a glance and from one page to another easily by having the fixed-top position navigation system (FR1)
      Feature 2. Allow the External User to search by any keyword or IMDG Code category straightaway, by having “Search” button at the Center of the Landing page and hyperlink it to “Search Engine & Result” section directly. (FR3, CI5 & CI6) 
      Feature 3. Users who direct to a non-existent page or resource are redirected back to the main page without having to use the browser navigation buttons and error notification message given. 

### Responsiveness (FR2)
      Feature 4. Allow the External User to view the platform with all devices, like desktop, laptop, tablets and smart mobile phones. It can be view in both portrait and landscape orientation as well by implement the responsive design. (FR2) 

### User interactions design (CR1)
      Feature 5. Hover effect "enlarge & shadow of button" on all the clickable button/hyperlinks to provide results in a manner that is visually appealing and user friendly
      Feature 6. Graphical elements like images, typography and icons are used to replace the words to communicate information to users 
      Feature 7. Used of <a href="https://docs.djangoproject.com/en/3.1/ref/contrib/messages/" target="_blank">Django flash message</a>  framework allows us to temporarily store messages in one request and retrieve them for display a one-time notification message to the user after processing a form or some other types of user input.

### Consistency and predictability (CR1)
      Feature 8. Allow the External User to stay clear and easy find the same components position at the same place regardless of which page they are at by having the header and theme stay consistent throughout the site. 

### Before Signup --> View all Dg Public Q&A, reivews & programs section (CR
      Feature 9. Allow the External User to know the current popular Public Q&A topic (CI3)
      Feature 10. Allow the External User to know more about how to handling DG goods (CI4) 

### Signup at Zero cost 
      Feature 11. Allow users to free sign up, identify and apply authorisation, authentication and permission features for Site Onwer to collect user data information (FR7)

#### CR Public Q&A & Review section
      Feature 12. Create the back-end code and front-end form(s), which allow external users to create & display Public Q&A records. (FR4)
      Feature 13. Create the back-end code and front-end form(s), which allow external users to create & display review records. (FR5)

#### Purchase program section 
      Feature 14. Allow users to purchase training program on site. (FR8)
      Feature 15. Implemented a feedback system that reports successful and unsuccessful purchases to the user, with a helpful message. And redirect users back to shopping all programs page.

#### Authentication mechanism 
      Feature 16. Only allow the same users to see, click & access UD button for their own Public Q&A & Review (FR6)
      Feature 17. Block different users to access others' UD Public Q&A & Review site if they try to access it by through url (FR6)
      Feature 18. Only allow the Site admin to see, click & access CUD button for programs site (FR9)
      Feature 19. Block users to access CUD Program site if they try to access it by through url (FR9)

#### Backend Data Collection (FR7)
      Feature 20. Used of <a href="https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/" target="_blank">Django postgres </a> to collect data information through this site "Backend" (FR7) 

### Security Features
      Feature 21. The <.gitignore> file was created for the purpose of preventing files, environment variables, any passwords or security sensitive information, from being uploaded without needing to explicitly exclude them. Any file added to the gitignore will never be included in git commits. Not only does this feature allow for system-specific files to be untouched, but it allows for insurance that sensitive files will never be uploaded. 
        
## Features Left to Implement
      Feature 22. Allow external users to choose whether update image or not 
      Feature 23. Show purchase receipt after payment successfully


# TECHNOLOGIES USED  
## requirements.txt
```
cloudinary==1.22.0
dj-database-url==0.5.0
Django==2.2.6
django-allauth==0.42.0
django-crispy-forms==1.9.2
gunicorn==20.0.4
oauthlib==3.1.0
Pillow==7.2.0
psycopg2==2.8.5
python-dotenv==0.14.0
python3-openid==3.2.0
pytz==2020.1
requests-oauthlib==1.3.0
sqlparse==0.3.1
stripe==2.50.0
whitenoise==5.2.0
```

## Technologies, Frameworks, Libraries & Programs Used 
### Preparation
1) <a href="https://fonts.google.com/specimen/Open+Sans?category=Sans+Serif&selection.family=Open+Sans:wght@600&sidebar.open=true" target="_blank">Google Font</a> to making the web more beautiful, fast, and open through great typography 
2) <a href="https://www.sessions.edu/color-calculator/" target="_blank">Sessions College color calculator</a> to find the perfect color scheme 
3) <a href="https://www.freepik.com/" target="_blank">Freepik</a> to get an high resolution image
4) <a href="https://pencil.evolus.vn/" target="_blank">Pencil Project </a>was used to create the wireframes during the design process.
5) <a href="https://erdplus.com/" target="_blank">ERDPlus </a> to design the database structure, Entity Relationship Diagram (ERD)
6) <a href="https://sqldbm.com/Home/" target="_blank">SQLDbm</a> to design the data model, Logical Diagram

### Production (Coding)
7) Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
8) <a href="https://github.com/" target="_blank">Github</a> for Versioning Control System and GitHub for repositories to store the projects code after being pushed from Git.
9) <a href="https://www.gitpod.io/" target="_blank">Gitpod</a> for code editor redefined and optimized for building and debugging modern web 
10) <a href="https://www.w3schools.com/html/html_intro.asp" target="_blank">HTM5</a> to structure the webpages
11) `.gitignore` file is used for the purpose of preventing files, environment variables, any passwords or security sensitive information, from being uploaded without needing to explicitly exclude them. Any file added to the gitignore will never be included in git commits. Not only does this feature allow for system-specific files to be untouched, but it allows for insurance that sensitive files will never be uploaded. 
12) <a href="https://docs.djangoproject.com/en/3.1/ref/contrib/messages/" target="_blank">Django flash message</a>  framework allows us to temporarily store messages in one request and retrieve them for display  a one-time notification message to the user after processing a form or some other types of user input.
13) `pip3 install cloudinary` to install <a href="https://cloudinary.com/" target="_blank">Cloudinary</a>, which use to efficiently create, manage, and deliver images, personalized and optimized for every device and channel.
14) `pip3 install python-dotenv` -- allows the use of `.env` files for environment variables
15) <a href="https://www.w3schools.com/js/" target="_blank">JavaScript</a> to CRUD Cloudinary profile as image 
16) `pip3 install stripe` to install <a href="https://stripe.com/en-sg" target="_blank">Stripe Payment</a> to implement Django app containing e-commerce functionality online payment processing system. We use the single payments method on this Site. 

### Production (Styling)	
19) <a href="https://getbootstrap.com/docs/4.4/getting-started/introduction/" target="_blank">Bootstrap 4.4.1</a> was used to assist with the responsiveness and styling of the website.	
20) <a href="https://www.w3schools.com/css/css_intro.asp" target="_blank">CSS3</a> to style HTML contents	
21) <a href="https://getbootstrap.com/docs/4.4/components/navbar/" target="_blank">BootStrap </a>to fix top & responsive navigation bar
22) <a href="https://getbootstrap.com/docs/4.0/utilities/flex/#justify-content" target="_blank">Bootstrap ml-auto or mr-auto</a> to fix navigation menu to the right or left
23) <a href="https://www.w3schools.com/html/html5_semantic_elements.asp" target="_blank">Semantic Elements</a> use in HTML to clearly describes its meaning to both the browser and the developer.
24) Hover.css was used on all clickable icons while being hovered over.	
25) <a href="https://getbootstrap.com/docs/4.4/components/jumbotron/" target="_blank">Jumbotron </a>to extend the entire viewport at profile advertisement section
26) <a href="https://getbootstrap.com/docs/4.0/utilities/spacing/" target="_blank">`mx-auto`</a> and <a href=https://getbootstrap.com/docs/4.3/components/card/ target="_blank">Bootscrap Card</a> to fix Ads Profile Card responsive	
27) <a href="https://bootstrap-table.com/docs/getting-started/introduction/" target="_blank">bootstrap-Table</a> for An extended table to the integration with some of the most widely used CSS frameworks. 	
28) `target="_blank"`to improve the UX, when user click on any link out (to another web site or social site), that opens a new window. 	
29) <a href="https://fontawesome.com/v4.7.0/icons/" target="_blank">Font Awesome Icons </a>are used on all pages throughout the website to add icons for aesthetic and UX purposes to represent accessibility standards

### Publication 	
30) <a href="https://heroku.com/" target="_blank">Heroku</a> to deploy, manage, and scale modern apps, to getting our apps to market.	
31) `pip3 install gunicorn` to install <a href="https://gunicorn.org/" target="_blank">Gunicorn</a> to run Python application concurrently by running multiple Python processes within a single dyno	
32) `pip3 install psycopg2` to install <a href="https://pypi.org/project/psycopg2/" target="_blank">psycopg2 driver</a>, which is a popular PostgreSQL driver developed for use with the Python programming language
33) `pip3 install Pillow` to install <a href="https://pypi.org/project/Pillow/" target="_blank">Pillow</a>, which is the Python Imaging Library
34) `pip3 install whitenoise` to install <a href="https://pypi.org/project/whitenoise/" target="_blank">whitenoise</a>, which allows web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service.
35) `pip3 install dj_database_url` to install <a href="https://pypi.org/project/dj-database-url/" target="_blank">dj_database_url</a> which returns a Django database connection dictionary, populated with all the data specified in URL.
36) <a href="https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/" target="_blank">Django Postgres</a> database, which has the richest feature set of the supported databases so its users have the most to gain. 

### Documentary	
37) <a href="https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md" target="_blank">Code Institute Readme.md template</a> for Readme file report guideline 	


# TESTING
## Tested with no error
| Testing on   | Result |
|:--|:--|
| <a href="http://validator.w3.org/" target="_blank">HTML Checker</a> | "Document checking completed. No errors or warnings to show."|
| <a href="https://jigsaw.w3.org/css-validator/" target="_blank">W3C CSS Validator</a> | "TextArea (CSS level 3 + SVG). Congratulations! No Error Found."|
| <a href="https://www.seoptimer.com/alt-tag-checker" target="_blank">Image</a> | "You do not have any images missing ALT attributes on your page"|
| <a href="https://color.a11y.com/Contrast/"  target="_blank">Color</a> | "Congratulations! No automated color contrast issues found on the webpage tested"|
| <a href="https://www.webfx.com/tools/read-able/" target="_blank">Readability</a> | "Your page has an average grade level of about 9. It should be easily understood by 14 to 15 year olds."|
| Python PEP& Style | No underline error message on gitpod | 
| Different browers | The website was tested on Google Chrome, Microsoft Edge and Safari browsers. | 
| US1 Navigation | Clicked on each of the navigation on every page and all pages were linking correctly. |
| US2 Responsiveness | The site can be viewed and used on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX and resolutions size from (1920x1200) till (320x480)|
| US6 Search function | Return with the right answer, no error found |
| US7 & 9 CRUD Public Q&A | Users able to CRUD their own Public Q&A. There are present and working |
| US8 & 9 CRUD Review | Users able to CRUD their own reviews. There are present and working |
| US10 Purchase | Users able to purchase a program & payment done within the Site |
| US11 Collect date | Site Owner manage to collect data at the backend POSTGRES Database |
| US12 CUD Program | Only Site Owner able to CUD program on the site | 

## Tested with errors result
```
1. Error message at browser inspect console
    Error found :  “GET /favicon.ico HTTP/1.1" 404 2674
    Corrective action : Insert `<link href="data:image/x-icon;base64,YourBase64StringHere" rel="icon" type="image/x-icon">`  in HTML head section
    Result : Every page checking completed. No errors or warnings to show on inspect console
```

# DEPLOYMENT
## A) PREPARATION	
### 1. Design	
* 	Design a good UI UX
* 	Design a database structure, Entity Relationship Diagram that is relevant for that particular domain, consisting of Six Django models (User, Dg, IMDGCode, Review, Program, Purchase) by using <a href="https://erdplus.com/" target="_blank">ERDPlus </a>
*	Design an assess functionality, usability and data management within the Full Stack web application by keep reference back to the user stories, functional & content requirement.
*	Design a data model, a logical diagram that ﬁts the purpose of the project by using <a href="https://sqldbm.com/Home/" target="_blank">SQLDbm</a> 
*   Design 5 set of forms with validation that will allow users to records in the database (in addition to the authentication mechanism).

### 2. Content	
* 	Choose font to be used 
* 	Fix color palette to be used 
* 	Find good images to be used 
* 	Find a suitable Font Awesome Icon 
* 	ensured file & name ﬁles consistently and descriptively, without spaces or capitalization to allow for cross-platform compatibility.

### 3. Before coding 	
*   Fixed Functional Requirement (FR)
*   Fixed Content Requirement (CR)
*	Fixed features 
* 	Understand the PEP8 style guide to ensure the use Python code that is consistent in style and conforms to the PEP8 style guide and validated HTML and CSS code.
*	Fixed Technologies to be used 

## B) PRODUCTION
### 1. Setting up Github Pages
    i. Sign up Github at https://github.com/
    ii. Log in to GitHub
    iii. Create a new GitHub Repository

### 2. Launch a workspace container at Gitpod
    i. Go https://www.gitpod.io/docs/browser-extension/, click to install Gitpod Browser Extension on browser in you are using Chrome or Firefox for convenient
    ii. Use `Ctrl+F5` on your Github Repository Page to refresh the browser
    iii. You will see a Gitpod button (Yellow color) is added to GitHub that does the prefixing for your convenience. And click on that button 
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

### Take note to deﬁne application URLs in a consistent manner

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
    i. Create a <Dg> model inside the "dgs/models.py" and use `date = models.DateField(auto_now_add=True)`
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
    ix. At template insert :-
            * `{% if request.user == d.user %} {% endif %}` to only allow the same user to click on the UD button for their post 
            * `{% if request.user.is_superuser %} {% endif %}`to only allow the superuser to click on the CUD for program

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
    ii. See step 13, to create `Review` models and use `date = models.DateField(auto_now_add=True)`
    iii. See step 15, to create "C"RUD Route for Reviews
    iv. See step 14, to create C"R"UD Route for Reviews
    v. See step 16, to create CR"U"D Route for Reviews and use path('update/<dg_id>/<review_id>') at reviews/urls.py
    vi. See step 17, to create CRU"D" Route for Reviews and use path('update/<dg_id>/<review_id>') at reviews/urls.py

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

### 28. Search engine
    i. See Step 10 to create new "home" app and set up it's url route 
    ii.  Create "home/forms.py", creata a SearchForm
    iii. Inside "home/views.py" :
            * import `from django.db.models import Q` 
            * Update the index view function to do the search
    iv. Create "home/home.template.html"
    v. At "home/urls.py" create home path

### 29. Create "Program" App, Model & CRUD
    i. See Step 10, 13~17 to create "Program" app, models & CRUD route
    ii See last step of Step 39 to set up permission for admin to access only 

### 30. Create "Cart" App & CRUD item from the cart
    i. Create "carts" app (see step 10)
    ii. Create "C" Cart Route to add program to cart (see step 15 & NOTE need the argument program_id)
    iii. Create "R" view cart route (see step 14 & NOTE need have cart array [] in view function)
    iv. Create "D" items route from cart (see step 17 & NOTE to use cart = request.session["shopping_cart"])
    v. Create "U" items route on cart (see step 16 & NOTE to use cart = request.session["shopping_cart"])

### 31. Show the number of cart items on every page
    i. Create a "cart/contexts.py" file and write a function to it. 
    ii. At "settings.py" insert `cart.contexts.cart_contents` to register the context_processors
    iii. Go "base.template.html" to show the number of cart items


### 32. Setting up Cloudinary for Uploading images 
    i. Sign up Cloudinary account at https://cloudinary.com
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
 
### 33. Allow user to "CRD" images  
    i. At "dgs/forms.py" :
            * import `from cloudinary.forms import CloudinaryJsFileField`
            * add in "cover" inside the form's fields.
            * insert `cover = CloudinaryJsFileField()` at the end of the class Form & ensure its align with the `class Meta:`
    ii. Upgrade jQuery CDN minified version at https://code.jquery.com/ by replacing the jQuery <script> inside base.template.html
    iii. At "dgs/create_dg.template.html" : 
            * load `{% load cloudinary %}` & `{% load static %}`
            * use `enctype="multipart/form-data" id="form"`
            * Code JQuery script  
    iv. At display template, load {% load cloudinary %} & insert {% cloudinary dg.image %} to show the image 
    v. At "dgs/delete_dg.template.html" to show the image & test on delete

### 34. Setup Stripe (online payment) settings
    i. On "https://stripe.com/en-sg" :
            * Sign up an account
            * Click on "Developers" on the left bar 
            * Click on "API Key"
            * Obtain the Stripe API Publishable & secret keys save it in .env file. 
    ii. Back to Gitpod, copy & paste the two keys and save in .env file.
        NOTE : Ensure we did inclulde `.env` in `.gitignore`
            ```
                export STRIPE_PUBLISHABLE_KEY='your_publishable_key'
                export STRIPE_SECRET_KEY='your_secret_key'
            ```
    iii. At Gitpod terminal, install Stripe by entering `pip3 install stripe`
    vi. At bottom of "setting.py", add the following to retrieve the Stripe keys from the .env file
            ```
                STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
                STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
            ```

### 35. Setup "Checkout" App for online payment 
    i. Create "Checkout" app (see step 10)
    ii. At "checkout/views.py" create a view function to generate the charge. NOTE import the following :- 
            ```
                `from django.contrib.sites.models import Site`
                `from django.conf import settings`
                `import stripe`
            ```
    iii. Create "checkout/checkout.template.html" and bring in Stripe Javastript 
    iv. At "checkout/urls.py" to set up the path

### 36. Empty the Cart after Checkout
    i. At "checkout/views.py", change the checkout_success function
    ii. use `request.session['shopping_cart'] = {}` to empty the shopping cart

### 37. Order Completion Webhook
    i. At checkout/views.py, create the new route & import the exempt_csrf decorator `from django.views.decorators.csrf import csrf_exempt`
    ii. set up its' checkout/urls.py 
    iii. test this URL in web browser. if error msg "HTTP_STRIPE_SIGNATURE", means in order, can continue the below steps.
    vi.  Go to https://dashboard.stripe.com/ site to create the endpoint :
            * click on "Add endpoint" at the right top
            * insert `<your url>/checkout/payment_completed`
            * At the Events to send dropdown, select `checkout.session.completed`
            * click on "Add endpoint" at below blue button
            * At "Signing secret" session, click "Click to reveal" & copy the endpoint secret 
            * Make sure to enable the endpoint before leaving the page.
    v. Add the endpoint secret to ".env" file and inform "settings.py" where to get it 
    vi. Create the handle_payment function
    vii. Test Checkout
    viii. At "checkout" app, create "Purchase" model, makemigrations, migrate, register it at admin.py to store the Purchase information 

### 38. Setting up Emails
* Sign up for a <a href="https://mail.google.com">Gmail account</a>
    * Click on the settings gear icon at the upper right corner
    * Click on the button [See all Settings]
    * Go to "Accounts & Import"
    * Click on "Other Google Account Settings"
    * Click on "Security" tab on the left bar and turns on two-step verification
    * click on "App Passwords"
    * Creating a new Mail App password 
    * Select "mail" under Select app, and "other" under Select device
    * When requested for a name, type in "django"
    * Save the 16-characters password and save it into .env file as EMAIL_HOST_PASS
* Back to Gitpod, update .env and settings.py file
* Try to get a <a href="https://temp-mail.org/en/">temp email</a> and use that to sign up as a new user for testing

### 39. User Group
* At Gitpod terminal, enter `django-admin startapp accounts` set up new "accounts" app 
* At Gitpod left bar, right click on "accounts" app to create new file "forms.py"
* At "settings.py", install 'accounts" app & insert `ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.SignupForm'`
* At "accounts/forms.py", create a SignupForm & test on broswer
* At "accounts/models.py", create a Profile model, makemigrations & migrate
* At "accounts/forms.py", import `from django.contrib.auth.models import Group` and add the user to group
* At "programs/views.py", insert as following for Site that not allow customer group to go in. 
    ```
    if request.user.groups.filter(name='customer').exists():
        messages.error(request, "You are not a Site administrator")
        return redirect(reverse(all_programs))
    ```

### 40. Static CCS styling
* Take note to check the site is responsiveness on every new styling input
* Import <a href="https://fonts.google.com/specimen/Open+Sans?category=Sans+Serif&selection.family=Open+Sans:wght@600&sidebar.open=true">Google Font</a>
* Added <a href="https://getbootstrap.com/docs/4.0/components/navbar/">Bootstrap fixed top navigation bar</a>

### 41. Create a new Site_ID 
* At Gitpod Terminal, enter : 
    * `python3 manage.py shell`
    * `from django.contrib.sites.models import Site`
    * `print(Site.objects.get(name='example.com').id)`, it will return a new Site_ID 
* At "settings.py", Change the 'SITE_ID' as what we can just now & save it 
* Test run `python3 manage.py runserver 8080` & login to /admin.

### 42. Handle error 404 
* At "home/views.py", create a error_404_view view function to handle 404 
* At "DGReviewsProject/urls.py", outside the urlpatterns, tell Django where is the handler404 view function
* At "DGReviewsProject/settings.py", change the DEBUG mode to False
* At Gitpod terminal, enter `python3 manage.py runserver 8080` to test run Django server 

## C) PUBLICATION
### Deploying to Heroku
* Implement manual test procedures to assess functionality, usability, responsiveness and data management within the Full Stack web application before publication
* Sign up for a <a href="https://www.heroku.com">Heroku</a> account
* Install dependencies, at Gitpod terminal : 
    * `pip3 install gunicorn`
    * `pip3 install psycopg2`
    * `pip3 install Pillow`
    * `pip3 install whitenoise` & go "settings.py" file, insert `'whitenoise.middleware.WhiteNoiseMiddleware'` into `MIDDLEWARE` Array
    * `pip3 install dj_database_url` 
* Update ".gitignore" file content as per this link http://gitignore.io/api/django
* At Gitpod terminal : 
    * log into Heroku using  `heroku login -i`
    * enter the email address & password for login to heroku
    * create a new app  `heroku create <app_name>` 
    * add new remote `git remote -v`
* Go to the <a href="https://www.heroku.com">Heroku</a> Site :
    * click on your project 
    * ciick on Setting
    * click on Reveal Config Vars
    * save all your environment variables (in .env file) into Reveal Config Vars
* At the folder, create a new file `Procfile`
* Save `web: gunicorn <PROJECT_FOLDER>.wsgi:application` inside the `Procfile`file
* At "settings.py", update ALLOWED_HOSTS with deployed url without https:// 
* At Gitpod terminal, generate requirements file `pip3 freeze --local > requirements.txt`
* At "settings.py", add `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` for Whitenoise to work 
* At Gitpod terminal : 
    * `git add .`
    * commit everything `git commit -m "<Commit Message>"`
    * push to heroku using `git push heroku master`

### Setting up the POSTGRES Database
* At Gitpod terminal : 
    * Enter `heroku config`
    * Copy down the DATABASE_URL & save it in `.env` file
* At "settings.py", import `import dj_database_url`. NOTE : after set the database to POSTGRES, We won't have access to old database unless revert the changes to orignal database setting
    * Configure the project efficiently through well-kept Procfile, requirements.txt file, settings files, keep the data store configuration in a single location where it can be changed easily.
* At Gitpod terminal : 
    * enter `python3 manage.py migrate` to migrate database
    * enter `python3 manage.py createsuperuser`to create a superuser as we have switched to a new POSTGRES database
    * enter `git add .`
    * enter `git commit -m "<Commit Message>"` to commit everything 
    * enter `git push heroku master` push to heroku 
* At Heroku Site : 
    * click on your project 
    * at the top left, cilck on "Open App" 
* Done publication!!
* Test to ensure it matches the development version 
* Ensure that ﬁnal deployed site has no broken internal links

### Ensure that Stripes still work
* Set up the url Sites correctly
    * Log into deployed site admin, go to Sites and edit the domain there to match heroku domain (with https:// in front and ending with a slash)
* Create new webhook endpoint with heroku url & SIGNING_SECRET at stripes.com
    * Add in a web hook with heroku app domain name for checkout.session.completed event. Make sure to set the signing key correctly.

### To update the Heroku deployed site
* At Gitpod terminal :
    * log into Heroku using  `heroku login -i`
    * enter the email address & password for login to heroku
* Update environment variables key (if any)
    * Go to the <a href="https://www.heroku.com">Heroku</a> Site
    * click on your project 
    * ciick on Setting
    * click on Reveal Config Vars
    * save all your environment variables (in .env file) into Reveal Config Vars
* At "settings.py", delete ["*"] at the ALLOWED_HOSTS 
* At Gitpod terminal : 
    * `git add .`
    * commit everything `git commit -m "<Commit Message>"`
    * push to heroku using `git push heroku master`
    * enter `python3 manage.py migrate` to migrate database (if we did update models.py before)
* Done publication!!
* Test to ensure it matches the development version
* Ensure that ﬁnal deployed site has no broken internal links


# CREDITS
## Content
1. Refer to <a href="https://github.com/Code-Institute-Solutions/SampleREADME#" target="_blank">Code Institute Readme.md sample</a> for Readme file report guidelines
2. All images are downloaded from <a href="https://www.freepik.com/" target="_blank">Freepik</a>.

## Code
1. Fixed font is chosed from <a href="https://fonts.google.com/specimen/Open+Sans?category=Sans+Serif&selection.family=Open+Sans:wght@600&sidebar.open=true" target="_blank">Google Font</a> to making the web more beautiful, fast, and open through great typography 
2. Refer to the notes took down during the lesson for coding
3. Refer to <a href=https://getbootstrap.com/docs/4.4/components/jumbotron/ target="_blank">Jumbotron</a> to extend the entire viewport at profile advertisement section
4. Refer to <a href="https://getbootstrap.com/docs/4.0/utilities/spacing/" target="_blank">`mx-auto`</a> and <a href=https://getbootstrap.com/docs/4.3/components/card/ target="_blank">Bootscrap Card</a> to fix Ads Profile Card responsive
5. Refer to <a href="https://bootstrap-table.com/docs/getting-started/introduction/" target="_blank">bootstrap-Table</a> for An extended table to the integration with some of the most widely used CSS frameworks. 
6. Refer to <a href="https://guides.github.com/features/mastering-markdown/" target="_blank">Github Markdown</a> to lightweight and easy-to-use syntax for styling all forms of writing on the GitHub platform.
7. Refer to <a href="https://github.com/twbs/bootstrap/issues/21885" target="_blank">style .card-deck to display: block</a> to fix the Bootstrap card display properly on Internet Explorer
8. Refer to <a href="https://stackoverflow.com/questions/9943771/adding-a-favicon-to-a-static-html-page" target="_blank">Stackoverflow</a> to fix the error msg at browser inspect console “GET /favicon.ico HTTP/1.1" 404 2674”
9. Refer to <a href="https://www.w3schools.com/html/html_formatting.asp" target="_blank">w3school HTML Text Formatting</a> to format the appearance of the text on web page
10. Refer to <a href="https://docs.djangoproject.com/en/3.1/topics/forms/" target="_blank">Django Documentation</a> to change the form display at the same row
11. Refer to <a href="https://css-tricks.com/almanac/properties/l/line-clamp/" target="_blank">The line-clamp property truncates</a> text at a specific number of lines.
12. Refer to <a href="https://docs.djangoproject.com/en/3.1/ref/forms/fields/" target="_blank">the empty_label attribute</a> to change the dropdown default text label from "---------" to what you like, or can disable the empty label entirely by setting empty_label to None  
13. Refer to <a href="https://docs.djangoproject.com/en/3.1/topics/http/views/" target="_blank">Django Returning errors 404 </a> to redirect error 404 back to the homepage & error notification message is given.  

# ACKNOWLEDGEMENTS 
I received inspiration for this project from : 

      1) Stackoverflow https://stackoverflow.com/ - on project idea
      2) Mr Paul Chor - Mentor of my course
      3) Mr John - Consultant of my project 
      4) Mr Donovan Lo - My classmate – on the Readme report  
