import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    user_data = requests.get('http://localhost:5000', timeout=2)
    recommender_data = requests.get('http://localhost:5001', timeout=2)

    return """
<html>
  <body>
    <h1>Hi %s!</h1>
    <h2>Your recommendations: %s</h2>
  </body>    
</html>
""" % (user_data.json()['name'], ', '.join(recommender_data.json()['categories']))


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=8080)
