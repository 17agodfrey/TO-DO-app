# TO-DO App – Utah Valley University Assessment

## Overview
This is a Django-based TO-DO application created for the **Utah Valley University Proficiency Assessment**.

## Setup
Followed Instructions in Django Proficiency Assessment - TO-DO app.pdf. Dependencies are listed in requirements.txt, but I will also list them here: 

asgiref==3.9.1
Django==5.2.4
django-widget-tweaks==1.5.0
sqlparse==0.5.3
tzdata==2025.2

After cloning repo, to setup run: 
```bash
cd TO-DO-app
python -m venv .venv              
.venv\Scripts\activate        
pip install -r requirements.txt
python manage.py migrate

```

## Run
To start the development server:

```bash
python manage.py runserver
