# URL_Shortener

SHORTLINK

About
---
ShortLink provides a simple and convenient way to shorten URLs and retrieve the original long URL from the short URL.

The `encode` function takes a long URL as input and generates a short URL with the format of "http://short.est/" plus a random string of characters (lowercase and uppercase letters and digits) of length 4 to 8. If the long URL already exists in the database, the function returns the corresponding short URL. Otherwise, it generates a new short URL and saves the new URL entry to the database.

The `decode` function takes a short URL as input and retrieves the corresponding long URL from the database.


Getting started:
---
1. Clone the repository:
  git clone https://github.com/LReva/URL_Shortener.git
2. Create a virtual environment:
  python3 -m venv .venv
3. Activate the virtual environment:
  source .venv/bin/activate
4. Install the required packages:
  pip install -r requirements.txt
5. Create a .env file in the root directory of your project and add your project's environment variables:
  SECRET_KEY = django-secret-key-here
6. Create a new database with the name url_db:
  psql postgres;
  CREATE DATABASE url_db;
7. Apply the migrations:
  python manage.py migrate


User guide:
---
1. Start by running the Django server. Open a terminal window, navigate to the project directory (the directory that contains the manage.py file) and run the following command:
  python manage.py runserver
2. Once the server is running, open a web browser and navigate to http://localhost:8000. This will take you to the home page of the app.
3. Select what action you want to perform: encode or decode.
4. To encode a long URL, enter the URL in the input field on the home page and click the "Encode" button. This will send a POST request to the /encode/ endpoint and return a JSON response with the corresponding short URL.
![Screenshot from 2023-05-09 17-50-56](https://github.com/LReva/URL_Shortener/assets/121891752/d516c7bf-c9a5-44a9-ba80-8c4533093aef)
![Screenshot from 2023-05-09 17-51-04](https://github.com/LReva/URL_Shortener/assets/121891752/7870647e-3acf-4589-a9a6-7fbcebb7b695)

5. To decode a short URL, enter the URL in the input field on the home page and click the "Decode" button. This will send a POST request to the /decode/ endpoint and return a JSON response with the corresponding long URL.
![Screenshot from 2023-05-09 17-51-24](https://github.com/LReva/URL_Shortener/assets/121891752/a6966836-855f-438b-b734-c7ad0d09b4d8)
![Screenshot from 2023-05-09 17-51-32](https://github.com/LReva/URL_Shortener/assets/121891752/8369dc5c-3858-4e9c-bc92-2bbda4511272)