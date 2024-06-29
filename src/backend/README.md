This is a simple example Flask application that uses an MVC type approach to develop APIs running on a Flask server. 

# To set up and run:

Create a vitrual python envrionment: ```python -m venv .venv```
Start virtual environment: ```.venv\Scripts\Activate.ps1```
Install Packages: ```pip install -r requirements.txt```
Run Flask server: ```py server.py```

# To make API requests:

POST http://127.0.0.1:5000/users
Request Body:
{
  "name": "John Doe",
  "email": "john@example.com"
}
GET http://127.0.0.1:5000/users
GET http://127.0.0.1:5000/users/<user_id>
