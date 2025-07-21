from flask import Flask, render_template, request, send_file, redirect, url_for, session
import requests
from fpdf import FPDF
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session

API_KEY = "yGchuojQqYfLSThgCK50KBzGdXQmqffL"
LOCATION_API_URL = "http://dataservice.accuweather.com/locations/v1/cities/search"
WEATHER_API_URL = "http://dataservice.accuweather.com/currentconditions/v1/"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            location_params = {"apikey": API_KEY, "q": city}
            loc_response = requests.get(LOCATION_API_URL, params=location_params)
            if loc_response.status_code == 200 and loc_response.json():
                location_key = loc_response.json()[0]["Key"]
                city_name = loc_response.json()[0]["LocalizedName"]

                weather_params = {"apikey": API_KEY}
                weather_response = requests.get(WEATHER_API_URL + location_key, params=weather_params)
                if weather_response.status_code == 200 and weather_response.json():
                    data = weather_response.json()[0]
                    weather = {
                        "city": city_name,
                        "temperature": data["Temperature"]["Metric"]["Value"],
                        "description": data["WeatherText"],
                        "humidity": data.get("RelativeHumidity", "N/A")
                    }
                    session['weather'] = weather
    return render_template("index.html", weather=weather)

@app.route("/download")
def download():
    weather = session.get("weather")
    if not weather:
        return redirect(url_for("index"))

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Weather Forecast for {weather['city']}", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Temperature: {weather['temperature']} °C", ln=True)
    pdf.cell(200, 10, txt=f"Description: {weather['description']}", ln=True)
    pdf.cell(200, 10, txt=f"Humidity: {weather['humidity']}%", ln=True)

    pdf_file = f"{weather['city']}_weather.pdf"
    pdf.output(pdf_file)
    
    return send_file(pdf_file, as_attachment=True)

@app.after_request
def cleanup(response):
    for filename in os.listdir():
        if filename.endswith("_weather.pdf"):
            os.remove(filename)
    return response

if __name__ == "__main__":
    app.run(debug=True)
