# OscarApiExtension
This package provides an extension for the oscar api

### Usage
To use this application, follow these steps:

1. Clone the repo `git clone https://github.com/NerdPraise/OscarApiExtension.git`

2. Install the required packages `pip install requirements.txt -r`

3. Add a .env file with the key "DJANGO_SECRET_KEY" and the value a random secret key

4. Run `python manage.py runserver`

5. Using Post Man, `localhost:8000/users/userapi/` 

    To **GET** the all registered users    
        set to GET, `localhost:8000/users/userapi/` go to url   
            
    To **register** a new user,  
            POST the payload {
            "username":"",
            "first_name":"",
            "last_name":"",
            "email":"",
            "password":""
            } to the above url 
PS: always remember to put the trailing backslash