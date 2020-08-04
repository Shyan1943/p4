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
