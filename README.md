GrandPy is a small Flask application that acts as a bot.

You put in the search field the place you're looking for and as a response and if it's found, you're being given the address of that place followed by a map locating it.

Then, a short description of that place is provided.

Actually, the application uses two APIs to perform those tasks:
- Google Maps is required to find the place and displaying the map.
- Then Mediawiki is used to get a short story of the place.

The hosted application can be accessed by the following link: https://grandpy-ebres.herokuapp.com

The application is developped with:
- Flask 1.1.1
- Python 3.7.6

Install guide
First step is to get the repository to your machine. 

For that, type in the following from your console:
- git remote add GP https://github.com/6netic/GrandPy.git
- git clone https://github.com/6netic/GrandPy.git

It's adviced to work in a virtual environment.

After being activated, go to the root of the repository and install the requirements by typing in the console:
`pip3 install -r requirements.txt`

Then, you need to create an environment file called .env in which you will store environment variables in the root of the repository.

In our application, we have two of those variables.

The first one is the application key. For example, you can generate one on:
https://miniwebtool.com/django-secret-key-generator/

The second one is your Google API key.

The following link explains how to get one if you don't have it yet:
https://developers.google.com/maps/documentation/embed/get-api-key
So, the .env file should look like that:

`export SECRET_KEY = "YOUR_KEY_APP_KEY" `

`export GOOGLE_API_KEY = "YOUR_GOOGLE_API" `

Once done, to launch the app, just type in:

`python3 run.py`

And open your web browser at : 

http://localhost:5000 to see it work.

