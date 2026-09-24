from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'give api key here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] != 200:
        return "Error: " + data['message']

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    return render_template('result.html', city=city, temperature=temperature, humidity=humidity, description=description)

app.run(debug=True)