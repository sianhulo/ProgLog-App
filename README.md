# ProgLog-App
A project created using Flask and the MVC pattern. 

## Requirements:
- [x] Python (Version 3).
- [x] Pip.
- [x] PostgreSQL.
- [x] Git.


## Instalación.

1. **Set up the repository locally.**
 - Run the following command:
   
   `$ git clone https://github.com/germmand/ProgLog-App.git`
  
 - `cd` into the folder created:
   
   `$ cd ProgLog-App/`


2. **Set up the virtual environment.**

 - As a suggestion, we recommend using [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/).
   Check out its documentation on how to install it, create it and activate it.

3. **Install dependencies.**

 - Once the virtual environment has already been activated, use the following command:
 
   `$ pip install -r requirements.txt`


4. **Update the configuration environments.**

 - Inside the `app` folder, make a copy of `.settings-TEMPLATE.py` removing the `-TEMPLATE` suffix from that new file.
 
 - Open the file and update the `SQLALCHEMY_DATABASE_URI` with its respective fields.
   * Username.
   * Password.
   * Host.
   * Port.
   * DBName.

 - Update the Cross-site request forgery session key and secret key.
   * CSRF_SESSION_KEY.
   * SECRET_KEY.
   
5. **Run the migrations.**

 - Run the following commands:
 
   `$ flask db upgrade`

6. **Run the server.**

 - In the project's root, run the command:
 
   `$ flask run`.

**OPTIONAL**
- To enable debug mode, add `FLASK_ENV=development` to the environment.

:+1:
